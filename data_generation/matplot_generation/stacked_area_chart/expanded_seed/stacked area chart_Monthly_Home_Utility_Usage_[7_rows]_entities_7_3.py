
import matplotlib.pyplot as plt

# Data provided in the question
data = [
    {'Month': 'January', ' Electricity (kWh)': 350, ' Water (Cubic Meters)': 25, ' Natural Gas (m³)': 30, ' Trash Collection (kg)': 12},
    {'Month': 'February', ' Electricity (kWh)': 320, ' Water (Cubic Meters)': 22, ' Natural Gas (m³)': 25, ' Trash Collection (kg)': 10},
    {'Month': 'March', ' Electricity (kWh)': 285, ' Water (Cubic Meters)': 20, ' Natural Gas (m³)': 22, ' Trash Collection (kg)': 9},
    {'Month': 'April', ' Electricity (kWh)': 275, ' Water (Cubic Meters)': 18, ' Natural Gas (m³)': 21, ' Trash Collection (kg)': 8},
    {'Month': 'May', ' Electricity (kWh)': 260, ' Water (Cubic Meters)': 19, ' Natural Gas (m³)': 19, ' Trash Collection (kg)': 7},
    {'Month': 'June', ' Electricity (kWh)': 270, ' Water (Cubic Meters)': 23, ' Natural Gas (m³)': 20, ' Trash Collection (kg)': 8},
    {'Month': 'July', ' Electricity (kWh)': 290, ' Water (Cubic Meters)': 25, ' Natural Gas (m³)': 23, ' Trash Collection (kg)': 9}
]

# Extracting the data for the plot
months = [entry['Month'] for entry in data]
electricity = [entry[' Electricity (kWh)'] for entry in data]
water = [entry[' Water (Cubic Meters)'] for entry in data]
natural_gas = [entry[' Natural Gas (m³)'] for entry in data]
trash_collection = [entry[' Trash Collection (kg)'] for entry in data]

# Plotting the stacked area chart
fig, ax = plt.subplots()
ax.stackplot(months, electricity, water, natural_gas, trash_collection, labels=['Electricity (kWh)', 'Water (Cubic Meters)', 'Natural Gas (m³)', 'Trash Collection (kg)'])

# Customizing the plot
ax.set_title('Utility Usage by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Consumption')
ax.legend(loc='upper left')

# Adding grid and styles
plt.grid(True, linestyle='--', alpha=0.5)
plt.style.use('ggplot')

# Show the plot
plt.show()