
import matplotlib.pyplot as plt
import squarify

# Data provided in tabular format
chart_data = [
    {'Appliance': 'Air Conditioner', 'Annual Energy Consumption (kWh)': 2150, 'Cost per Year (USD)': 322.0},
    {'Appliance': 'Refrigerator', 'Annual Energy Consumption (kWh)': 600, 'Cost per Year (USD)': 90.0},
    {'Appliance': 'Washing Machine', 'Annual Energy Consumption (kWh)': 150, 'Cost per Year (USD)': 22.5},
    {'Appliance': 'Dishwasher', 'Annual Energy Consumption (kWh)': 200, 'Cost per Year (USD)': 30.0}
]

# Prepare data for the treemap
sizes = [data['Annual Energy Consumption (kWh)'] for data in chart_data]
labels = ["{}\n{} kWh\n${}".format(data['Appliance'], data['Annual Energy Consumption (kWh)'], data['Cost per Year (USD)']) for data in chart_data]
colors = plt.cm.viridis(range(len(labels)))  # You can choose any other appropriate colormap

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Decorate the plot
plt.title('Treemap of Annual Energy Consumption by Appliance')
plt.axis('off')  # Disable the axes

# Display the plot
plt.show()