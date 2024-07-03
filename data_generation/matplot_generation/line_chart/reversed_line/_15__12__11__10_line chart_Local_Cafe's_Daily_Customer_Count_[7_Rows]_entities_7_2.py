
import matplotlib.pyplot as plt

data = [
    {'Day': 'Monday', 'Step Count': 10000},
    {'Day': 'Tuesday', 'Step Count': 8500},
    {'Day': 'Wednesday', 'Step Count': 9000},
    {'Day': 'Thursday', 'Step Count': 8000},
    {'Day': 'Friday', 'Step Count': 7500},
    {'Day': 'Saturday', 'Step Count': 7000},
    {'Day': 'Sunday', 'Step Count': 6500}
]

days = [entry['Day'] for entry in data]
step_count = [entry['Step Count'] for entry in data]

plt.figure(figsize=(18, 6))
plt.plot(days, step_count, color='#ff7f0e', linestyle='-', marker='D', linewidth=2, markersize=8, label="Daily Step Count")

plt.title('Weekly Step Count Trend', fontsize=20, loc='center')
plt.xlabel('Day of the Week', fontsize=16)
plt.ylabel('Step Count', fontsize=16)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

for i, count in enumerate(step_count):
    plt.text(days[i], count - 500, str(count), ha='center', color='black')

max_count = max(step_count)
min_count = min(step_count)
plt.axhline(max_count, color='#2ca02c', linestyle='--', linewidth=1)
plt.axhline(min_count, color='#d62728', linestyle='--', linewidth=1)

plt.legend(loc='upper left')
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()