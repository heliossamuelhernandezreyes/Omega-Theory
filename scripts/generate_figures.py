from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "selected"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

p = DATA / "delivery_19__test_04_produccion_entropia.csv"
if p.exists():
    d = pd.read_csv(p)
    plt.figure(figsize=(8, 5.2))
    for model, g in d.groupby("model"):
        plt.plot(g.path_length, g.mean_entropy_production, marker="o", label=model)
    plt.xlabel("Longitud del camino")
    plt.ylabel("Producción media de entropía")
    plt.title("Producción media de entropía por longitud")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG / "core_entropy_production.png", dpi=180)
    plt.close()

p = DATA / "delivery_21__test_02_aditividad_energia_frecuencia.csv"
if p.exists():
    d = pd.read_csv(p).sort_values("mean_additivity_error")
    plt.figure(figsize=(8, 5.2))
    plt.barh(d.candidate, d.mean_additivity_error)
    plt.xscale("symlog", linthresh=1e-15)
    plt.xlabel("Error medio de aditividad")
    plt.title("Prueba de candidatos energía–frecuencia")
    plt.tight_layout()
    plt.savefig(FIG / "core_energy_frequency_additivity.png", dpi=180)
    plt.close()

p = DATA / "delivery_18__monotonicity_summary.csv"
if p.exists():
    d = pd.read_csv(p).iloc[0]
    values = [
        100 * d.trials_with_global_decrease / d.trials,
        100 * d.trials_with_local_macro_entropy_decrease / d.trials,
    ]
    plt.figure(figsize=(7, 5))
    plt.bar(["Conteo global", "Entropía macro actual"], values)
    plt.ylabel("Trayectorias con al menos una disminución (%)")
    plt.title("Monotonía global frente a local")
    plt.tight_layout()
    plt.savefig(FIG / "core_global_vs_local_monotonicity.png", dpi=180)
    plt.close()
