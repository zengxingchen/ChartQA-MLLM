
import matplotlib.pyplot as plt
import squarify

# Data from your provided dataset.
data = [
    {'Appliance': 'Refrigerator', 'Energy Consumption (kWh)': 150, 'Cost per Month (USD)': 20.25, 'Room': 'Kitchen'},
    {'Appliance': 'HVAC System', 'Energy Consumption (kWh)': 400, 'Cost per Month (USD)': 54.00, 'Room': 'Living Room'},
    {'Appliance': 'Washing Machine', 'Energy Consumption (kWh)': 75, 'Cost per Month (USD)': 10.13, 'Room': 'Laundry Room'},
    {'Appliance': 'Oven', 'Energy Consumption (kWh)': 90, 'Cost per Month (USD)': 12.15, 'Room': 'Kitchen'},
    {'Appliance': 'Lighting', 'Energy Consumption (kWh)': 100, 'Cost per Month (USD)': 13.5, 'Room': 'Entire House'}
]

# Extracting 'Energy Consumption (kWh)' as sizes for the rectangles
sizes = [item['Energy Consumption (kWh)'] for item in data]
labels = [f"{item['Appliance']}\n({item['Cost per Month (USD)']} USD)" for item in data]
colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Creating the treemap
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7)

# Removing the axes, as they are not meaningful for treemaps
plt.axis('off')

# Set the title of the treemap
plt.title('Energy Consumption and Cost per Month of Appliances', size=15)

# Show the treemap
plt.show()