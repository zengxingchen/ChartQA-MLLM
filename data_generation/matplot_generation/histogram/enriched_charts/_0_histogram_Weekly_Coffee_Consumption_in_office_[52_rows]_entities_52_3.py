
import matplotlib.pyplot as plt
import numpy as np

# Given data points (weights of fruit in grams)
data = [120, 121, 122, 119, 124, 125, 123, 122, 125, 124, 120, 122, 121,
        123, 124, 126, 128, 130, 129, 127, 125, 124, 122, 123, 121, 127,
        128, 130, 132, 133, 131, 129, 128, 126, 124, 123, 125, 127, 130,
        131, 133, 135, 134, 132, 131, 130, 129, 127, 125, 124, 122, 119,
        121, 120, 123, 125, 127, 128, 130, 132, 131, 134, 135, 136, 138,
        137, 139, 141, 140]

# Histogram properties
bin_width = 3
bins = np.arange(min(data), max(data) + bin_width, bin_width)

# Create figure and axis with specified size
fig, ax = plt.subplots(figsize=(8, 6))

# Create a horizontal histogram with specified properties
ax.hist(data, bins=bins, orientation='horizontal', color='#34a2eb', edgecolor='#2F4F4F', linewidth=1.5)

# Set title and labels
ax.set_title('Distribution of Fruit Weights')
ax.set_xlabel('Frequency')
ax.set_ylabel('Weight (grams)')

# Show the plot
plt.show()