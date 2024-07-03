
import matplotlib.pyplot as plt

destinations = ["Paris", "London", "Berlin", "Rome", "Madrid", "Lisbon", "Vienna", "Amsterdam", "Prague", "Brussels"]
distances = [450, 350, 600, 800, 1200, 1500, 700, 500, 900, 400]

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.barh(destinations, distances, height=0.6, color=['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF'])

ax.set_title('Travel Distances to Popular Destinations', fontsize=18, pad=20)
ax.set_xlabel('Distance (km)', fontsize=14)
ax.set_ylabel('Destination', fontsize=14)

ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 20, bar.get_y() + bar.get_height()/2, f'{width} km', va='center', ha='left', fontsize=12)

plt.tight_layout()
plt.show()