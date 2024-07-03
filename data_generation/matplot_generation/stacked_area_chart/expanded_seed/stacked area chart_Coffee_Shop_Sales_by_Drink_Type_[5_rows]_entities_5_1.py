
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Espresso': 150, 'Latte': 200, 'Cappuccino': 130, 'Americano': 120},
    {'Date': '2023-03-02', 'Espresso': 165, 'Latte': 210, 'Cappuccino': 135, 'Americano': 115},
    {'Date': '2023-03-03', 'Espresso': 170, 'Latte': 190, 'Cappuccino': 140, 'Americano': 130},
    {'Date': '2023-03-04', 'Espresso': 180, 'Latte': 220, 'Cappuccino': 150, 'Americano': 140},
    {'Date': '2023-03-05', 'Espresso': 160, 'Latte': 230, 'Cappuccino': 160, 'Americano': 135}
]

# Parsing dates and sales data
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
espresso_sales = [d['Espresso'] for d in data]
latte_sales = [d['Latte'] for d in data]
cappuccino_sales = [d['Cappuccino'] for d in data]
americano_sales = [d['Americano'] for d in data]

# Plotting the stacked area chart
plt.figure(figsize=(10, 7))

# Diversified color encoding
colors = ['#6b5b95', '#feb236', '#d64161', '#ff7b25']

plt.stackplot(dates, espresso_sales, latte_sales, cappuccino_sales, americano_sales, labels=['Espresso', 'Latte', 'Cappuccino', 'Americano'], colors=colors, alpha=0.5)

# Formatting the dates on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Adding chart title and labels
plt.title('Coffee Sales Data (Stacked Area Chart)')
plt.xlabel('Date')
plt.ylabel('Number of Drinks Sold')

# Adding the legend
plt.legend(loc='upper left')

# Rotating date labels for better visibility
plt.xticks(rotation=45)

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()