
import matplotlib.pyplot as plt
import squarify
import seaborn as sns

# Given chart data
data = [
    {'Appliance': 'Heating and Cooling', 'Annual Energy Consumption (kWh)': 6000, 'Cost per Year (USD)': 660},
    {'Appliance': 'Water Heater', 'Annual Energy Consumption (kWh)': 4000, 'Cost per Year (USD)': 440},
    {'Appliance': 'Washer and Dryer', 'Annual Energy Consumption (kWh)': 1000, 'Cost per Year (USD)': 110},
    {'Appliance': 'Lighting', 'Annual Energy Consumption (kWh)': 1500, 'Cost per Year (USD)': 165},
    {'Appliance': 'Refrigerator', 'Annual Energy Consumption (kWh)': 600, 'Cost per Year (USD)': 66}
]

# Extracting the necessary values from data
labels = [entry['Appliance'] for entry in data]
sizes = [entry['Annual Energy Consumption (kWh)'] for entry in data]
costs = [entry['Cost per Year (USD)'] for entry in data]

# Use the squarify library to plot a treemap
cmap = plt.cm.viridis
minima = min(costs)
maxima = max(costs)
norm = plt.Normalize(vmin=minima, vmax=maxima)
colors = [cmap(norm(value)) for value in costs]

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7)

# Adding a color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(costs), vmax=max(costs)))
sm.set_array([])
plt.colorbar(sm, label='Cost per Year (USD)')

# Use seaborn's styling
sns.set(style="white", context="talk")
plt.axis('off')
plt.title('Annual Energy Consumption and Cost per Year', fontsize=16)
plt.show()