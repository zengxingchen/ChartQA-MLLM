
import matplotlib.pyplot as plt

# Data points
categories = [
    'Space Travel', 'Mars Exploration', 'Astrophysics', 'Black Holes', 'Exoplanets', 
    'Cosmology', 'Astronomy Research', 'Space Telescopes', 'Astrobiology', 'Dark Matter'
]

popularity = [
    22.0, 17.5, 15.3, 11.0, 9.5, 
    8.0, 7.2, 5.8, 3.2, 0.5
]

# Colors for each section
colors = [
    '#FF6347', '#FFD700', '#1E90FF', '#8A2BE2', '#00CED1',
    '#FF69B4', '#BA55D3', '#CD5C5C', '#7FFF00', '#FF4500'
]

# Resize the chart
plt.figure(figsize=(14, 9))

# Create the pie chart
plt.pie(popularity, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Astronomy & Space Exploration Topics in 2023', fontsize=16, pad=25)

# Display the chart
plt.show()