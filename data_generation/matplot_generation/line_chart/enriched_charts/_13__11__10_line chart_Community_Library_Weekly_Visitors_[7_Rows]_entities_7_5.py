
import matplotlib.pyplot as plt

data = [
    {'Week': '2023-W09', 'Steps': 7800},
    {'Week': '2023-W10', 'Steps': 7500},
    {'Week': '2023-W11', 'Steps': 7900},
    {'Week': '2023-W12', 'Steps': 7700},
    {'Week': '2023-W13', 'Steps': 8100},
    {'Week': '2023-W14', 'Steps': 7300},
    {'Week': '2023-W15', 'Steps': 8200},
    {'Week': '2023-W16', 'Steps': 8000},
    {'Week': '2023-W17', 'Steps': 8500},
    {'Week': '2023-W18', 'Steps': 8300},
    {'Week': '2023-W19', 'Steps': 8600},
    {'Week': '2023-W20', 'Steps': 8400},
    {'Week': '2023-W21', 'Steps': 8700},
    {'Week': '2023-W22', 'Steps': 8600},
    {'Week': '2023-W23', 'Steps': 8900},
    {'Week': '2023-W24', 'Steps': 8800}
]

weeks = [entry['Week'] for entry in data]
steps = [entry['Steps'] for entry in data]

plt.figure(figsize=(16, 8))
line, = plt.plot(weeks, steps, color='#1f77b4', linestyle='-', linewidth=2, marker='s', markerfacecolor='#ff7f0e', markeredgewidth=2, markersize=8)

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

plt.title('Weekly Step Count in 2023: Analyzing Physical Activity Trends', fontsize=18, fontweight='bold', y=1.05)
plt.xlabel('Week', fontsize=14)
plt.ylabel('Number of Steps', fontsize=14)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
plt.xticks(rotation=45)
plt.gca().invert_yaxis()  # Inverting the y-axis
plt.tight_layout()

plt.show()