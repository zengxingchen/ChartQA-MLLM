
import matplotlib.pyplot as plt
from datetime import datetime

# Data from the table
data = [
    {'Date': '2023-03-01', 'Eggs per dozen ($)': 3.5, 'Milk per gallon ($)': 2.5, 'Apples per lb ($)': 1.2, 'Carrots per lb ($)': 0.85},
    {'Date': '2023-03-08', 'Eggs per dozen ($)': 3.55, 'Milk per gallon ($)': 2.55, 'Apples per lb ($)': 1.25, 'Carrots per lb ($)': 0.8},
    {'Date': '2023-03-15', 'Eggs per dozen ($)': 3.6, 'Milk per gallon ($)': 2.6, 'Apples per lb ($)': 1.3, 'Carrots per lb ($)': 0.75},
    {'Date': '2023-03-22', 'Eggs per dozen ($)': 3.65, 'Milk per gallon ($)': 2.65, 'Apples per lb ($)': 1.35, 'Carrots per lb ($)': 0.7},
    {'Date': '2023-03-29', 'Eggs per dozen ($)': 3.7, 'Milk per gallon ($)': 2.7, 'Apples per lb ($)': 1.4, 'Carrots per lb ($)': 0.9},
    {'Date': '2023-04-05', 'Eggs per dozen ($)': 3.75, 'Milk per gallon ($)': 2.75, 'Apples per lb ($)': 1.45, 'Carrots per lb ($)': 0.95},
    {'Date': '2023-04-12', 'Eggs per dozen ($)': 3.8, 'Milk per gallon ($)': 2.8, 'Apples per lb ($)': 1.5, 'Carrots per lb ($)': 1.0},
    {'Date': '2023-04-19', 'Eggs per dozen ($)': 3.85, 'Milk per gallon ($)': 2.85, 'Apples per lb ($)': 1.55, 'Carrots per lb ($)': 1.05},
    {'Date': '2023-04-26', 'Eggs per dozen ($)': 3.9, 'Milk per gallon ($)': 2.9, 'Apples per lb ($)': 1.6, 'Carrots per lb ($)': 1.1}
]

# Parsing the dates from string to datetime objects
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]

# Extracting the individual price series
eggs_prices = [d['Eggs per dozen ($)'] for d in data]
milk_prices = [d['Milk per gallon ($)'] for d in data]
apples_prices = [d['Apples per lb ($)'] for d in data]
carrots_prices = [d['Carrots per lb ($)'] for d in data]

# Plotting each product with a different line style and marker
plt.figure(figsize=(10, 6))

plt.plot(dates, eggs_prices, color='blue', linestyle='-', marker='o', label='Eggs per dozen ($)')
plt.plot(dates, milk_prices, color='green', linestyle='--', marker='s', label='Milk per gallon ($)')
plt.plot(dates, apples_prices, color='red', linestyle='-.', marker='^', label='Apples per lb ($)')
plt.plot(dates, carrots_prices, color='orange', linestyle=':', marker='x', label='Carrots per lb ($)')

# Adding titles and labels
plt.title('Prices of Various Goods Over Time')
plt.xlabel('Date')
plt.ylabel('Price in USD')

# Format the x-axis to show the date in a readable format
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()  # Rotate date labels to fit

# Add legend and grid
plt.legend()
plt.grid(True)

# Save the plot as a file
plt.savefig('prices_over_time.png', format='png')

# Show the plot
plt.show()