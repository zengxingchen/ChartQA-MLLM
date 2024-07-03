
import matplotlib.pyplot as plt

# Definition of data points
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
cardio = [10, 12, 14, 16, 18, 20, 22, 24]
strength = [8, 9, 10, 11, 12, 13, 14, 15]
flexibility = [5, 6, 7, 8, 9, 10, 11, 12]
balance = [3, 4, 5, 6, 7, 8, 9, 10]
endurance = [4, 5, 6, 7, 8, 9, 10, 11]

# Colors for the data series for better clarity
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF']

# Create a figure and a set of subplots - modify width and height of the chart
fig, ax = plt.subplots(figsize=(10, 8))

# Change the width of bars
bar_height = 0.6

# Stacking bars horizontally
ax.barh(years, cardio, color=colors[0], edgecolor='white', height=bar_height, label='Cardio')
ax.barh(years, strength, left=cardio, color=colors[1], edgecolor='white', height=bar_height, label='Strength')
ax.barh(years, flexibility, left=[i+j for i,j in zip(cardio, strength)], color=colors[2], edgecolor='white', height=bar_height, label='Flexibility')
ax.barh(years, balance, left=[i+j+k for i,j,k in zip(cardio, strength, flexibility)], color=colors[3], edgecolor='white', height=bar_height, label='Balance')
ax.barh(years, endurance, left=[i+j+k+l for i,j,k,l in zip(cardio, strength, flexibility, balance)], color=colors[4], edgecolor='white', height=bar_height, label='Endurance')

# Labeling the chart
ax.set_xlabel('Percentage (%)')
ax.set_title('Composition of Physical Activities by Type (2016-2023)', pad=20)

# Displaying the legend
ax.legend(loc='lower right')

# Adding numerical labels
for i, (c, s, f, b, e) in enumerate(zip(cardio, strength, flexibility, balance, endurance)):
    total = c + s + f + b + e
    ax.text(total + 1, i, str(total), va='center')

# Show the plot
plt.tight_layout()
plt.show()