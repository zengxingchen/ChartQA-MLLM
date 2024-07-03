
import matplotlib.pyplot as plt
import numpy as np

# Given data points
years = ['2018', '2019', '2020', '2021', '2022']
communication = [25, 22, 20, 18, 15]
development = [50, 55, 58, 60, 63]
project_management = [15, 13, 12, 12, 12]
design = [10, 10, 10, 10, 10]

# Convert the data to percentage
total = [sum(x) for x in zip(communication, development, project_management, design)]
communication_percentage = [i / j * 100 for i, j in zip(communication, total)]
development_percentage = [i / j * 100 for i, j in zip(development, total)]
project_management_percentage = [i / j * 100 for i, j in zip(project_management, total)]
design_percentage = [i / j * 100 for i, j in zip(design, total)]

# Set the figure size
plt.figure(figsize=(10, 8))

# Plot horizontal bar chart
barWidth = 0.85
plt.barh(years, communication_percentage, color='#1f77b4', edgecolor='white', height=barWidth, label='Communication')
plt.barh(years, development_percentage, left=communication_percentage, color='#ff7f0e', edgecolor='white', height=barWidth, label='Development')
plt.barh(years, project_management_percentage, left=[i+j for i,j in zip(communication_percentage, development_percentage)], color='#2ca02c', edgecolor='white', height=barWidth, label='Project Management')
plt.barh(years, design_percentage, left=[i+j+k for i,j,k in zip(communication_percentage, development_percentage, project_management_percentage)], color='#d62728', edgecolor='white', height=barWidth, label='Design')

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1, 1), title='Software Categories')

# Add labels and title
plt.xlabel('Percentage')
plt.title('Annual Software Usage in a Tech Company')

# Change xlim for better spacing
plt.xlim(0, 100)

# Display the plot
plt.show()