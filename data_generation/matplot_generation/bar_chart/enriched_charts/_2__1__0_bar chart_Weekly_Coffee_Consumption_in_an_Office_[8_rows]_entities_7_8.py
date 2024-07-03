
import matplotlib.pyplot as plt

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
minutes = [60, 45, 30, 75, 90, 120, 150]

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.barh(weekdays, minutes, height=0.6,
               color=['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#BA55D3', '#FFA500', '#DC143C'])

ax.set_title('Weekly Exercise Duration', fontsize=18)
ax.set_xlabel('Minutes', fontsize=14)
ax.set_ylabel('Day', fontsize=14)

ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, f'{width} min',
            va='center', ha='left', fontsize=12)

plt.tight_layout()
plt.show()