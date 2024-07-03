
import matplotlib.pyplot as plt

# Data points
languages = [
    'Python', 'JavaScript', 'Java', 'C#', 'PHP', 
    'C++', 'R', 'Swift', 'Go', 'Ruby'
]

popularity = [
    25.9, 29.7, 17.6, 8.2, 6.0, 
    4.8, 3.2, 2.1, 1.3, 1.2
]

# Colors for each section
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Resize the chart
plt.figure(figsize=(10, 6))

# Create the pie chart
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Programming Languages in 2023')

# Display the chart
plt.show()