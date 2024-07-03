
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data
data = [
    {'Date': '2023-03-01', 'Sales (USD)': 1570},
    {'Date': '2023-03-02', 'Sales (USD)': 1830},
    {'Date': '2023-03-03', 'Sales (USD)': 1410},
    {'Date': '2023-03-04', 'Sales (USD)': 1675}
]

# Parsing dates and sales
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
sales = [d['Sales (USD)'] for d in data]

# Creating the area chart
plt.fill_between(dates, sales, color="skyblue", alpha=0.4)

# Customizing the axes
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Annotations for each data point
for i, (date, sale) in enumerate(zip(dates, sales)):
    plt.text(date, sale, f'${sale}', ha='center', va='bottom')

# Title and labels
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales (USD)')

# Beautify the x-axis (rotation & formatting)
plt.gcf().autofmt_xdate()
plt.xticks(dates, [date.strftime('%Y-%m-%d') for date in dates], rotation=45)

# Show grid
plt.grid(True)

# Show the plot
plt.tight_layout() # This adjusts subplot params so that the subplot(s) fits in to the figure area.
plt.show()