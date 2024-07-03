
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2020, 'Electricity': '35%', 'Natural Gas': '40%', 'Heating Oil': '20%', 'Solar': '5%'},
    {'Year': 2021, 'Electricity': '33%', 'Natural Gas': '42%', 'Heating Oil': '18%', 'Solar': '7%'},
    {'Year': 2022, 'Electricity': '30%', 'Natural Gas': '43%', 'Heating Oil': '15%', 'Solar': '12%'},
    {'Year': 2023, 'Electricity': '28%', 'Natural Gas': '45%', 'Heating Oil': '12%', 'Solar': '15%'}
]

# Extract data and convert percentages to numeric values
years = [item['Year'] for item in data]
electricity = [int(item['Electricity'].rstrip('%')) for item in data]
natural_gas = [int(item['Natural Gas'].rstrip('%')) for item in data]
heating_oil = [int(item['Heating Oil'].rstrip('%')) for item in data]
solar = [int(item['Solar'].rstrip('%')) for item in data]

# Stack the data
bottom_electricity = [0] * len(years)
bottom_natural_gas = list(map(lambda x, y: x + y, bottom_electricity, electricity))
bottom_heating_oil = list(map(lambda x, y: x + y, bottom_natural_gas, natural_gas))
bottom_solar = list(map(lambda x, y: x + y, bottom_heating_oil, heating_oil))

# Plot the data
fig, ax = plt.subplots()

ax.bar(years, electricity, label='Electricity', color='blue', bottom=bottom_electricity)
ax.bar(years, natural_gas, label='Natural Gas', color='orange', bottom=bottom_natural_gas)
ax.bar(years, heating_oil, label='Heating Oil', color='green', bottom=bottom_heating_oil)
ax.bar(years, solar, label='Solar', color='yellow', bottom=bottom_solar)

# Formatting
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Year')
ax.set_title('Energy Sources Distribution by Year')
ax.set_xticks(years)
ax.set_yticks(range(0, 101, 10))
ax.legend(title='Energy Source')

# Display values on the bars
for i, (el, ng, ho, so) in enumerate(zip(electricity, natural_gas, heating_oil, solar)):
    ax.text(years[i], bottom_electricity[i] + el/2, f"{el}%", ha='center', va='center')
    ax.text(years[i], bottom_natural_gas[i] + ng/2, f"{ng}%", ha='center', va='center')
    ax.text(years[i], bottom_heating_oil[i] + ho/2, f"{ho}%", ha='center', va='center')
    ax.text(years[i], bottom_solar[i] + so/2, f"{so}%", ha='center', va='center')

# Show the figure
plt.show()