
import matplotlib.pyplot as plt

data = [
    {'Week': '2023-W09', 'Steps': 8200},
    {'Week': '2023-W10', 'Steps': 7900},
    {'Week': '2023-W11', 'Steps': 8100},
    {'Week': '2023-W12', 'Steps': 7800},
    {'Week': '2023-W13', 'Steps': 7600},
    {'Week': '2023-W14', 'Steps': 7300},
    {'Week': '2023-W15', 'Steps': 7400},
    {'Week': '2023-W16', 'Steps': 7100},
    {'Week': '2023-W17', 'Steps': 7200},
    {'Week': '2023-W18', 'Steps': 6900},
    {'Week': '2023-W19', 'Steps': 7000},
    {'Week': '2023-W20', 'Steps': 6700},
    {'Week': '2023-W21', 'Steps': 6800},
    {'Week': '2023-W22', 'Steps': 6500},
    {'Week': '2023-W23', 'Steps': 6600},
    {'Week': '2023-W24', 'Steps': 6300}
]

weeks = [entry['Week'] for entry in data]
steps = [entry['Steps'] for entry in data]

plt.figure(figsize=(16, 8))
line, = plt.plot(weeks, steps, color='#FF5733', linestyle='-', linewidth=2, marker='o', markerfacecolor='#1F618D', markeredgewidth=2, markersize=8)

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

plt.title('Weekly Mental Well-being Score in 2023', fontsize=18, fontweight='bold', y=1.05)
plt.xlabel('Week', fontsize=14)
plt.ylabel('Score', fontsize=14)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
plt.xticks(rotation=45)
plt.gca().invert_yaxis()
plt.tight_layout()

plt.show()