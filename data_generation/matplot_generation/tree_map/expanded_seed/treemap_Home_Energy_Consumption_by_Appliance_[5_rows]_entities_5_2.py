
import matplotlib.pyplot as plt
import squarify

# Data from the table
data = [
    {'Appliance': 'Refrigerator', 'Energy Consumption (kWh/year)': 600, 'Percentage of Total Energy': '29%'},
    {'Appliance': 'Air Conditioner', 'Energy Consumption (kWh/year)': 215, 'Percentage of Total Energy': '10%'},
    {'Appliance': 'Heating Systems', 'Energy Consumption (kWh/year)': 900, 'Percentage of Total Energy': '43%'},
    {'Appliance': 'Washing Machine', 'Energy Consumption (kWh/year)': 75, 'Percentage of Total Energy': '4%'},
    {'Appliance': 'Lighting', 'Energy Consumption (kWh/year)': 160, 'Percentage of Total Energy': '8%'}
]

# Extracting data for plotting
labels = [d['Appliance'] for d in data]
sizes = [d['Energy Consumption (kWh/year)'] for d in data]
percentages = [d['Percentage of Total Energy'].rstrip('%') for d in data]
colors = plt.cm.viridis([int(p)/100 for p in percentages])

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the treemap
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Adding title and axis off
plt.title('Energy Consumption by Appliances (kWh/year) and Percentage of Total Energy')
plt.axis('off')

# Custom legend to show percentages
for s, p in zip(sizes, percentages):
    plt.bar([], [], color=plt.cm.viridis(int(p)/100), label=f"{p}%", alpha=0.8)

plt.legend(title="Percentage of Total Energy", bbox_to_anchor=(1, 0.5), loc="center left")

# Show the plot
plt.show()