
import matplotlib.pyplot as plt

cities = [
    "Boston", "London", "Berlin", "Chicago", "New York",
    "Tokyo", "Paris", "Los Angeles", "Amsterdam", "Vienna",
    "Barcelona", "Sydney"
]
average_temperature = [
    16, 14, 18, 15, 12, 
    10, 20, 22, 16, 14, 
    20, 18
]
annual_participants = [
    30000, 45000, 40000, 35000, 50000,
    38000, 25000, 28000, 35000, 30000,
    32000, 29000
]
event_rating = [
    85, 90, 88, 87, 92,
    89, 80, 78, 84, 83,
    86, 79
]

sizes = [rating * 10 for rating in event_rating]
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#aec7e8', '#ffbb78'
]

fig, ax = plt.subplots(figsize=(18, 12))
bubble = ax.scatter(average_temperature, cities, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

ax.set_title('Top Marathon Cities: Average Temperature vs. Participant Count', fontsize=20, pad=20)
ax.set_xlabel('Average Temperature (°C)', fontsize=16)
ax.set_ylabel('Cities', fontsize=16)

ax.grid(True)

for rating in sorted(set(event_rating), reverse=True):
    ax.scatter([], [], c='k', alpha=0.3, s=rating * 10, label=str(rating))
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Event Rating', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()