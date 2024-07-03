
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data
data = [
    {'Date': '2023-01-01', 'Espresso': 200, 'Brewed Coffee': 180, 'Tea': 70, 'Pastries': 130},
    {'Date': '2023-01-02', 'Espresso': 190, 'Brewed Coffee': 192, 'Tea': 65, 'Pastries': 120},
    {'Date': '2023-01-03', 'Espresso': 210, 'Brewed Coffee': 185, 'Tea': 75, 'Pastries': 140},
    {'Date': '2023-01-04', 'Espresso': 205, 'Brewed Coffee': 200, 'Tea': 80, 'Pastries': 130},
    {'Date': '2023-01-05', 'Espresso': 220, 'Brewed Coffee': 204, 'Tea': 85, 'Pastries': 135}
]

# Preparation of data
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
espresso = [d['Espresso'] for d in data]
brewed_coffee = [d['Brewed Coffee'] for d in data]
tea = [d['Tea'] for d in data]
pastries = [d['Pastries'] for d in data]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(dates, espresso, brewed_coffee, tea, pastries, labels=['Espresso', 'Brewed Coffee', 'Tea', 'Pastries'], alpha=0.6)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # Set major locator to daily interval
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) # Set the display format for dates

# Diversified visual encoding
plt.xticks(rotation=45) # Rotate date labels for better readability
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Daily Sales Data Stack Area Chart')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(loc='upper left')

# To ensure all date labels are shown
fig.autofmt_xdate()

plt.tight_layout()
plt.show()