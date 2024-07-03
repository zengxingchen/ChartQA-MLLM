
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-01-01', 'Number of Coffees Sold': 150, 'Size of Cups (oz)': 12, 'Average Temperature (°F)': 35},
    {'Date': '2023-01-02', 'Number of Coffees Sold': 165, 'Size of Cups (oz)': 12, 'Average Temperature (°F)': 33},
    {'Date': '2023-01-03', 'Number of Coffees Sold': 180, 'Size of Cups (oz)': 16, 'Average Temperature (°F)': 38},
    {'Date': '2023-01-04', 'Number of Coffees Sold': 200, 'Size of Cups (oz)': 16, 'Average Temperature (°F)': 40},
    {'Date': '2023-01-05', 'Number of Coffees Sold': 190, 'Size of Cups (oz)': 12, 'Average Temperature (°F)': 45},
    {'Date': '2023-01-06', 'Number of Coffees Sold': 210, 'Size of Cups (oz)': 12, 'Average Temperature (°F)': 50},
    {'Date': '2023-01-07', 'Number of Coffees Sold': 205, 'Size of Cups (oz)': 16, 'Average Temperature (°F)': 52},
    {'Date': '2023-01-08', 'Number of Coffees Sold': 220, 'Size of Cups (oz)': 16, 'Average Temperature (°F)': 49},
    {'Date': '2023-01-09', 'Number of Coffees Sold': 230, 'Size of Cups (oz)': 16, 'Average Temperature (°F)': 51}
]

# Extracting information from the data
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
sales = [d['Number of Coffees Sold'] for d in data]
temperatures = [d['Average Temperature (°F)'] for d in data]
cup_sizes = [d['Size of Cups (oz)'] for d in data]

# Normalizing the temperature for bubble size (the 10 is arbitrary for scaling purposes)
bubble_sizes = [temp * 10 for temp in temperatures]

# Choosing a color based on cup size
colors = ['#1f77b4' if size == 12 else '#ff7f0e' for size in cup_sizes]

# Create the bubble chart
plt.figure(figsize=(10, 6))

scatter = plt.scatter(dates, sales, s=bubble_sizes, c=colors, alpha=0.5)

# Create a date formatter and format the x-axis to show month and day
date_format = mdates.DateFormatter('%m-%d')
plt.gca().xaxis.set_major_formatter(date_format)

# Adding labels and title
plt.title('Number of Coffees Sold per Day (Bubble Size: Avg Temp, Color: Cup Size)')
plt.xlabel('Date')
plt.ylabel('Number of Coffees Sold')

# Adding a legend for cup sizes - we will use a dummy scatter as handles
legend1 = plt.legend(*scatter.legend_elements(prop="sizes", alpha=0.6), loc="upper left", title="Temperatures (°F)")
legend2 = plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='12 oz', markerfacecolor='#1f77b4', markersize=10),
                              plt.Line2D([0], [0], marker='o', color='w', label='16 oz', markerfacecolor='#ff7f0e', markersize=10)],
                   title="Cup Sizes", loc="lower left")
plt.gca().add_artist(legend1)  # Need to manually add this back in after the second legend

# Show the plot
plt.show()