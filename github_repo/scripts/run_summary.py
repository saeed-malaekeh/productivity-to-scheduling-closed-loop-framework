from pathlib import Path
import pandas as pd
base = Path(__file__).resolve().parents[1]
perf = pd.read_csv(base / 'data/project_performance_comparison_double_improvement.csv')
print('Average PPC, manual:', round(perf['ppc_manual'].mean(), 1))
print('Average PPC, monitoring only:', round(perf['ppc_monitoring_only'].mean(), 1))
print('Average PPC, closed-loop:', round(perf['ppc_closed_loop'].mean(), 1))
print('Final cumulative slip, manual:', round(perf['slip_manual'].iloc[-1], 1))
print('Final cumulative slip, monitoring only:', round(perf['slip_monitoring_only'].iloc[-1], 1))
print('Final cumulative slip, closed-loop:', round(perf['slip_closed_loop'].iloc[-1], 1))
