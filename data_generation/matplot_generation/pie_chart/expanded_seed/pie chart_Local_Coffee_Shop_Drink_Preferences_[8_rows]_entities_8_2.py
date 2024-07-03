
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Drink Type': 'Espresso', 'Number of Cups Sold': 150},
    {'Drink Type': 'Americano', 'Number of Cups Sold': 120},
    {'Drink Type': 'Latte', 'Number of Cups Sold': 200},
    {'Drink Type': 'Cappuccino', 'Number of Cups Sold': 180},
    {'Drink Type': 'Iced Coffee', 'Number of Cups Sold': 100},
    {'Drink Type': 'Mocha', 'Number of Cups Sold': 90},
    {'Drink Type': 'Tea', 'Number of Cups Sold': 60},
    {'Drink Type': 'Hot Chocolate', 'Number of Cups Sold': 50}
]

# Extracting the names of the drinks and the number of cups sold
drink_types = [item['Drink Type'] for item in data]
cups_sold = [item['Number of Cups Sold'] for item in data]

# Colors for the pie chart (one color for each drink type)
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#f7e1a0']

# Explode the slice with the most cups sold (in this case, Latte)
explode = [0.1 if drink == 'Latte' else 0 for drink in drink_types]

# Plotting the pie chart
plt.figure(figsize=(10,7))
plt.pie(cups_sold, explode=explode, labels=drink_types, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Number of Coffee Drinks Sold')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Display the pie chart
plt.show()