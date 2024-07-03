
import matplotlib.pyplot as plt

# Data points
topics = [
    'Artificial Intelligence', 'Blockchain Technology', 'Renewable Energy', 
    'Quantum Computing', 'Cybersecurity', 'Internet of Things', 
    '5G Networks', 'Augmented Reality', 'Nanotechnology', 'Biotechnology'
]

percentages = [
    25.0, 15.5, 12.0, 10.0, 9.5, 
    8.0, 6.5, 5.0, 4.0, 4.5
]

# Colors for each section
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Resize the chart
plt.figure(figsize=(10, 7))

# Create the pie chart
plt.pie(percentages, labels=topics, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Future Technologies in 2023', fontsize=14, pad=20)

# Display the chart
plt.show()