
import matplotlib.pyplot as plt

subjects = ["Reading", "Writing", "Mathematics", "Science", "History", "Art"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

data = [
    [5, 6.5, 7, 5.5, 8, 4, 6],
    [4.5, 5, 6.5, 6, 7, 3.5, 5.5],
    [6, 7.5, 8, 7, 9, 5.5, 7.5],
    [5.5, 6, 7, 6.5, 8.5, 4.5, 6.5],
    [4, 5.5, 6, 5.5, 7, 3, 5],
    [5, 5.5, 6.5, 6, 7.5, 4, 5.5]
]

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.4
bars = []

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33', '#57FF33', '#8F33FF']

for i, subject in enumerate(subjects):
    bars.append(ax.barh(days, data[i], height=width, color=colors[i], label=subject))

ax.set_title('Weekly Study Hours by Subject', fontsize=18, pad=20)
ax.set_xlabel('Hours', fontsize=14)
ax.set_ylabel('Day', fontsize=14)
ax.set_xlim(3, 10)

ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

for bar_set in bars:
    for bar in bar_set:
        width = bar.get_width()
        ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, f'{width} hrs',
                va='center', ha='left', fontsize=10)

plt.legend(title="Subjects", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()