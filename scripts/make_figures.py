from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
base = Path(__file__).resolve().parents[1]
perf = pd.read_csv(base / 'data/project_performance_comparison_double_improvement.csv')
fig, ax = plt.subplots(figsize=(10,5), dpi=220)
x = range(len(perf))
dates = pd.to_datetime(perf['date']).dt.strftime('%b %d')
ax.plot(x, perf['ppc_manual'], label='Manual control')
ax.plot(x, perf['ppc_monitoring_only'], label='Monitoring only')
ax.plot(x, perf['ppc_closed_loop'], label='Closed-loop control')
ax.set_ylabel('PPC (%)')
ax.set_xticks(list(x)[::2]); ax.set_xticklabels(dates[::2], rotation=45, ha='right', fontsize=8)
ax.legend(frameon=False); ax.grid(alpha=0.25)
fig.tight_layout(); (base / 'figures').mkdir(exist_ok=True); fig.savefig(base / 'figures' / 'regime_comparison_from_repo.png', bbox_inches='tight')
