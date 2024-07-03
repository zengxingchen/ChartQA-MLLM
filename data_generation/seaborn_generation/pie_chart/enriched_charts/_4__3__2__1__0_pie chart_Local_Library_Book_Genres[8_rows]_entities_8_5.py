
import matplotlib.pyplot as plt

# Data points
sports = [
    'Running', 'Cycling', 'Swimming', 'Yoga', 
    'Gym Workouts', 'Basketball', 'Soccer', 
    'Tennis', 'Others'
]

percentages = [
    22.5, 18.0, 15.0, 12.5, 
    10.0, 7.5, 6.0, 5.5, 3.0
]

# Colors for each section
colors = [
    '#ff4500', '#4682b4', '#32cd32', '#ffd700', 
    '#dda0dd', '#ff6347', '#4169e1', '#ff69b4', '#8a2be2'
]

# Resize the chart
plt.figure(figsize=(10, 7))

# Create the pie chart
plt.pie(percentages, labels=sports, colors=colors, autopct='%1.1f%%', startangle=90)

# Set the title
plt.title('Sports & Fitness: Participation in Different Sports Activities in 2023', fontsize=16, pad=20)

# Display the chart
plt.show()