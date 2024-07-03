
import matplotlib.pyplot as plt
import numpy as np

# Data: Provided above as a list, representing the ages of a population group
ages = [
    21, 21, 22, 22, 22, 23, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 26, 
    27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 30, 30, 31, 31, 33, 33, 34, 34, 
    35, 35, 35, 36, 37, 37, 37, 38, 38, 40, 40, 41, 41, 42, 43, 43, 44, 45, 45, 
    46, 46, 47, 50, 52, 53, 54, 56, 58, 60, 61, 63, 65
]

# Settings for histogram
bins = range(20, 70, 3)  # Specify bin edges (age intervals of 3 years)

# Create histogram
plt.figure(figsize=(8, 12))  # Adjust the width and height of the chart
plt.hist(ages, bins=bins, color='#1f77b4', rwidth=0.8)  # Vertical histogram and width of histograms

# Customize chart
plt.xlabel('Age Group')  # Axis label for age groups
plt.ylabel('Frequency')  # Axis label for frequency
plt.title('Age Distribution in Sports & Fitness')  # Title of the chart
plt.grid(axis='y')

# Show the plot
plt.show()