
import matplotlib.pyplot as plt

# Data
data = [
    {'Year': 2018, 'Electricity': 4000, 'Natural Gas': 2500, 'Heating Oil': 500, 'Propane': 200},
    {'Year': 2019, 'Electricity': 4200, 'Natural Gas': 2400, 'Heating Oil': 450, 'Propane': 150},
    {'Year': 2020, 'Electricity': 3500, 'Natural Gas': 2000, 'Heating Oil': 300, 'Propane': 100},
    {'Year': 2021, 'Electricity': 3700, 'Natural Gas': 2200, 'Heating Oil': 280, 'Propane': 120}
]

# Extracting individual components
years = [item['Year'] for item in data]
electricity = [item['Electricity'] for item in data]
natural_gas = [item['Natural Gas'] for item in data]
heating_oil = [item['Heating Oil'] for item in data]
propane = [item['Propane'] for item in data]

# Stacked Bar Chart
fig, ax = plt.subplots()

ax.bar(years, electricity, label='Electricity', color='skyblue', edgecolor='black')
ax.bar(years, natural_gas, bottom=electricity, label='Natural Gas', color='lightgreen', edgecolor='black')
bottoms_for_heating_oil = [e+n for e, n in zip(electricity, natural_gas)]
ax.bar(years, heating_oil, bottom=bottoms_for_heating_oil, label='Heating Oil', color='salmon', edgecolor='black')
bottoms_for_propane = [e+n+h for e, n, h in zip(electricity, natural_gas, heating_oil)]
ax.bar(years, propane, bottom=bottoms_for_propane, label='Propane', color='gold', edgecolor='black')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Energy Consumption (in Millions)')
plt.title('Energy Consumption by Year and Source')
plt.xticks(years) # ensures only those years are used for the x-axis

# Adding legend outside of the plot to the upper left
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

# Display the plot
plt.tight_layout()
plt.show()