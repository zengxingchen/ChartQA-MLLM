
import matplotlib.pyplot as plt

# Data
years = ['2018', '2019', '2020', '2021', '2022']
adventure_activities = [400, 420, 380, 460, 480]
relaxation_activities = [300, 330, 350, 370, 390]

# Colors
colors_adventure = ['#FF6347', '#FF4500', '#FF7F50', '#FF8C00', '#FFA07A']
colors_relaxation = ['#4682B4', '#5F9EA0', '#6495ED', '#00CED1', '#40E0D0']

# Plot
fig, ax = plt.subplots(figsize=(12, 6))  # Change width and height of the chart

bar_width = 0.5  # Change band width for bars

# Creating a vertical stacked bar chart
bars_adventure = plt.bar(years, adventure_activities, color=colors_adventure, edgecolor='white', width=bar_width)
bars_relaxation = plt.bar(years, relaxation_activities, bottom=adventure_activities, color=colors_relaxation, edgecolor='white', width=bar_width)

# Adding labels and title
plt.ylabel('Number of Activities')
plt.title('Annual Comparison of Adventure and Relaxation Activities', pad=20)

# Adding numerical labels on each bar
for bar in bars_adventure + bars_relaxation:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Customizing the axes
plt.ylim(0, 1000)  # Adjust the y-axis limit to accommodate the stack

# Display the plot
plt.show()