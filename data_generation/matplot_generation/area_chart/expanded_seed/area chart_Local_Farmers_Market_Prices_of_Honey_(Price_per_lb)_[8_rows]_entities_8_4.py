
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data from the given table
data = [
    {'Week': '2023-04-01 to 2023-04-07', 'Price_USD': 7.5},
    {'Week': '2023-04-08 to 2023-04-14', 'Price_USD': 7.8},
    {'Week': '2023-04-15 to 2023-04-21', 'Price_USD': 8.0},
    {'Week': '2023-04-22 to 2023-04-28', 'Price_USD': 7.3},
    {'Week': '2023-04-29 to 2023-05-05', 'Price_USD': 7.7},
    {'Week': '2023-05-06 to 2023-05-12', 'Price_USD': 7.9},
    {'Week': '2023-05-13 to 2023-05-19', 'Price_USD': 7.6},
    {'Week': '2023-05-20 to 2023-05-26', 'Price_USD': 8.1}
]

# Extracting the mid-point of the week for plotting on the x-axis
week_dates = [(datetime.strptime(week['Week'][:10], '%Y-%m-%d') + 
               (datetime.strptime(week['Week'][-10:], '%Y-%m-%d') -
                datetime.strptime(week['Week'][:10], '%Y-%m-%d')) / 2).date()
              for week in data]

# Extracting the price values for the y-axis
prices = [week['Price_USD'] for week in data]

# Creating the area chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the data
ax.fill_between(week_dates, prices, color="skyblue", alpha=0.4)
ax.plot(week_dates, prices, color="Slateblue", alpha=0.6, linewidth=2)

# Customizing the date format on the x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Adding grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Adding labels and title
ax.set_xlabel('Week', fontsize=14, labelpad=10)
ax.set_ylabel('Price (USD)', fontsize=14, labelpad=10)
ax.set_title('Weekly Price Trend for Product', fontsize=16, pad=20)

# Rotating date labels for clarity
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

# Show the plot
plt.tight_layout()
plt.show()