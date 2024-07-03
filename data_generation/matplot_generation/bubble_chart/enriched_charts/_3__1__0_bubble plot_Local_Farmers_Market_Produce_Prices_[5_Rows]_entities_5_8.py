
import matplotlib.pyplot as plt

# Provided data for the chart
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
fruits = [2.5, 3.0, 3.2, 3.5, 3.8, 4.0]
vegetables = [3.0, 3.2, 3.5, 3.8, 4.0, 4.2]
proteins = [2.0, 2.3, 2.5, 2.7, 3.0, 3.2]
grains = [3.5, 3.8, 4.0, 4.2, 4.5, 4.8]
dairy = [1.5, 1.7, 1.8, 2.0, 2.2, 2.5]

# Bubble sizes, arbitrary values for visualization purposes
bubble_sizes = [size * 80 for size in fruits + vegetables + proteins + grains + dairy]

# Define colors for each food group
colors = [
    '#FF6347', '#FF4500', '#FFD700', '#ADFF2F', '#32CD32', '#98FB98', 
    '#8B0000', '#B22222', '#DC143C', '#FF8C00', '#FFA500', '#FFD700', 
    '#4B0082', '#6A5ACD', '#7B68EE', '#4682B4', '#5F9EA0', '#66CDAA', 
    '#20B2AA', '#2E8B57', '#3CB371', '#00FF7F', '#32CD32', '#9ACD32', 
    '#556B2F', '#6B8E23', '#7CFC00', '#7FFF00', '#ADFF2F', '#F0E68C'
]

# Bubble chart
plt.figure(figsize=(14, 10))
plt.scatter(age_groups * 5, fruits + vegetables + proteins + grains + dairy, s=bubble_sizes, c=colors, alpha=0.6)

# Title and labels
plt.title('Average Daily Intake of Different Food Groups by Age Group', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Average Intake (servings per day)')

# Show grid
plt.grid(True)

# Show the figure
plt.show()