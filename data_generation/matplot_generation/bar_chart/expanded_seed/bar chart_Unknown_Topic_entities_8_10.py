
import matplotlib.pyplot as plt

# Data
drinks = ['Americano', 'Latte', 'Cappuccino', 'Espresso', 'Mocha', 'Iced Coffee', 'Flat White', 'Chai Latte']
orders = [150, 200, 120, 80, 100, 170, 90, 60]

# Colors for each bar for diversification
colors = ['#FF0000', '#FFA500', '#FFFF00', '#008000', '#00FFFF', '#0000FF', '#800080', '#FFC0CB']

# Creating the bar chart
plt.figure(figsize=(10, 6))  # Setting the figure size
bars = plt.bar(drinks, orders, color=colors, edgecolor='black')  # Creating bars with edge color

# Add a title and labels
plt.title('Number of Orders for Different Types of Drinks', fontsize=15)
plt.xlabel('Drink Types', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the value on top of each bar for better readability
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=10)

# Display the legend (optional, this might not be needed as the bars are directly labeled)
# plt.legend(drinks, loc='best')

# Tight layout for fitting everything within the figure cleanly
plt.tight_layout()

# Show the plot
plt.show()