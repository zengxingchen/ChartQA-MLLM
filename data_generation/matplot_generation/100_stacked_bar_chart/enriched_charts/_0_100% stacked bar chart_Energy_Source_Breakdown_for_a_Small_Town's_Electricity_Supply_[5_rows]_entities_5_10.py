
import matplotlib.pyplot as plt

# Data
years = ['2019', '2020', '2021']
energy_sources = {
    'Coal': [45, 40, 35],
    'Natural Gas': [35, 30, 25],
    'Nuclear': [10, 15, 20],
    'Renewables': [10, 15, 20]
}

# Normalize the data to sum to 100% for each year
totals = [sum(values) for values in zip(*energy_sources.values())]
data_percentage = {source: [value / total * 100 for value, total in zip(values, totals)]
                   for source, values in energy_sources.items()}

# Set up the colors for each energy source
colors = {
    'Coal': '#1d1d1d',
    'Natural Gas': '#f97306',
    'Nuclear': '#07f2f8',
    'Renewables': '#7dff0b'
}

# Setup the bars
prev_values = [0] * len(years)
fig, ax = plt.subplots(figsize=(10, 8))  # Change the figure size here

for energy, values in data_percentage.items():
    ax.barh(
        years,  # Make it horizontal
        values,
        left=prev_values,  # Stack the bars
        color=colors[energy],
        edgecolor='white',
        height=0.6  # Adjust the height of the bars
    )
    prev_values = [pv + v for pv, v in zip(prev_values, values)]

# Customizing the chart
ax.set_xlabel('Percentage')
ax.set_title('Energy Source Distribution for Electricity Generation')
ax.set_xlim(0, 100)  # Ensure the x-axis range from 0 to 100%

# Add the legend
energy_patches = [plt.Rectangle((0, 0), 1, 1, color=colors[energy]) for energy in energy_sources]
ax.legend(energy_patches, energy_sources.keys(), bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()