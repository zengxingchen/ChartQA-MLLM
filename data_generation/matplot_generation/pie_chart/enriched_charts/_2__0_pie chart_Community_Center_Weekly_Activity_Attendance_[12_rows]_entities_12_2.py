
import matplotlib.pyplot as plt

# Data setup
destinations = ['France', 'Spain', 'Italy', 'USA', 'China', 'Australia', 'Japan', 'Brazil', 'Canada', 'Thailand', 'Mexico', 'India']
percentages = [20, 15, 12, 10, 8, 7, 6, 5, 5, 4, 3, 3]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ff6666', '#c4e17f', '#d3b6c6', '#ffcccb', '#c0d6e4']

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))  # width and height of the chart
ax.pie(percentages, labels=destinations, autopct='%1.1f%%', colors=colors, startangle=140)
ax.set_title('Popular Travel Destinations by Visitor Percentage', pad=20)

# Show plot
plt.show()