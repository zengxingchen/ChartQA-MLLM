
import matplotlib.pyplot as plt
import numpy as np

# Data
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia']
coal = [25, 15, 45, 10, 35, 20]
natural_gas = [30, 20, 25, 25, 30, 40]
hydro = [10, 15, 5, 35, 10, 5]
nuclear = [20, 30, 10, 5, 5, 10]
renewables = [15, 20, 15, 25, 20, 25]

# Stacked bar positions
bar_width = 0.5
bar_positions = np.arange(len(regions))

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(bar_positions, coal, color='#4B0082', edgecolor='white', height=bar_width, label='Coal')
ax.barh(bar_positions, natural_gas, left=coal, color='#FF6347', edgecolor='white', height=bar_width, label='Natural Gas')
ax.barh(bar_positions, hydro, left=np.array(coal) + np.array(natural_gas), color='#00FA9A', edgecolor='white', height=bar_width, label='Hydro')
ax.barh(bar_positions, nuclear, left=np.array(coal) + np.array(natural_gas) + np.array(hydro), color='#FFD700', edgecolor='white', height=bar_width, label='Nuclear')
ax.barh(bar_positions, renewables, left=np.array(coal) + np.array(natural_gas) + np.array(hydro) + np.array(nuclear), color='#1E90FF', edgecolor='white', height=bar_width, label='Renewables')

# Labels and titles
ax.set_xlabel('Percentage (%)')
ax.set_title('Energy Sources Distribution by Region', pad=20)
ax.set_yticks(bar_positions)
ax.set_yticklabels(regions)
ax.legend(loc='lower right', bbox_to_anchor=(1, 0))

# Show plot
plt.tight_layout()
plt.show()