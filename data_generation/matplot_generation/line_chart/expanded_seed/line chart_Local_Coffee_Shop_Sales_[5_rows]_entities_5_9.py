
import matplotlib.pyplot as plt
from datetime import datetime

# The provided data
data = [
    {'Date': '2023-01-01', 'Espresso': 75, 'Cappuccino': 135, 'Latte': 162},
    {'Date': '2023-01-02', 'Espresso': 57, 'Cappuccino': 123, 'Latte': 158},
    {'Date': '2023-01-03', 'Espresso': 89, 'Cappuccino': 145, 'Latte': 176},
    {'Date': '2023-01-04', 'Espresso': 64, 'Cappuccino': 132, 'Latte': 169},
    {'Date': '2023-01-05', 'Espresso': 80, 'Cappuccino': 140, 'Latte': 183}
]

# Parsing dates and separating the sales data for each coffee type
dates = [datetime.strptime(entry['Date'], '%Y-%m-%d') for entry in data]
espresso_sales = [entry['Espresso'] for entry in data]
cappuccino_sales = [entry['Cappuccino'] for entry in data]
latte_sales = [entry['Latte'] for entry in data]

# Creating the line chart
plt.figure(figsize=(10, 5))

# Plotting each coffee type sales with different styles
plt.plot(dates, espresso_sales, color='brown', linestyle='-', marker='o', label='Espresso')
plt.plot(dates, cappuccino_sales, color='darkorange', linestyle='--', marker='s', label='Cappuccino')
plt.plot(dates, latte_sales, color='saddlebrown', linestyle='-.', marker='^', label='Latte')

# Formatting the date axis
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator())

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Coffee Sales Data')

# Displaying the legend
plt.legend()

# Rotating date labels to avoid overlap
plt.xticks(rotation=45)

# Tightly layout to prevent clipping of labels
plt.tight_layout()

# Showing the plot
plt.show()