
import matplotlib.pyplot as plt

activities = ["Sleeping", "Working", "Exercising", "Meditating", "Socializing", "Reading", "Learning", "Cooking", "Traveling", "Relaxing"]
hours = [8, 9, 5, 4, 6, 3, 8, 7, 4, 6]

fig, ax = plt.subplots(figsize=(14, 10))

bars = ax.barh(activities, hours, height=0.5,
              color=['#8B0000', '#FF8C00', '#FFD700', '#ADFF2F', '#00FF00', '#00CED1', '#1E90FF', '#4B0082', '#9400D3', '#FF1493'])

ax.set_title('Weekly Health & Psychology Activities Distribution', fontsize=18, pad=20)
ax.set_xlabel('Hours', fontsize=14)
ax.set_ylabel('Activity', fontsize=14)
ax.set_xlim(3, 10)

ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, f'{width} hrs',
            va='center', ha='left', fontsize=12)

plt.tight_layout()
plt.show()