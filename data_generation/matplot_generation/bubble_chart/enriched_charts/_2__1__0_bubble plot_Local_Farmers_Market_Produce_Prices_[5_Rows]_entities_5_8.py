
import matplotlib.pyplot as plt

# Provided data for the chart
categories = ['Traveling', 'Reading', 'Watching TV', 'Social Media', 'Gaming']
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
hours = [
    [1.0, 1.2, 1.3, 1.1, 0.9, 0.8],  # Traveling
    [1.5, 1.6, 1.4, 1.3, 1.1, 1.0],  # Reading
    [2.5, 2.7, 2.8, 3.0, 3.2, 3.5],  # Watching TV
    [3.0, 2.8, 2.5, 2.3, 2.0, 1.5],  # Social Media
    [2.0, 1.8, 1.5, 1.2, 1.0, 0.7]   # Gaming
]

# Flatten the data for plotting
flat_age_groups = age_groups * len(categories)
flat_hours = [hour for sublist in hours for hour in sublist]
bubble_sizes = [size * 50 for size in flat_hours]

# Define colors for each category
colors = [
    '#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6', 
    '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', 
    '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F', 
    '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039', 
    '#900C3F', '#581845', '#DAF7A6', '#FFC300', '#FF5733', 
    '#C70039', '#900C3F', '#581845', '#DAF7A6', '#FFC300'
]

# Bubble chart
plt.figure(figsize=(14, 10))
plt.scatter(flat_age_groups, flat_hours, s=bubble_sizes, c=colors, alpha=0.6)

# Title and labels
plt.title('Average Hours Spent on Leisure Activities by Age Group', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')

# Show grid
plt.grid(True)

# Show the figure
plt.show()