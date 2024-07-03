
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2010, 'Electricity': 44.5, 'Natural Gas': 34, 'Fuel Oil': 6, 'Propane': 5, 'Renewable Energy': 10.5},
    {'Year': 2015, 'Electricity': 40.0, 'Natural Gas': 31, 'Fuel Oil': 7, 'Propane': 6, 'Renewable Energy': 16.0},
    {'Year': 2018, 'Electricity': 35.0, 'Natural Gas': 29, 'Fuel Oil': 8, 'Propane': 6, 'Renewable Energy': 22.0},
    {'Year': 2020, 'Electricity': 33.0, 'Natural Gas': 28, 'Fuel Oil': 5, 'Propane': 5, 'Renewable Energy': 29.0},
    {'Year': 2022, 'Electricity': 30.0, 'Natural Gas': 26, 'Fuel Oil': 4, 'Propane': 4, 'Renewable Energy': 36.0}
]

# Extracting categories and stacking them
years = [entry['Year'] for entry in data]
energy_types = list(data[0].keys())[1:]  # Excluding the 'Year' key
stacked_data = {energy: [entry[energy] for entry in data] for energy in energy_types}

# Normalizing data to sum up to 100 for each year
stacked_percentages = {energy: [entry[energy] / sum(entry.values()) * 100 for entry in data] for energy in energy_types}

# Plotting the stacked bar chart
fig, ax = plt.subplots()

bottoms = [0] * len(years)
for energy in energy_types:
    ax.bar(years, stacked_percentages[energy], bottom=bottoms, label=energy)
    # Updating the bottoms for the next energy type in the stack
    bottoms = [bottoms[i] + stacked_percentages[energy][i] for i in range(len(bottoms))]

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Energy Consumption by Source (Percentage Stacked Bar Chart)')

# Display percentage values on the bars
for i, year in enumerate(years):
    cumulative_percentage = 0
    for energy in energy_types:
        value = stacked_percentages[energy][i]
        # Display the value if it's not too small
        if value > 5:
            plt.text(year, cumulative_percentage + value / 2, f"{value:.1f}%", ha='center', va='center')
        cumulative_percentage += value
    
ax.set_xticks(years)
ax.legend()

plt.tight_layout()
plt.show()