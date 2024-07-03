
import matplotlib.pyplot as plt

# Data
data = [
    {'Year': 2018, 'Electricity': 320, 'Natural Gas': 210, 'Heating Oil': 50, 'Propane': 20, 'Renewables': 10},
    {'Year': 2019, 'Electricity': 330, 'Natural Gas': 220, 'Heating Oil': 45, 'Propane': 15, 'Renewables': 15},
    {'Year': 2020, 'Electricity': 310, 'Natural Gas': 225, 'Heating Oil': 40, 'Propane': 10, 'Renewables': 20},
    {'Year': 2021, 'Electricity': 305, 'Natural Gas': 230, 'Heating Oil': 35, 'Propane': 12, 'Renewables': 30},
    {'Year': 2022, 'Electricity': 300, 'Natural Gas': 240, 'Heating Oil': 30, 'Propane': 14, 'Renewables': 35}
]

# Extract information for plotting
years = [d['Year'] for d in data]
electricity = [d['Electricity'] for d in data]
natural_gas = [d['Natural Gas'] for d in data]
heating_oil = [d['Heating Oil'] for d in data]
propane = [d['Propane'] for d in data]
renewables = [d['Renewables'] for d in data]

# Start plotting the stacked bar chart
fig, ax = plt.subplots()

ax.bar(years, electricity, label='Electricity', color='skyblue')
ax.bar(years, natural_gas, bottom=electricity, label='Natural Gas', color='lightgreen')
# Use a list comprehension to add up the 'bottom' values for the Oil stack
ax.bar(years, heating_oil, bottom=[i+j for i, j in zip(electricity, natural_gas)], label='Heating Oil', color='gold')
# Adjust the bottom position for propane and renewables accordingly
ax.bar(years, propane, bottom=[i+j+k for i, j, k in zip(electricity, natural_gas, heating_oil)], label='Propane', color='purple')
ax.bar(years, renewables, bottom=[i+j+k+l for i, j, k, l in zip(electricity, natural_gas, heating_oil, propane)], label='Renewables', color='orange')

# Add some text for labels, title, and custom x-axis tick labels
ax.set_xlabel('Year')
ax.set_ylabel('Energy Consumption (in Terajoules)')
ax.set_title('Energy Consumption by Source and Year')
ax.set_xticks(years)
ax.set_xticklabels(years)

# Add a legend to describe the stack layers
ax.legend()
plt.tight_layout()  # This can help prevent overlap of elements in the figure

plt.show()