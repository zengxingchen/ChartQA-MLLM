
import matplotlib.pyplot as plt

# Table data provided
data = [
    {'Day': 'Monday', 'Espresso': 50, 'Americano': 75, 'Cappuccino': 100, 'Latte': 120, 'Mocha': 45},
    {'Day': 'Tuesday', 'Espresso': 60, 'Americano': 65, 'Cappuccino': 85, 'Latte': 110, 'Mocha': 50},
    {'Day': 'Wednesday', 'Espresso': 40, 'Americano': 80, 'Cappuccino': 70, 'Latte': 130, 'Mocha': 60},
    {'Day': 'Thursday', 'Espresso': 70, 'Americano': 90, 'Cappuccino': 120, 'Latte': 140, 'Mocha': 55},
    {'Day': 'Friday', 'Espresso': 80, 'Americano': 85, 'Cappuccino': 140, 'Latte': 160, 'Mocha': 65},
    {'Day': 'Saturday', 'Espresso': 90, 'Americano': 100, 'Cappuccino': 160, 'Latte': 200, 'Mocha': 70},
    {'Day': 'Sunday', 'Espresso': 85, 'Americano': 95, 'Cappuccino': 150, 'Latte': 190, 'Mocha': 60}
]

# Extracting data for plotting
days = [item['Day'] for item in data]
espresso_sales = [item['Espresso'] for item in data]
americano_sales = [item['Americano'] for item in data]
cappuccino_sales = [item['Cappuccino'] for item in data]
latte_sales = [item['Latte'] for item in data]
mocha_sales = [item['Mocha'] for item in data]

# Creating a line chart with a different line style and marker for each coffee type
plt.figure(figsize=(10, 6))
plt.plot(days, espresso_sales, label='Espresso', linestyle='-', marker='o')
plt.plot(days, americano_sales, label='Americano', linestyle='--', marker='s')
plt.plot(days, cappuccino_sales, label='Cappuccino', linestyle='-.', marker='^')
plt.plot(days, latte_sales, label='Latte', linestyle=':', marker='D')
plt.plot(days, mocha_sales, label='Mocha', linestyle='-', marker='*')

# Adding relevant titles and labels
plt.title('Coffee Sales Data')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Drinks Sold')
plt.legend()

# Customizing the grid
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Displaying the chart
plt.tight_layout()
plt.show()