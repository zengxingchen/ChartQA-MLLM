
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'January', 'Average Daily Electricity Use (kWh)': 30, 'Average Daily Natural Gas Use (cubic feet)': 200},
    {'Month': 'February', 'Average Daily Electricity Use (kWh)': 22, 'Average Daily Natural Gas Use (cubic feet)': 180},
    {'Month': 'March', 'Average Daily Electricity Use (kWh)': 19, 'Average Daily Natural Gas Use (cubic feet)': 150},
    {'Month': 'April', 'Average Daily Electricity Use (kWh)': 17, 'Average Daily Natural Gas Use (cubic feet)': 130},
    {'Month': 'May', 'Average Daily Electricity Use (kWh)': 18, 'Average Daily Natural Gas Use (cubic feet)': 120}
]

# Extracting the months, electricity, and natural gas data
months = [item['Month'] for item in data]
electricity_use = [item['Average Daily Electricity Use (kWh)'] for item in data]
natural_gas_use = [item['Average Daily Natural Gas Use (cubic feet)'] for item in data]

# Converting months to numerical values for scatterplot
month_numbers = range(1, len(months) + 1)

# Creating scatterplot
plt.figure(figsize=(10, 5))  # Set the figure size

plt.scatter(month_numbers, electricity_use, color='blue', label='Electricity Use (kWh)', marker='o')
plt.scatter(month_numbers, natural_gas_use, color='red', label='Natural Gas Use (cubic feet)', marker='^')

# Apply labels, title and legend
plt.xlabel('Month')
plt.ylabel('Average Daily Use')
plt.title('Average Daily Use of Electricity and Natural Gas')
plt.xticks(month_numbers, months)  # Set the x-ticks to be the months
plt.legend()

# Show grid
plt.grid(True)

# Show the plot
plt.show()