
import matplotlib.pyplot as plt

# Data for the pie chart
languages = ['Python', 'JavaScript', 'Java', 'C#', 'PHP', 'Ruby', 'Swift', 'Kotlin', 'Rust']
popularity = [29.7, 19.5, 16.5, 14.2, 8.6, 3.9, 2.9, 2.7, 2.0]

# Colors for each section of the pie chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']

# Create a pie chart
plt.figure(figsize=(10, 8))  # Modify the size of the chart
plt.pie(popularity, labels=languages, colors=colors, startangle=90, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Programming Language Popularity in 2023')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()