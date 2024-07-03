
import matplotlib.pyplot as plt
import numpy as np

# Given table data
data = [
    {'Day': 'Monday', 'Coffee (cups)': 150, 'Tea (cups)': 70, 'Smoothies (cups)': 30, 'Hot Chocolate (cups)': 50},
    {'Day': 'Tuesday', 'Coffee (cups)': 135, 'Tea (cups)': 65, 'Smoothies (cups)': 28, 'Hot Chocolate (cups)': 45},
    {'Day': 'Wednesday', 'Coffee (cups)': 160, 'Tea (cups)': 75, 'Smoothies (cups)': 35, 'Hot Chocolate (cups)': 55},
    {'Day': 'Thursday', 'Coffee (cups)': 170, 'Tea (cups)': 80, 'Smoothies (cups)': 40, 'Hot Chocolate (cups)': 60},
    {'Day': 'Friday', 'Coffee (cups)': 200, 'Tea (cups)': 90, 'Smoothies (cups)': 50, 'Hot Chocolate (cups)': 70},
    {'Day': 'Saturday', 'Coffee (cups)': 220, 'Tea (cups)': 100, 'Smoothies (cups)': 60, 'Hot Chocolate (cups)': 80},
    {'Day': 'Sunday', 'Coffee (cups)': 180, 'Tea (cups)': 85, 'Smoothies (cups)': 45, 'Hot Chocolate (cups)': 65}
]

# Extracting data
days = [d['Day'] for d in data]
coffee = [d['Coffee (cups)'] for d in data]
tea = [d['Tea (cups)'] for d in data]
smoothies = [d['Smoothies (cups)'] for d in data]
hot_chocolate = [d['Hot Chocolate (cups)'] for d in data]

# Number of groups
n_groups = len(days)

# Create a bar width
bar_width = 0.2

# Set position of bar on X axis
r1 = np.arange(n_groups)
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

# Make the plot
plt.bar(r1, coffee, color='b', width=bar_width, edgecolor='grey', label='Coffee')
plt.bar(r2, tea, color='r', width=bar_width, edgecolor='grey', label='Tea')
plt.bar(r3, smoothies, color='g', width=bar_width, edgecolor='grey', label='Smoothies')
plt.bar(r4, hot_chocolate, color='y', width=bar_width, edgecolor='grey', label='Hot Chocolate')

# Add labels to the x-axis and y-axis
plt.xlabel('Days of the Week', fontweight='bold', fontsize=15)
plt.ylabel('Cups Sold', fontweight='bold', fontsize=15)

# Add the days as the x-axis labels and rotate them for better visibility
plt.xticks([r + bar_width for r in range(n_groups)], days, rotation=45)

# Create a legend
plt.legend()

# Set a title
plt.title('Cups of Drinks Sold per Day')

# Show the plot
plt.tight_layout()
plt.show()