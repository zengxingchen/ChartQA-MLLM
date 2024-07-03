
import matplotlib.pyplot as plt

# Provided data for the chart
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
meditation = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
walking = [1.2, 1.1, 1.0, 0.9, 0.8, 0.7]
cooking = [0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
gardening = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3]

# Bubble sizes, arbitrary values for visualization purposes
bubble_sizes = [size * 80 for size in meditation + walking + cooking + gardening]

# Define colors for each activity
colors = [
    '#FF6347', '#FF4500', '#FF6347', '#FF4500', '#FF6347', '#FF4500',
    '#4682B4', '#4169E1', '#4682B4', '#4169E1', '#4682B4', '#4169E1',
    '#32CD32', '#3CB371', '#32CD32', '#3CB371', '#32CD32', '#3CB371',
    '#8A2BE2', '#9400D3', '#8A2BE2', '#9400D3', '#8A2BE2', '#9400D3'
]

# Bubble chart
plt.figure(figsize=(14, 8))
plt.scatter(age_groups * 4, meditation + walking + cooking + gardening, s=bubble_sizes, c=colors, alpha=0.6)

# Title and labels
plt.title('Daily Leisure Activities by Age Group', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')

# Show grid
plt.grid(True)

# Show the figure
plt.show()