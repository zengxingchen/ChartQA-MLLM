
import matplotlib.pyplot as plt
from datetime import datetime

# Provided data
data = [
    {'Date': '2023-03-01', 'Espresso': 250, 'Brewed Coffee': 150, 'Tea': 100, 'Pastries': 75},
    {'Date': '2023-03-02', 'Espresso': 200, 'Brewed Coffee': 180, 'Tea': 120, 'Pastries': 90},
    {'Date': '2023-03-03', 'Espresso': 300, 'Brewed Coffee': 190, 'Tea': 80, 'Pastries': 110},
    {'Date': '2023-03-04', 'Espresso': 220, 'Brewed Coffee': 220, 'Tea': 150, 'Pastries': 60},
    {'Date': '2023-03-05', 'Espresso': 280, 'Brewed Coffee': 170, 'Tea': 90, 'Pastries': 130}
]

# Parsing the data
dates = [datetime.strptime(d['Date'], "%Y-%m-%d") for d in data]
espressos = [d['Espresso'] for d in data]
brewed_coffees = [d['Brewed Coffee'] for d in data]
teas = [d['Tea'] for d in data]
pastries = [d['Pastries'] for d in data]

# Plot configuration
fig, ax = plt.subplots()
bar_width = 0.5
ind = range(len(dates))

# Creating stacked bar chart
p1 = ax.bar(ind, espressos, bar_width, label='Espresso')
p2 = ax.bar(ind, brewed_coffees, bar_width, bottom=espressos, label='Brewed Coffee')
p3 = ax.bar(ind, teas, bar_width, bottom=[i+j for i,j in zip(espressos, brewed_coffees)], label='Tea')
p4 = ax.bar(ind, pastries, bar_width, bottom=[i+j+k for i,j,k in zip(espressos, brewed_coffees, teas)], label='Pastries')

# Customizing the axes and layout
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.set_title('Sales Data for Coffee Shop')
ax.set_xticks(ind)
# Convert dates to the format to display in the chart
ax.set_xticklabels([date.strftime("%m-%d") for date in dates], rotation=45)
ax.legend()

# Display the figure
plt.tight_layout()
plt.show()