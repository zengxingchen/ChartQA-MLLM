
import matplotlib.pyplot as plt

# Data
categories = ['Artificial Intelligence', 'Quantum Computing', 'Blockchain', 'Augmented Reality', '5G Technology', 'Nanotechnology']
percentages = [32.1, 22.4, 18.7, 12.9, 9.6, 4.3]
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#3CB371', '#FF8C00', '#C71585']

# Create a pie chart
plt.figure(figsize=(12, 8))
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Popularity of Emerging Technologies in 2023', y=1.05)

# Display the chart
plt.show()