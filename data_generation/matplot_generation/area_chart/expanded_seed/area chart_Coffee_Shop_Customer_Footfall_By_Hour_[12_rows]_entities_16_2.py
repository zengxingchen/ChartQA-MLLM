
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Your dataset
data = [
    {'Hour of Day': '6 AM', ' Customers': 50},
    {'Hour of Day': '7 AM', ' Customers': 75},
    {'Hour of Day': '8 AM', ' Customers': 110},
    {'Hour of Day': '9 AM', ' Customers': 90},
    {'Hour of Day': '10 AM', ' Customers': 70},
    {'Hour of Day': '11 AM', ' Customers': 80},
    {'Hour of Day': '12 PM', ' Customers': 150},
    {'Hour of Day': '1 PM', ' Customers': 180},
    {'Hour of Day': '2 PM', ' Customers': 165},
    {'Hour of Day': '3 PM', ' Customers': 155},
    {'Hour of Day': '4 PM', ' Customers': 140},
    {'Hour of Day': '5 PM', ' Customers': 130},
    {'Hour of Day': '6 PM', ' Customers': 120},
    {'Hour of Day': '7 PM', ' Customers': 105},
    {'Hour of Day': '8 PM', ' Customers': 85}
]

# Parsing the hour and customer count
hours = [datetime.strptime(d['Hour of Day'], '%I %p') for d in data]
customers = [d[' Customers'] for d in data]

# Plotting
plt.figure(figsize=(10, 6))

# Create an area chart
plt.fill_between(hours, customers, color="skyblue", alpha=0.4)
plt.plot(hours, customers, color="Slateblue", alpha=0.6)  # Line on top

# Formatting the x-axis with hour format
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))

# Labeling the axes and title
plt.xlabel('Hour of Day')
plt.ylabel('Number of Customers')
plt.title('Customer Visits by Hour')

# Grid, Legend, and tight_layout for better spacing
plt.grid(True)
plt.legend(['Customers'])
plt.tight_layout()

# Rotate x-axis labels for better readability
plt.gcf().autofmt_xdate()

# Show plot
plt.show()