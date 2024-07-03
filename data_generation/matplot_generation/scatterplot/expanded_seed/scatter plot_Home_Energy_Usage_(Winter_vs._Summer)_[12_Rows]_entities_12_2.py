
import matplotlib.pyplot as plt

# Data
data = [
    {'Month': 'January', 'Winter Energy Consumption (kWh)': 450, 'Summer Energy Consumption (kWh)': 0},
    {'Month': 'February', 'Winter Energy Consumption (kWh)': 430, 'Summer Energy Consumption (kWh)': 0},
    {'Month': 'March', 'Winter Energy Consumption (kWh)': 350, 'Summer Energy Consumption (kWh)': 0},
    {'Month': 'April', 'Winter Energy Consumption (kWh)': 250, 'Summer Energy Consumption (kWh)': 100},
    {'Month': 'May', 'Winter Energy Consumption (kWh)': 0, 'Summer Energy Consumption (kWh)': 150},
    {'Month': 'June', 'Winter Energy Consumption (kWh)': 0, 'Summer Energy Consumption (kWh)': 300},
    {'Month': 'July', 'Winter Energy Consumption (kWh)': 0, 'Summer Energy Consumption (kWh)': 320},
    {'Month': 'August', 'Winter Energy Consumption (kWh)': 0, 'Summer Energy Consumption (kWh)': 310},
    {'Month': 'September', 'Winter Energy Consumption (kWh)': 0, 'Summer Energy Consumption (kWh)': 200},
    {'Month': 'October', 'Winter Energy Consumption (kWh)': 200, 'Summer Energy Consumption (kWh)': 50},
    {'Month': 'November', 'Winter Energy Consumption (kWh)': 320, 'Summer Energy Consumption (kWh)': 0},
    {'Month': 'December', 'Winter Energy Consumption (kWh)': 410, 'Summer Energy Consumption (kWh)': 0}
]

# Separate the data into usable lists
months = [d['Month'] for d in data]
winter_consumption = [d['Winter Energy Consumption (kWh)'] for d in data]
summer_consumption = [d['Summer Energy Consumption (kWh)'] for d in data]

# Create scatterplot
plt.figure(figsize=(10, 6))

# Plot Winter Energy Consumption
for i, month in enumerate(months):
    plt.scatter(i, winter_consumption[i], color='blue', marker='o', label="Winter" if i == 0 else "")
    plt.text(i, winter_consumption[i], month, fontsize=9, ha='center')

# Plot Summer Energy Consumption
for i, month in enumerate(months):
    plt.scatter(i, summer_consumption[i], color='red', marker='x', label="Summer" if i == 0 else "")
    plt.text(i, summer_consumption[i], month, fontsize=9, ha='center')

# Add title and labels
plt.title('Monthly Energy Consumption by Season')
plt.xlabel('Months')
plt.ylabel('Energy Consumption (kWh)')

# x-axis labels
plt.xticks(range(len(months)), months, rotation=45)

# Add legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()