
import matplotlib.pyplot as plt

# Data from the provided table
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales = [650, 700, 800, 850, 950, 1100, 900]

# Create an area chart
plt.fill_between(days, sales, color="skyblue", alpha=0.4)
plt.plot(days, sales, color="Slateblue", alpha=0.6, linewidth=2)

# Add titles and labels
plt.title('Sales ($) throughout the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Sales ($)')

# Customize the grid
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Add a marker for each data point
plt.scatter(days, sales, color='blue', alpha=0.8, zorder=3)

# Annotate each data point on the graph
for i in range(len(days)):
    plt.text(days[i], sales[i]*1.01, f"${sales[i]}", ha='center', va='bottom')

# Show the plot
plt.show()