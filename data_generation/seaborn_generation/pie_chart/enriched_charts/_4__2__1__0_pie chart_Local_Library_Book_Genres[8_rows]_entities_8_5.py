
import matplotlib.pyplot as plt

# Data points
activities = [
    'Reading', 'Writing', 'Gaming', 'Cooking', 'Traveling',
    'Sports', 'Watching TV', 'Music', 'Others'
]

percentages = [
    12.0, 8.0, 20.0, 18.0, 15.0,
    10.0, 7.0, 5.0, 5.0
]

# Colors for each section
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'
]

# Resize the chart
plt.figure(figsize=(12, 8))

# Create the pie chart
plt.pie(percentages, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Leisure Activities Distribution in 2023', fontsize=16, pad=20)

# Display the chart
plt.show()