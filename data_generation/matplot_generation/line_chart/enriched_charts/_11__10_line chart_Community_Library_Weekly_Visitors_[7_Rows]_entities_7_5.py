
import matplotlib.pyplot as plt

data = [
    {'Week': '2023-W09', 'Steps': 7000},
    {'Week': '2023-W10', 'Steps': 7200},
    {'Week': '2023-W11', 'Steps': 6800},
    {'Week': '2023-W12', 'Steps': 7500},
    {'Week': '2023-W13', 'Steps': 7300},
    {'Week': '2023-W14', 'Steps': 6900},
    {'Week': '2023-W15', 'Steps': 7100},
    {'Week': '2023-W16', 'Steps': 7400},
    {'Week': '2023-W17', 'Steps': 7200},
    {'Week': '2023-W18', 'Steps': 7600},
    {'Week': '2023-W19', 'Steps': 7800},
    {'Week': '2023-W20', 'Steps': 7500},
    {'Week': '2023-W21', 'Steps': 7700},
    {'Week': '2023-W22', 'Steps': 7900},
    {'Week': '2023-W23', 'Steps': 8100},
    {'Week': '2023-W24', 'Steps': 8000}
]

weeks = [entry['Week'] for entry in data]
steps = [entry['Steps'] for entry in data]

plt.figure(figsize=(14, 7))
line, = plt.plot(weeks, steps, color='#2ca02c', linestyle='-', linewidth=2, marker='o', markerfacecolor='#d62728', markeredgewidth=2, markersize=8)

max_steps = max(steps)
max_week = weeks[steps.index(max_steps)]
plt.annotate(f'Peak\n{max_steps}', xy=(max_week, max_steps), xytext=(max_week, max_steps + 300),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

min_steps = min(steps)
min_week = weeks[steps.index(min_steps)]
plt.annotate(f'Low\n{min_steps}', xy=(min_week, min_steps), xytext=(min_week, min_steps - 300),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='center')

plt.title('Weekly Steps Count in 2023', fontsize=18, fontweight='bold', y=1.05)
plt.xlabel('Week', fontsize=14)
plt.ylabel('Number of Steps', fontsize=14)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()