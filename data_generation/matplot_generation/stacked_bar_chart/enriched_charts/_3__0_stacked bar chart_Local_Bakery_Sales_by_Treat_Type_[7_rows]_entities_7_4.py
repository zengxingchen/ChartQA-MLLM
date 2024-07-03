
import matplotlib.pyplot as plt

# Data points based on the table provided
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
running_hours = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
yoga_hours = [15, 20, 18, 22, 25, 28, 30, 32, 35, 38, 40, 42]
strength_training_hours = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]

fig, ax = plt.subplots(figsize=(12, 10))

# Stacked bar chart with custom colors and vertical orientation
bars_running = plt.bar(months, running_hours, color='#4CAF50', edgecolor='white', width=0.7, label='Running')
bars_yoga = plt.bar(months, yoga_hours, bottom=running_hours, color='#FFC107', edgecolor='white', width=0.7, label='Yoga')
bars_strength_training = plt.bar(months, strength_training_hours, bottom=[i+j for i,j in zip(running_hours, yoga_hours)], color='#F44336', edgecolor='white', width=0.7, label='Strength Training')

# Customizing the axes and title
ax.set_ylabel('Hours')
ax.set_title('Monthly Hours Spent on Fitness Activities')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Activities')

# Adding numerical labels
for bars in [bars_running, bars_yoga, bars_strength_training]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + yval / 2, int(yval), ha='center', va='center')

# Padding between the end of the bars and the edge of the figure
plt.margins(x=0.1)

# Display the plot
plt.show()