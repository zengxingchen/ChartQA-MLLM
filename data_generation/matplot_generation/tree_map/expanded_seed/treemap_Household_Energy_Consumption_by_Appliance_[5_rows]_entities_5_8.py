
import matplotlib.pyplot as plt
import squarify

# Data
data = [
    {'Appliance': 'Heating', 'Utility': 'Central Heating', 'Annual Usage (kWh)': 4000, 'Annual Cost (USD)': 480},
    {'Appliance': 'Cooling', 'Utility': 'Air Conditioner', 'Annual Usage (kWh)': 1500, 'Annual Cost (USD)': 180},
    {'Appliance': 'Water Heating', 'Utility': 'Water Heater', 'Annual Usage (kWh)': 1200, 'Annual Cost (USD)': 144},
    {'Appliance': 'Appliances', 'Utility': 'Refrigerator', 'Annual Usage (kWh)': 600, 'Annual Cost (USD)': 72},
    {'Appliance': 'Lighting', 'Utility': 'LED Bulbs', 'Annual Usage (kWh)': 300, 'Annual Cost (USD)': 36}
]

# Prepare the data for the treemap
sizes = [entry['Annual Cost (USD)'] for entry in data]  # Sizes based on annual cost
labels = [f"{entry['Appliance']}\n{entry['Utility']}\n{entry['Annual Usage (kWh)']} kWh\n${entry['Annual Cost (USD)']}" for entry in data]
colors = plt.cm.viridis_r(range(len(sizes)))  # Take colors from the reversed viridis color map

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Additional settings
plt.title('Annual Energy Usage and Costs by Appliance')
plt.axis('off')  # Hide the axis

# Display the plot
plt.show()