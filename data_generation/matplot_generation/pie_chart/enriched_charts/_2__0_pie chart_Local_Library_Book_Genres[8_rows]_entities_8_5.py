
import matplotlib.pyplot as plt

# Data points
activities = [
    'Walking', 'Running', 'Yoga', 'Cycling', 'Swimming', 
    'Weightlifting', 'Pilates', 'Aerobics', 'Dancing', 'Hiking'
]

popularity = [
    30.2, 20.4, 15.8, 12.3, 8.5, 
    5.6, 3.4, 2.0, 1.1, 0.7
]

# Colors for each section
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#76d7c4', '#f4a582', '#e18d92'
]

# Resize the chart
plt.figure(figsize=(12, 7))

# Create the pie chart
plt.pie(popularity, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Health Activities in 2023', pad=20)

# Display the chart
plt.show()