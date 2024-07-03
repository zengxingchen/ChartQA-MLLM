
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
math_scores = [78, 80, 82, 85, 88, 90, 92, 94, 96, 98, 99]
science_scores = [85, 82, 88, 90, 92, 94, 95, 97, 99, 100, 101]

# Colors
colors_math = ['#4CAF50', '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800', '#FF5722', '#F44336', '#E91E63', '#9C27B0', '#673AB7']
colors_science = ['#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800', '#FF5722']

# Plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

bar_height = 0.4  # Change band height for bars

# Creating a horizontal stacked bar chart
bars_math = plt.barh(years, math_scores, color=colors_math, edgecolor='white', height=bar_height)
bars_science = plt.barh(years, science_scores, left=math_scores, color=colors_science, edgecolor='white', height=bar_height)

# Adding labels and title
plt.xlabel('Scores')
plt.title('Annual Academic Performance: Math vs Science', pad=20)

# Customizing the axes
plt.xlim(0, 200)  # Adjust the x-axis limit to accommodate the stack

# Adding numerical labels
for index, value in enumerate(math_scores):
    plt.text(value / 2, index, str(value), ha='center', va='center', color='black')
for index, value in enumerate(science_scores):
    plt.text(math_scores[index] + value / 2, index, str(value), ha='center', va='center', color='black')

# Display the plot
plt.show()