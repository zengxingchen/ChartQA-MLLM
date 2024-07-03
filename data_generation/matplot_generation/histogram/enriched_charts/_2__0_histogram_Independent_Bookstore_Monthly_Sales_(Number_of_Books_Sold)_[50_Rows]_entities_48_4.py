
import matplotlib.pyplot as plt
import numpy as np

# Data: Provided above as a list, representing the ages of a population group
ages = [
    20, 21, 22, 22, 23, 23, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 28, 
    28, 28, 29, 29, 30, 30, 31, 31, 31, 32, 32, 33, 34, 34, 34, 35, 35, 36, 36, 37, 
    37, 38, 38, 38, 39, 40, 40, 41, 41, 42, 43, 43, 44, 45, 45, 46, 47
]

# Settings for histogram
bins = range(20, 50, 2)  # Specify bin edges (age intervals of 2 years)

# Create histogram
plt.figure(figsize=(8, 12))  # Adjust the width and height of the chart
plt.hist(ages, bins=bins, orientation='vertical', color='#FF5733', rwidth=0.8)  # Vertical to horizontal and width of histograms

# Customize chart
plt.xlabel('Age Group')  # Switched axis label due to orientation change
plt.ylabel('Frequency')
plt.title('Age Distribution in a Sample Population')
plt.grid(axis='y')

# Show the plot
plt.show()