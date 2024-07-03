
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Given data
data = [
    {'Appliance': 'Refrigerator', 'Annual Energy Consumption (kWh)': 600, 'Percentage': 35},
    {'Appliance': 'Washing Machine', 'Annual Energy Consumption (kWh)': 150, 'Percentage': 9},
    {'Appliance': 'Dishwasher', 'Annual Energy Consumption (kWh)': 200, 'Percentage': 12},
    {'Appliance': 'TV', 'Annual Energy Consumption (kWh)': 400, 'Percentage': 23},
    {'Appliance': 'Lighting', 'Annual Energy Consumption (kWh)': 350, 'Percentage': 21}
]

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Create a normalized size value for each slice
sizes = df['Annual Energy Consumption (kWh)']
labels = df.apply(lambda x: '{}\n{} kWh\n{}%'.format(x['Appliance'], x['Annual Energy Consumption (kWh)'], x['Percentage']), axis=1)
colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

# Create a figure and a subplot
fig, ax = plt.subplots(1, figsize = (12,8))

# Treemap parameters
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, ax=ax)

# Remove axis
ax.axis('off')

# Set title
ax.set_title('Annual Energy Consumption by Appliance', fontsize=18)

# Plot the treemap
plt.show()