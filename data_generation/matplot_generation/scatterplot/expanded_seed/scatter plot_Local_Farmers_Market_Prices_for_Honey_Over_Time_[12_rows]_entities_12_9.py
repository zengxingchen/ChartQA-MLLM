
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime

# Data
data = [
    {'Date': '2023-01-07', 'Price per Jar (USD)': 7.5},
    {'Date': '2023-01-14', 'Price per Jar (USD)': 7.55},
    {'Date': '2023-01-21', 'Price per Jar (USD)': 7.6},
    {'Date': '2023-01-28', 'Price per Jar (USD)': 7.65},
    {'Date': '2023-02-04', 'Price per Jar (USD)': 7.7},
    {'Date': '2023-02-11', 'Price per Jar (USD)': 7.75},
    {'Date': '2023-02-18', 'Price per Jar (USD)': 7.8},
    {'Date': '2023-02-25', 'Price per Jar (USD)': 7.85},
    {'Date': '2023-03-04', 'Price per Jar (USD)': 7.9},
    {'Date': '2023-03-11', 'Price per Jar (USD)': 7.95},
    {'Date': '2023-03-18', 'Price per Jar (USD)': 8.0},
    {'Date': '2023-03-25', 'Price per Jar (USD)': 8.05}
]

# Extracting the date and price information
dates = [datetime.datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
prices = [item['Price per Jar (USD)'] for item in data]
dates_numeric = date2num(dates)  # Convert dates to numeric values for plotting

# Generate a list of colors
colors = plt.cm.jet(prices/max(prices))

# Generate a list of markers
markers = ['o', 's', '^', 'D', 'v', '>', '<', 'p', '*', 'H', 'X', 'd']

plt.figure(figsize=(10, 5))

# Create a scatter plot with diversified visual encoding
for i, (date, price) in enumerate(zip(dates_numeric, prices)):
    plt.scatter(date, price, color=colors[i], marker=markers[i], s=100, label=f'{dates[i].date()} - ${price}')

# Beautify the plot
plt.title('Price per Jar Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)

# Auto-format the date on the x-axis
plt.gcf().autofmt_xdate()
date_format = mdates.DateFormatter('%Y-%m-%d')
plt.gca().xaxis.set_major_formatter(date_format)

# Add a color bar for better understanding of the color encoding
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=plt.Normalize(vmin=min(prices), vmax=max(prices)))
plt.colorbar(sm, label='Price (USD)')

# Show legend
plt.legend(loc='upper left', title='Date - Price', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# Show the plot
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()