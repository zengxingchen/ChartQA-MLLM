
import matplotlib.pyplot as plt
from datetime import datetime

# Your provided data
data = [
    {'Date': '2023-03-01', 'Espresso': 55, 'Latte': 89, 'Americano': 45, 'Cappuccino': 60, 'Mocha': 30},
    {'Date': '2023-03-02', 'Espresso': 40, 'Latte': 95, 'Americano': 50, 'Cappuccino': 65, 'Mocha': 35},
    {'Date': '2023-03-03', 'Espresso': 60, 'Latte': 110, 'Americano': 40, 'Cappuccino': 70, 'Mocha': 45},
    {'Date': '2023-03-04', 'Espresso': 70, 'Latte': 120, 'Americano': 60, 'Cappuccino': 80, 'Mocha': 50},
    {'Date': '2023-03-05', 'Espresso': 65, 'Latte': 130, 'Americano': 55, 'Cappuccino': 75, 'Mocha': 40}
]

# Convert date strings to datetime objects for better x-axis formatting
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]

# Separate the coffee types into their own lists for plotting
espresso = [d['Espresso'] for d in data]
latte = [d['Latte'] for d in data]
americano = [d['Americano'] for d in data]
cappuccino = [d['Cappuccino'] for d in data]
mocha = [d['Mocha'] for d in data]

# We create a bottom for the "stack" by cumulatively summing the heights of the bars below
latte_bottom = espresso
americano_bottom = [i+j for i,j in zip(latte_bottom, latte)]
cappuccino_bottom = [i+j for i,j in zip(americano_bottom, americano)]
mocha_bottom = [i+j for i,j in zip(cappuccino_bottom, cappuccino)]

# Plot
fig, ax = plt.subplots()

ax.bar(dates, espresso, label='Espresso')
ax.bar(dates, latte, bottom=latte_bottom, label='Latte')
ax.bar(dates, americano, bottom=americano_bottom, label='Americano')
ax.bar(dates, cappuccino, bottom=cappuccino_bottom, label='Cappuccino')
ax.bar(dates, mocha, bottom=mocha_bottom, label='Mocha')

# Format the date on the x-axis
date_format = "%m/%d"
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: datetime.strftime(datetime.utcfromtimestamp(x), date_format)))

# Adding details
plt.title('Coffee Sales Data (Stacked Bar Chart)')
plt.xlabel('Date')
plt.ylabel('Number of Drinks Sold')
plt.xticks(rotation=45)  # Rotate dates for better visibility
plt.legend(title='Coffee Types')

# Display the resulting plot
plt.tight_layout()  # Adjust the plot to ensure there's enough space for the date labels
plt.show()