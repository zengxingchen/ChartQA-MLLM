
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Define the data
data = [
    {'Date': '2023-03-01', 'Station 1 Usage (kWh)': 73, 'Station 2 Usage (kWh)': 65, 'Station 3 Usage (kWh)': 59},
    {'Date': '2023-03-02', 'Station 1 Usage (kWh)': 68, 'Station 2 Usage (kWh)': 72, 'Station 3 Usage (kWh)': 49},
    # ... (Include all data points)
    {'Date': '2023-03-15', 'Station 1 Usage (kWh)': 110, 'Station 2 Usage (kWh)': 106, 'Station 3 Usage (kWh)': 100}
]

# Parse date and extract usage data for each station
dates = [datetime.strptime(entry['Date'], '%Y-%m-%d') for entry in data]
station1_usage = [entry['Station 1 Usage (kWh)'] for entry in data]
station2_usage = [entry['Station 2 Usage (kWh)'] for entry in data]
station3_usage = [entry['Station 3 Usage (kWh)'] for entry in data]

# Create scatter plot
fig, ax = plt.subplots()

# Plot for Station 1
ax.scatter(dates, station1_usage, color='blue', marker='o', label='Station 1 Usage')
# Plot for Station 2
ax.scatter(dates, station2_usage, color='red', marker='^', label='Station 2 Usage')
# Plot for Station 3
ax.scatter(dates, station3_usage, color='green', marker='s', label='Station 3 Usage')

# Format the x-axis to show the date format nicely
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()  # Rotation

# Annotation for data points
for i, date in enumerate(dates):
    ax.annotate(str(station1_usage[i]), (mdates.date2num(date), station1_usage[i]), textcoords="offset points", xytext=(0,5), ha='center')
    ax.annotate(str(station2_usage[i]), (mdates.date2num(date), station2_usage[i]), textcoords="offset points", xytext=(0,5), ha='center')
    ax.annotate(str(station3_usage[i]), (mdates.date2num(date), station3_usage[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Title and labels
plt.title('Daily Usage of Three Stations (kWh)')
plt.xlabel('Date')
plt.ylabel('Usage (kWh)')

# Enable legend
plt.legend()

# Show the plot
plt.show()