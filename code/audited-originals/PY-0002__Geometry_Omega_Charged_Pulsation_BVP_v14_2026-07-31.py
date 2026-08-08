"""
Geometry Omega charged radial pulsation BVP — v14.

This file implements the dimensionless five-variable system described in:
Geometry_Omega_BVP_Cargado_Adimensional_v14_2026-07-31.md

The solver intentionally refuses to regularize Z/f**2 with an arbitrary floor.
It requires a background profile containing:
x, f, fx, h, N, alpha_physical, w_physical, wx_physical

The numerical execution should begin with the neutral-limit control.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_bvp


@dataclass
class Background:
    x: np.ndarray
    f: np.ndarray
    fx: np.ndarray
    h: np.ndarray
    N: np.ndarray
    alpha: np.ndarray
    w: np.ndarray
    wx: np.ndarray
    kappa: float
    e: float
    a: float = 1.0
    b: float = 1.0

    @classmethod
    def from_csv(cls, path: str | Path, *, kappa: float, e: float) -> "Background":
        df = pd.read_csv(path)
        required = {
            "x", "f", "fx", "h", "N",
            "alpha_physical", "w_physical", "wx_physical"
        }
        missing = required.difference(df.columns)
        if missing:
            raise ValueError(f"Missing background columns: {sorted(missing)}")
        return cls(
            x=df["x"].to_numpy(),
            f=df["f"].to_numpy(),
            fx=df["fx"].to_numpy(),
            h=df["h"].to_numpy(),
            N=df["N"].to_numpy(),
            alpha=df["alpha_physical"].to_numpy(),
            w=df["w_physical"].to_numpy(),
            wx=df["wx_physical"].to_numpy(),
            kappa=kappa,
            e=e,
        )


class ChargedPulsationBVP:
    def __init__(self, bg: Background):
        self.bg = bg
        x = bg.x
        self.spl = {
            name: CubicSpline(x, getattr(bg, name))
            for name in ("f", "fx", "h", "N", "alpha", "w", "wx")
        }

    def background(self, x: np.ndarray) -> dict[str, np.ndarray]:
        out = {name: spl(x) for name, spl in self.spl.items()}
        out["Nx"] = self.spl["N"].derivative()(x)
        out["alphax"] = self.spl["alpha"].derivative()(x)
        return out

    def rhs(self, x: np.ndarray, y: np.ndarray, p: np.ndarray) -> np.ndarray:
        lam = float(p[0])
        eta, pi, u, Z, H0 = y
        b = self.background(x)
        f, fx = b["f"], b["fx"]
        N, Nx = b["N"], b["Nx"]
        alpha, alphax = b["alpha"], b["alphax"]
        w, wx = b["w"], b["wx"]
        kappa, e, a, bb = self.bg.kappa, self.bg.e, self.bg.a, self.bg.b

        if np.any(f == 0):
            raise FloatingPointError("The chosen domain contains f=0 exactly.")

        sqrtN = np.sqrt(N)
        V1 = 1 - 2*a*f*f + 3*bb*f**4
        V2 = 1 - 6*a*f*f + 15*bb*f**4

        fxx = -(2/x + alphax/alpha + Nx/(2*N))*fx
        fxx -= ((w*w/alpha**2 - V1)/N)*f

        H2 = 2*kappa*x*fx*eta + kappa*w*Z/(alpha*x*sqrtN)

        Zx = 2*x*x/(alpha*sqrtN) * (
            2*f*eta*w - f*f*u + 0.5*f*f*w*(-H0 + H2)
        )

        ux = lam*Z/(2*alpha*x*x*sqrtN*f*f)
        ux -= e*e*alpha*Z/(x*x*sqrtN)
        ux -= 0.5*wx*(H0 + H2)

        # Differentiate the algebraic H2 expression.
        term = w*Z/(alpha*x*sqrtN)
        term_x = (
            wx*Z/(alpha*x*sqrtN)
            + w*Zx/(alpha*x*sqrtN)
            - w*Z*alphax/(alpha**2*x*sqrtN)
            - w*Z/(alpha*x*x*sqrtN)
            - w*Z*Nx/(2*alpha*x*N*sqrtN)
        )
        H2x = 2*kappa*((fx + x*fxx)*eta + x*fx*pi) + kappa*term_x

        em_rho = sqrtN*wx*Z/(alpha*x*x)
        Ttt_scalar = (
            H0*f*f*w*w/alpha**2 + N*H2*fx*fx - 2*N*fx*pi
            - 2*f*eta*w*w/alpha**2 + 2*f*f*u*w/alpha**2
            - 2*f*V1*eta
        )
        Trr_scalar = (
            -H0*f*f*w*w/alpha**2 - N*H2*fx*fx + 2*N*fx*pi
            + 2*f*eta*w*w/alpha**2 - 2*f*f*u*w/alpha**2
            - 2*f*V1*eta
        )
        Ttt = Ttt_scalar - em_rho
        Trr = Trr_scalar - em_rho

        H0x = kappa*x*Trr/N + 2*alphax*H2/alpha + H2/x

        dg_box = (
            -N*H2*fxx - N*H2*alphax*fx/alpha - 0.5*Nx*H2*fx
            + 0.5*N*(H0x - H2x)*fx - 2*N*H2*fx/x
        )

        pix = -(
            (2*N/x + N*alphax/alpha + 0.5*Nx)*pi
            + ((lam + w*w)/alpha**2 - V2)*eta
            - 2*f*w*u/alpha**2
            - f*w*w*H0/alpha**2
            + dg_box
        )/N

        return np.vstack((pi, pix, ux, Zx, H0x))

    def bc(self, ya: np.ndarray, yb: np.ndarray, p: np.ndarray) -> np.ndarray:
        lam = float(p[0])
        # Conservative scalar Robin approximation. The full two-band
        # asymptotic condition must replace this after neutral validation.
        k = np.sqrt(max(1.0 - self.bg.w[-1]**2 - max(lam, 0.0), 1e-12))
        return np.array([
            ya[0] - 1.0,  # normalization
            ya[1],        # eta'(0)=0
            ya[3],        # Z(0)=0
            yb[1] + k*yb[0],
            yb[3],        # fixed total charge
            yb[2],        # u(infinity)=0
        ])

    def solve(self, lam_guess: float = 1e-3):
        x = self.bg.x
        decay = np.exp(-0.2*(x-x[0]))
        y0 = np.vstack([
            decay,
            -0.2*decay,
            np.zeros_like(x),
            np.zeros_like(x),
            np.zeros_like(x),
        ])
        return solve_bvp(
            self.rhs, self.bc, x, y0, p=np.array([lam_guess]),
            tol=1e-5, max_nodes=100000, verbose=1
        )


if __name__ == "__main__":
    raise SystemExit(
        "Import ChargedPulsationBVP and provide a complete charged background."
    )
