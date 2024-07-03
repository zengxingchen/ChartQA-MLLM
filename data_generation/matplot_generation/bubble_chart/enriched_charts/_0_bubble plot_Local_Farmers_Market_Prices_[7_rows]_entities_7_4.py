
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sleeping = [7, 6.5, 7, 6, 6.5, 8, 8]       # Average hours spent on sleeping
eating = [2, 2.5, 2, 2.5, 3, 3, 3]         # Average hours spent on eating
working = [9, 8.5, 8, 9, 7, 4, 3]          # Average hours spent on working
leisure = [6, 6.5, 7, 6.5, 7.5, 9, 10]     # Average hours spent on leisure

# Plot setting (adjusting width and height)
plt.figure(figsize=(14, 8))

# Bubble chart
for i in range(len(days)):
    plt.scatter(days[i], sleeping[i], s=sleeping[i]*30, alpha=0.5, color='#3498db', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], eating[i], s=eating[i]*30, alpha=0.5, color='#e74c3c', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], working[i], s=working[i]*30, alpha=0.5, color='#2ecc71', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], leisure[i], s=leisure[i]*30, alpha=0.5, color='#f39c12', edgecolors='w', linewidth=0.5)

# Customizing the plot
plt.title('Average Time Spent on Daily Activities (Hours) - Week Overview')
plt.xlabel('Day of the Week')
plt.ylabel('Average Hours')
plt.xticks(rotation=45)

# Custom legend
for activity, color in zip(["Sleeping", "Eating", "Working", "Leisure"], ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']):
    plt.scatter([], [], alpha=0.5, s=100, label=activity, color=color, edgecolors='w', linewidth=0.5)
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='upper left', title="Activities")

plt.tight_layout()
plt.show()