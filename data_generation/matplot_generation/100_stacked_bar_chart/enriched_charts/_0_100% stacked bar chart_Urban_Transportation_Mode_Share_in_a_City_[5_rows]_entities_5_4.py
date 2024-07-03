
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Python', 'Java', 'C++', 'JavaScript', 'C#']
beginner = np.array([25, 15, 10, 30, 20])
intermediate = np.array([35, 25, 40, 20, 30])
advanced = np.array([40, 60, 50, 50, 50])

# Normalize the data to get percentages
total = beginner + intermediate + advanced
beginner_percentage = np.true_divide(beginner, total) * 100
intermediate_percentage = np.true_divide(intermediate, total) * 100
advanced_percentage = np.true_divide(advanced, total) * 100

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot horizontal bars
bar_width = 0.8
indices = np.arange(len(categories))
ax.barh(indices, beginner_percentage, color='#ADD8E6', edgecolor='white', height=bar_width, label='Beginner')
ax.barh(indices, intermediate_percentage, left=beginner_percentage, color='#90EE90', edgecolor='white', height=bar_width, label='Intermediate')
ax.barh(indices, advanced_percentage, left=beginner_percentage + intermediate_percentage, color='#FFB6C1', edgecolor='white', height=bar_width, label='Advanced')

# Add labels and title
ax.set(yticks=indices, yticklabels=categories, xlabel='Percentage')
ax.set_title('Preferred Programming Languages by Expertise Level')

# Add legend
ax.legend(loc='upper right')

# Display the chart
plt.show()