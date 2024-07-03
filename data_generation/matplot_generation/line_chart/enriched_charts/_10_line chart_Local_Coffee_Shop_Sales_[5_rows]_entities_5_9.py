
import matplotlib.pyplot as plt
from datetime import datetime

# The provided data
data = [
    {'Date': '2023-01-01', 'Quantum Computing': 120, 'Artificial Intelligence': 80, 'Blockchain': 150},
    {'Date': '2023-01-02', 'Quantum Computing': 110, 'Artificial Intelligence': 85, 'Blockchain': 155},
    {'Date': '2023-01-03', 'Quantum Computing': 115, 'Artificial Intelligence': 90, 'Blockchain': 145},
    {'Date': '2023-01-04', 'Quantum Computing': 130, 'Artificial Intelligence': 95, 'Blockchain': 140},
    {'Date': '2023-01-05', 'Quantum Computing': 125, 'Artificial Intelligence': 100, 'Blockchain': 160},
    {'Date': '2023-01-06', 'Quantum Computing': 135, 'Artificial Intelligence': 105, 'Blockchain': 165},
    {'Date': '2023-01-07', 'Quantum Computing': 140, 'Artificial Intelligence': 110, 'Blockchain': 170},
    {'Date': '2023-01-08', 'Quantum Computing': 145, 'Artificial Intelligence': 115, 'Blockchain': 175},
    {'Date': '2023-01-09', 'Quantum Computing': 150, 'Artificial Intelligence': 120, 'Blockchain': 180},
    {'Date': '2023-01-10', 'Quantum Computing': 160, 'Artificial Intelligence': 125, 'Blockchain': 185},
    {'Date': '2023-01-11', 'Quantum Computing': 155, 'Artificial Intelligence': 130, 'Blockchain': 190},
    {'Date': '2023-01-12', 'Quantum Computing': 165, 'Artificial Intelligence': 135, 'Blockchain': 195},
    {'Date': '2023-01-13', 'Quantum Computing': 170, 'Artificial Intelligence': 140, 'Blockchain': 200},
    {'Date': '2023-01-14', 'Quantum Computing': 175, 'Artificial Intelligence': 145, 'Blockchain': 205},
    {'Date': '2023-01-15', 'Quantum Computing': 180, 'Artificial Intelligence': 150, 'Blockchain': 210},
]

# Parsing dates and separating the sales data for each technology trend
dates = [datetime.strptime(entry['Date'], '%Y-%m-%d') for entry in data]
quantum_sales = [entry['Quantum Computing'] for entry in data]
ai_sales = [entry['Artificial Intelligence'] for entry in data]
blockchain_sales = [entry['Blockchain'] for entry in data]

# Creating the line chart
plt.figure(figsize=(12, 6))

# Plotting each technology trend with different styles and colors
plt.plot(dates, quantum_sales, color='#FF5733', linestyle='-', marker='o', label='Quantum Computing')
plt.plot(dates, ai_sales, color='#33FF57', linestyle='--', marker='s', label='Artificial Intelligence')
plt.plot(dates, blockchain_sales, color='#3357FF', linestyle='-.', marker='^', label='Blockchain')

# Formatting the date axis
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator())

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Popularity Index')
plt.title('Trends in Future Technologies')

# Displaying the legend
plt.legend()

# Rotating date labels to avoid overlap
plt.xticks(rotation=45)

# Adding annotations for specific data points
plt.annotate('AI peak start', xy=(dates[10], ai_sales[10]), xytext=(dates[10], ai_sales[10]+10),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Tightly layout to prevent clipping of labels
plt.tight_layout()

# Showing the plot
plt.show()