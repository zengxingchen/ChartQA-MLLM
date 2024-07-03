
import matplotlib.pyplot as plt
import numpy as np

# Generate data points - Weight (in kg) of 1000 individuals
weight_data = 50 + 50*np.random.beta(2, 5, 1000)  # Generates a diverse, non-uniform dataset

# Modify the color scheme, width of histograms, size of the chart, and set horizontal orientation
plt.figure(figsize=(10, 8))  # Change width and height of the chart
plt.hist(weight_data, bins=np.arange(50, 101, 0.5), color="#3498DB", orientation='horizontal', rwidth=0.9)
# Change band width, orientation, color code, and rwidth

# Change the topic, headline, and data type (weights distribution)
plt.title('Distribution of Weights in a Population')
plt.xlabel('Frequency')
plt.ylabel('Weight (kg)')
plt.grid(axis='x', linestyle='--')

# Display the histogram
plt.show()