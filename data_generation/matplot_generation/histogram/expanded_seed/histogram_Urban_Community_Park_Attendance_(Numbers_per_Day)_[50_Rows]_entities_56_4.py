
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

# The given chart table data
data = [{'Day': 'Monday', 'Number of Visitors': 320},
        {'Day': 'Tuesday', 'Number of Visitors': 285},
        {'Day': 'Wednesday', 'Number of Visitors': 340},
        {'Day': 'Thursday', 'Number of Visitors': 390},
        {'Day': 'Friday', 'Number of Visitors': 560},
        {'Day': 'Saturday', 'Number of Visitors': 610},
        {'Day': 'Sunday', 'Number of Visitors': 580},
        {'Day': 'Monday', 'Number of Visitors': 300},
        {'Day': 'Tuesday', 'Number of Visitors': 270},
        {'Day': 'Wednesday', 'Number of Visitors': 350},
        {'Day': 'Thursday', 'Number of Visitors': 410},
        {'Day': 'Friday', 'Number of Visitors': 570},
        {'Day': 'Saturday', 'Number of Visitors': 620},
        {'Day': 'Sunday', 'Number of Visitors': 600},
        {'Day': 'Monday', 'Number of Visitors': 310}]

# Processing the data
visitors_per_day = defaultdict(list)

for entry in data:
    visitors_per_day[entry['Day']].append(entry['Number of Visitors'])

# Define days of the week to maintain the order
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Prepare data for plotting
visitors_avg = [np.mean(visitors_per_day[day]) for day in days]

# Colors, edge colors and hatch patterns for diversity
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
edge_colors = ['#333333'] * 7  # same edge color for all bars for clarity
hatch_patterns = ['/', '\\', '|', '-', '+', 'x', 'o']

# Plotting the bar chart
plt.figure(figsize=(10, 5))
bars = plt.bar(days, visitors_avg, color=colors, edgecolor=edge_colors, hatch=hatch_patterns)

# Adding chart titles and labels
plt.title('Average Number of Visitors per Day')
plt.xlabel('Day of the Week')
plt.ylabel('Average Number of Visitors')

# Show the average value on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, round(yval, 1), ha='center', va='bottom')

# Show the plot
plt.show()