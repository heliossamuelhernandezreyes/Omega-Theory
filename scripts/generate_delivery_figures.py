from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "data" / "primary"
DERIVED = ROOT / "data" / "derived" / "deliveries_01_17"
FIG = ROOT / "figures" / "deliveries_01_17"
FIG.mkdir(parents=True, exist_ok=True)

# Delivery 01: bridge rate and spectral gap.
d = pd.read_csv(PRIMARY / "delivery_01" / "TEST_03_RUPTURA_CONTINUIDAD.csv")
pos = d[d.epsilon_bridge_rate > 0]
plt.figure(figsize=(7.5, 4.8))
plt.loglog(pos.epsilon_bridge_rate, pos.spectral_gap, marker="o")
plt.xlabel("Bridge rate epsilon")
plt.ylabel("Spectral gap")
plt.title("Delivery 01: continuity bridge and spectral gap")
plt.tight_layout()
plt.savefig(FIG / "d01_gap_vs_bridge.svg")
plt.close()

# Delivery 13: convergence of finite partitions toward exponential response.
d = pd.read_csv(DERIVED / "d13_partition_limit_summary.csv")
plt.figure(figsize=(7.5, 4.8))
for s, g in d.groupby("s"):
    plt.plot(g.n, g.relative_error, marker="o", label=f"s={s}")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Number of partitions")
plt.ylabel("Maximum relative error")
plt.title("Delivery 13: convergence to exponential response")
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "d13_partition_convergence.svg")
plt.close()

# Delivery 16: cycle insertion destroys topological ordering in tested graphs.
d = pd.read_csv(DERIVED / "d16_cycle_order_summary.csv")
plt.figure(figsize=(7.5, 4.8))
plt.plot(d.n, d.cyclic_fraction, marker="o", label="Cyclic fraction")
plt.plot(d.n, d.topological_order_fraction, marker="o", label="Topological-order fraction")
plt.xlabel("Graph size")
plt.ylabel("Fraction")
plt.title("Delivery 16: back edges and order failure")
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "d16_cycles_vs_order.svg")
plt.close()

# Delivery 17: allowing erasure restores exact recurrence.
d = pd.read_csv(PRIMARY / "delivery_17" / "TEST_04_BORRADO_HISTORIA.csv")
plt.figure(figsize=(7.5, 4.8))
plt.plot(d.erase_probability, d.fraction_trials_with_recurrence, marker="o")
plt.xscale("symlog", linthresh=1e-4)
plt.xlabel("History erasure probability")
plt.ylabel("Fraction with exact recurrence")
plt.title("Delivery 17: erasure reopens exact recurrence")
plt.tight_layout()
plt.savefig(FIG / "d17_erasure_recurrence.svg")
plt.close()
