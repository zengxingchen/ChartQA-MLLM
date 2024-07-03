
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data preparation
data = [
    {'Hour': '10 AM', 'Visitors': 42}, 
    {'Hour': '11 AM', 'Visitors': 58}, 
    {'Hour': '12 PM', 'Visitors': 67},
    {'Hour': '1 PM', 'Visitors': 73}, 
    {'Hour': '2 PM', 'Visitors': 65}, 
    {'Hour': '3 PM', 'Visitors': 59},
    {'Hour': '4 PM', 'Visitors': 48}, 
    {'Hour': '5 PM', 'Visitors': 35}
]

# Convert hour strings to datetime objects for better handling in the plot
hours = [datetime.strptime(entry['Hour'], '%I %p') for entry in data]
visitors = [entry['Visitors'] for entry in data]

# Create figure and plot
fig, ax = plt.subplots()

# Plotting the area chart
plt.fill_between(hours, visitors, color='skyblue', alpha=0.4)
plt.plot(hours, visitors, color='Slateblue', alpha=0.6, linewidth=2)

# Beautify the x-labels (Date formatting)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator())

# Setting the labels and title
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Visitors')
plt.title('Area Chart of Visitors by Hour')

# Rotate date labels for better readability
plt.gcf().autofmt_xdate()

# Show a grid
plt.grid(True)

# Show the plot
plt.show()