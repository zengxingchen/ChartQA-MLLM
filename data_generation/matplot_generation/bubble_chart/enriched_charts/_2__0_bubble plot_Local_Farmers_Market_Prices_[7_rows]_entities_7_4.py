
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
walking = [5, 6, 4.5, 5.5, 6, 7, 6.5]        # Average hours spent on walking
reading = [2, 1.5, 2, 2.5, 3, 4, 3.5]        # Average hours spent on reading
working_out = [1, 1.5, 1, 2, 1, 2, 2]        # Average hours spent on working out
relaxing = [3, 3.5, 4, 2.5, 4, 5, 6]         # Average hours spent on relaxing

# Plot setting (adjusting width and height)
plt.figure(figsize=(16, 9))

# Bubble chart
for i in range(len(days)):
    plt.scatter(days[i], walking[i], s=walking[i]*30, alpha=0.5, color='#1f77b4', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], reading[i], s=reading[i]*30, alpha=0.5, color='#ff7f0e', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], working_out[i], s=working_out[i]*30, alpha=0.5, color='#2ca02c', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], relaxing[i], s=relaxing[i]*30, alpha=0.5, color='#d62728', edgecolors='w', linewidth=0.5)

# Customizing the plot
plt.title('Average Time Spent on Daily Activities (Hours) - Week Overview', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Average Hours')
plt.xticks(rotation=45)

# Custom legend
for activity, color in zip(["Walking", "Reading", "Working Out", "Relaxing"], ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']):
    plt.scatter([], [], alpha=0.5, s=100, label=activity, color=color, edgecolors='w', linewidth=0.5)
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='upper right', title="Activities")

plt.tight_layout()
plt.show()