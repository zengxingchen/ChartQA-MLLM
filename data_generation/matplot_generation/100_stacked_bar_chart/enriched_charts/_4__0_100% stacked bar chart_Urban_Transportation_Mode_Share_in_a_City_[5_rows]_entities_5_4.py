
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Stress', 'Anxiety', 'Depression', 'Sleep Quality', 'Physical Activity', 'Diet', 'Social Support']
low = np.array([20, 25, 15, 30, 35, 25, 20])
medium = np.array([35, 30, 25, 40, 25, 35, 40])
high = np.array([45, 45, 60, 30, 40, 40, 40])

# Normalize the data to get percentages
total = low + medium + high
low_percentage = np.true_divide(low, total) * 100
medium_percentage = np.true_divide(medium, total) * 100
high_percentage = np.true_divide(high, total) * 100

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot vertical bars
bar_width = 0.6
indices = np.arange(len(categories))
ax.bar(indices, low_percentage, color='#FF6347', edgecolor='white', width=bar_width, label='Low')
ax.bar(indices, medium_percentage, bottom=low_percentage, color='#FFD700', edgecolor='white', width=bar_width, label='Medium')
ax.bar(indices, high_percentage, bottom=low_percentage + medium_percentage, color='#4682B4', edgecolor='white', width=bar_width, label='High')

# Add labels and title
ax.set(xticks=indices, xticklabels=categories, ylabel='Percentage')
ax.set_title('Mental Health Factors by Severity Level')

# Add legend
ax.legend(loc='upper left')

# Display the chart
plt.show()