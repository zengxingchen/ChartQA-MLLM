
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
physical_activity = [68, 70, 73, 76, 79, 82, 85, 87, 89, 91, 93]
healthy_eating = [75, 78, 80, 83, 85, 88, 90, 92, 95, 97, 100]

# Colors
colors_physical = ['#FF5733', '#FF6F33', '#FF8F33', '#FFA533', '#FFC233', '#FFE033', '#FFFF33', '#E0FF33', '#C3FF33', '#A6FF33', '#89FF33']
colors_healthy = ['#33FF57', '#33FF77', '#33FF97', '#33FFB7', '#33FFD7', '#33FFF7', '#33D7FF', '#33B7FF', '#3397FF', '#3377FF', '#3357FF']

# Plot
fig, ax = plt.subplots(figsize=(12, 10))  # Change width and height of the chart

bar_width = 0.4  # Change band width for bars

# Creating a vertical stacked bar chart
bars_physical = plt.bar(years, physical_activity, color=colors_physical, edgecolor='white', width=bar_width)
bars_healthy = plt.bar(years, healthy_eating, bottom=physical_activity, color=colors_healthy, edgecolor='white', width=bar_width)

# Adding labels and title
plt.ylabel('Scores')
plt.title('Health and Wellness: Physical Activity vs Healthy Eating', pad=20)

# Customizing the axes
plt.ylim(0, 200)  # Adjust the y-axis limit to accommodate the stack

# Adding numerical labels
for index, value in enumerate(physical_activity):
    plt.text(index, value / 2, str(value), ha='center', va='center', color='black')
for index, value in enumerate(healthy_eating):
    plt.text(index, physical_activity[index] + value / 2, str(value), ha='center', va='center', color='black')

# Display the plot
plt.show()