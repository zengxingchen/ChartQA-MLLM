
import matplotlib.pyplot as plt
import numpy as np

# Data: Provided above as a list, representing the ages of a population group
ages = [
    23, 25, 29, 22, 24, 28, 35, 36, 37, 41, 23, 26, 23, 27, 28, 29, 30, 31, 21, 22,
    24, 25, 26, 27, 29, 33, 34, 35, 37, 38, 40, 42, 43, 45, 46, 21, 22, 23, 23, 24,
    25, 26, 28, 28, 29, 30, 31, 33, 34, 35, 37, 38, 40, 41, 43, 44, 45, 46, 47
]

# Settings for histogram
bins = range(20, 50, 2)  # Specify bin edges (age intervals of 2 years)

# Create histogram
plt.figure(figsize=(10, 6))  # Adjust the width and height of the chart
plt.hist(ages, bins=bins, orientation='horizontal', color='#3478f6', rwidth=0.9)  # Vertical to horizontal and width of histograms

# Customize chart
plt.xlabel('Frequency')  # Switched axis label due to orientation change
plt.ylabel('Age Group')
plt.title('Age Distribution of a Population Group')
plt.grid(axis='x')

# Show the plot
plt.show()