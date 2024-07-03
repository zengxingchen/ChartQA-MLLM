
import matplotlib.pyplot as plt

# Data
genres = [
    "Action", "Adventure", "Strategy", "Simulation", "RPG", "Puzzle",
    "Sports", "Racing", "Fighting", "Platformer", "MMORPG", "FPS"
]
sales_millions = [125, 90, 45, 55, 130, 35, 75, 60, 50, 40, 100, 150]

# Creating vertical bar chart
fig, ax = plt.subplots(figsize=(14, 10))

ax.bar(genres, sales_millions, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e'
], width=0.6)

# Adding labels and title
ax.set_ylabel('Sales (millions)')
ax.set_title('Video Game Sales by Genre')

# Show the plot
plt.show()