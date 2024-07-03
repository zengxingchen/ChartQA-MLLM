
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
carbon_emissions = [200, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300, 310]
renewable_energy_usage = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
waste_generated = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]

fig, ax = plt.subplots(figsize=(12, 10))

# Stacked bar chart with custom colors and horizontal orientation
bars_ce = plt.bar(months, carbon_emissions, color='#3498DB', edgecolor='white', width=0.7, label='Carbon Emissions')
bars_reu = plt.bar(months, renewable_energy_usage, bottom=carbon_emissions, color='#E74C3C', edgecolor='white', width=0.7, label='Renewable Energy Usage')
bars_wg = plt.bar(months, waste_generated, bottom=[i+j for i,j in zip(carbon_emissions, renewable_energy_usage)], color='#2ECC71', edgecolor='white', width=0.7, label='Waste Generated')

# Customizing the axes and title
ax.set_ylabel('Quantity')
ax.set_title('Monthly Environmental Impact Data', pad=20)
ax.set_xticks(range(len(months)), labels=months)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1), title='Metrics')

# Padding between the end of the bars and the edge of the figure
plt.margins(x=0.05)

# Display the plot
plt.show()