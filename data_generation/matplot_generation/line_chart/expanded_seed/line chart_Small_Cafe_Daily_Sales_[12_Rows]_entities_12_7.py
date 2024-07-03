
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Coffee': 70, 'Tea': 30, 'Pastries': 50, 'Sandwiches': 40},
    {'Date': '2023-03-02', 'Coffee': 65, 'Tea': 28, 'Pastries': 55, 'Sandwiches': 35},
    {'Date': '2023-03-03', 'Coffee': 80, 'Tea': 35, 'Pastries': 60, 'Sandwiches': 45},
    {'Date': '2023-03-04', 'Coffee': 75, 'Tea': 32, 'Pastries': 65, 'Sandwiches': 50},
    {'Date': '2023-03-05', 'Coffee': 85, 'Tea': 37, 'Pastries': 70, 'Sandwiches': 55},
    {'Date': '2023-03-06', 'Coffee': 90, 'Tea': 40, 'Pastries': 75, 'Sandwiches': 60},
    {'Date': '2023-03-07', 'Coffee': 95, 'Tea': 35, 'Pastries': 80, 'Sandwiches': 65},
    {'Date': '2023-03-08', 'Coffee': 100, 'Tea': 30, 'Pastries': 85, 'Sandwiches': 70},
    {'Date': '2023-03-09', 'Coffee': 110, 'Tea': 32, 'Pastries': 90, 'Sandwiches': 75},
    {'Date': '2023-03-10', 'Coffee': 105, 'Tea': 34, 'Pastries': 95, 'Sandwiches': 80},
    {'Date': '2023-03-11', 'Coffee': 115, 'Tea': 36, 'Pastries': 100, 'Sandwiches': 85},
    {'Date': '2023-03-12', 'Coffee': 120, 'Tea': 38, 'Pastries': 105, 'Sandwiches': 90}
]

# Prepare the data for plotting
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
coffee_sales = [d['Coffee'] for d in data]
tea_sales = [d['Tea'] for d in data]
pastries_sales = [d['Pastries'] for d in data]
sandwiches_sales = [d['Sandwiches'] for d in data]

# Start plotting
fig, ax = plt.subplots()

# Plot each line with a different style and marker
ax.plot(dates, coffee_sales, label='Coffee', color='brown', linestyle='-', marker='o')
ax.plot(dates, tea_sales, label='Tea', color='green', linestyle='--', marker='s')
ax.plot(dates, pastries_sales, label='Pastries', color='orange', linestyle='-.', marker='^')
ax.plot(dates, sandwiches_sales, label='Sandwiches', color='blue', linestyle=':', marker='x')

# Beautify the date labels
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()  # Rotation

# Add legend
ax.legend()

# Titles and labels
plt.title('Sales Data')
plt.xlabel('Date')
plt.ylabel('Items Sold')

# Show grid
plt.grid(True)

# Display the plot
plt.show()