
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
type_A = [20, 18, 25, 30, 22, 24, 20, 25, 23, 21, 24, 22, 26, 28]
type_B = [30, 28, 22, 20, 27, 29, 30, 25, 24, 26, 22, 24, 28, 24]
type_C = [25, 30, 30, 25, 31, 20, 28, 25, 28, 27, 29, 26, 20, 27]
type_D = [25, 24, 23, 25, 20, 27, 22, 25, 25, 26, 25, 28, 26, 21]

# Convert data to numpy arrays
type_A = np.array(type_A)
type_B = np.array(type_B)
type_C = np.array(type_C)
type_D = np.array(type_D)

# Stack data
data = np.vstack([type_A, type_B, type_C, type_D])

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F']

# Create stacked bar chart
width = 0.5
bars = ax.barh(categories, type_A, color=colors[0], edgecolor='black', height=width)
bars = ax.barh(categories, type_B, left=type_A, color=colors[1], edgecolor='black', height=width)
bars = ax.barh(categories, type_C, left=type_A + type_B, color=colors[2], edgecolor='black', height=width)
bars = ax.barh(categories, type_D, left=type_A + type_B + type_C, color=colors[3], edgecolor='black', height=width)

# Add labels
ax.set_xlabel('Percentage')
ax.set_title('Annual Distribution of Activity Types (2010-2023)')
ax.legend(['Type A', 'Type B', 'Type C', 'Type D'], loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()