
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Sales': 350},
    {'Date': '2023-03-02', 'Sales': 445},
    {'Date': '2023-03-03', 'Sales': 475},
    {'Date': '2023-03-04', 'Sales': 520},
    {'Date': '2023-03-05', 'Sales': 600}
]

# Converting date strings to datetime objects
dates = [datetime.strptime(item['Date'], "%Y-%m-%d") for item in data]
sales = [item['Sales'] for item in data]

# Setting up the plot
plt.figure(figsize=(10, 6))

# Plotting the line chart
plt.plot(dates, sales, 
         color='purple',           # Line color
         linestyle='--',           # Line style
         linewidth=2,              # Line width
         marker='o',               # Marker style
         markersize=8,             # Marker size
         markerfacecolor='orange', # Marker face color
         markeredgewidth=2,        # Marker edge width
         markeredgecolor='blue')   # Marker edge color

# Formatting the dates on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Adding data labels
for date, sale in zip(dates, sales):
    plt.text(date, sale + 25, f'{sale}', ha='center', va='bottom')

# Adding title and labels
plt.title('Sales Data from 2023-03-01 to 2023-03-05')
plt.xlabel('Date')
plt.ylabel('Sales')

# Rotating the date labels for better visibility
plt.gcf().autofmt_xdate()

# Adding a grid for better readability
plt.grid(True)

# Show the plot
plt.show()