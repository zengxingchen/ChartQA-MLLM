
import matplotlib.pyplot as plt
from datetime import datetime

# Given table data
data = [
    {'Date': '2023-01-01', 'Espresso': 75, 'Brewed Coffee': 120, 'Tea': 45, 'Pastries': 80},
    {'Date': '2023-01-02', 'Espresso': 50, 'Brewed Coffee': 150, 'Tea': 60, 'Pastries': 90},
    {'Date': '2023-01-03', 'Espresso': 90, 'Brewed Coffee': 180, 'Tea': 40, 'Pastries': 85},
    {'Date': '2023-01-04', 'Espresso': 60, 'Brewed Coffee': 160, 'Tea': 55, 'Pastries': 75},
    {'Date': '2023-01-05', 'Espresso': 100, 'Brewed Coffee': 170, 'Tea': 50, 'Pastries': 90}
]

# Preparing the data for plotting
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
espresso = [d['Espresso'] for d in data]
brewed_coffee = [d['Brewed Coffee'] for d in data]
tea = [d['Tea'] for d in data]
pastries = [d['Pastries'] for d in data]

# Plotting the stacked bar chart
fig, ax = plt.subplots()

ax.bar(dates, espresso, label='Espresso', color='saddlebrown', edgecolor='black')
ax.bar(dates, brewed_coffee, bottom=espresso, label='Brewed Coffee', color='sienna', edgecolor='black')
ax.bar(dates, tea, bottom=[i+j for i,j in zip(espresso, brewed_coffee)], label='Tea', color='green', edgecolor='black')
ax.bar(dates, pastries, bottom=[i+j+k for i,j,k in zip(espresso, brewed_coffee, tea)], label='Pastries', color='burlywood', edgecolor='black')

# Formatting the dates on the x-axis
date_format = "%Y-%m-%d"
ax.xaxis_date()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: datetime.fromordinal(int(x)).strftime(date_format)))

# Adding the chart labels and title
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.title('Sales Data - Stacked Bar Chart')

# Adding a legend
plt.legend()

# Rotating the date labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()  # Adjust layout for a better fit
plt.show()