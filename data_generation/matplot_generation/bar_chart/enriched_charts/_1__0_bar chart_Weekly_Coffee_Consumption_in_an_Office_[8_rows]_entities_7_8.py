
import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours = [8, 6.5, 7, 5.5, 9, 4, 10]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(days, hours, width=0.5, 
              color=['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33', '#57FF33', '#8F33FF'])

ax.set_title('Weekly Study Hours', fontsize=16)
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Hours', fontsize=12)

ax.xaxis.set_tick_params(labelsize=10)
ax.yaxis.set_tick_params(labelsize=10)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.2, f'{height} hrs',
            va='bottom', ha='center', fontsize=10)

plt.tight_layout()
plt.show()