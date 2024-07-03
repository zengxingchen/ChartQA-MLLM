
import matplotlib.pyplot as plt
import squarify

# Data points
activity_items = [
    'Reading', 'Exercise', 'Socializing', 'Work', 'Meditation', 
    'Watching TV', 'Gaming', 'Traveling', 'Cooking', 
    'Shopping', 'Cleaning', 'Sleeping'
]
average_sleep_duration = [6.5, 7.0, 5.5, 6.0, 7.5, 5.0, 4.5, 6.8, 6.2, 5.8, 6.1, 8.0]
occurrence = [120, 95, 75, 110, 30, 60, 45, 50, 70, 65, 55, 150]

# Color scheme using specific color codes
colors = [
    '#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', 
    '#e67e22', '#1abc9c', '#34495e', '#d35400', '#7f8c8d',
    '#c0392b', '#2980b9'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(18, 14))

# Creating a treemap
squarify.plot(sizes=occurrence, label=activity_items, color=colors, alpha=0.8, value=average_sleep_duration, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Average Daily Sleep Duration for Various Activities', fontsize=20, color='darkblue')
plt.suptitle('Health & Psychology', fontsize=24)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()