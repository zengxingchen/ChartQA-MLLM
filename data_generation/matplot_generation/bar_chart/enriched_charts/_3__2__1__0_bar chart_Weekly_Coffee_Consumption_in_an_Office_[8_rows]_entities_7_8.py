
import matplotlib.pyplot as plt

activities = ["Reading", "Writing", "Coding", "Exercise", "Meditation", "Cooking", "Sleeping", "Socializing", "Traveling", "Learning"]
hours = [8, 5, 12, 6, 4, 7, 8, 5, 3, 9]

fig, ax = plt.subplots(figsize=(10, 14))

bars = ax.bar(activities, hours, width=0.6,
              color=['#8B0000', '#FF8C00', '#FFD700', '#ADFF2F', '#00FF00', '#00CED1', '#1E90FF', '#4B0082', '#9400D3', '#FF1493'])

ax.set_title('Weekly Activity Distribution', fontsize=18, pad=20)
ax.set_ylabel('Hours', fontsize=14)
ax.set_xlabel('Activity', fontsize=14)

ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height} hrs',
            va='bottom', ha='center', fontsize=12)

plt.tight_layout()
plt.show()