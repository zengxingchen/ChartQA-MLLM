
import matplotlib.pyplot as plt

# Provided data for the chart
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
sleeping = [7.5, 6.8, 6.5, 6.2, 6.0, 6.5]
working = [2.5, 3.0, 3.5, 4.0, 4.5, 4.2]
socializing = [1.2, 1.0, 0.9, 0.7, 0.6, 0.8]
relaxing = [1.8, 1.5, 1.3, 1.2, 1.0, 1.1]
exercising = [0.9, 1.1, 1.0, 0.8, 0.6, 0.4]

# Bubble sizes, arbitrary values for visualization purposes
bubble_sizes = [size * 80 for size in sleeping + working + socializing + relaxing + exercising]

# Define colors for each activity
colors = [
    # Sleeping color codes
    '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd', '#8c564b',
    # Working color codes
    '#ff9896', '#c49c94', '#f7b6d2', '#c5b0d5', '#c7c7c7', '#dbdb8d',
    # Socializing color codes
    '#bcbd22', '#17becf', '#9edae5', '#e377c2', '#7f7f7f', '#b5cf6b',
    # Relaxing color codes
    '#cedb9c', '#8c6d31', '#bd9e39', '#d6616b', '#6b486b', '#a05d56',
    # Exercising color codes
    '#d0743c', '#ff8c00', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Bubble chart
plt.figure(figsize=(12, 8))
plt.scatter(age_groups * 5, sleeping + working + socializing + relaxing + exercising, s=bubble_sizes, c=colors, alpha=0.6)

# Title and labels
plt.title('Average Sleep Hours per Day by Age Group and Activity', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')

# Show grid
plt.grid(True)

# Show the figure
plt.show()