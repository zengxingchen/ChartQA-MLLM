
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2024', '2025', '2026', '2027', '2028']
electric_vehicles = [20, 25, 30, 35, 40]
autonomous_vehicles = [15, 20, 25, 30, 35]
shared_mobility = [30, 25, 20, 15, 10]
public_transport = [35, 30, 25, 20, 15]

# Stack data
data = np.array([electric_vehicles, autonomous_vehicles, shared_mobility, public_transport])
data_cum = data.cumsum(axis=0)

# Bar width
bar_width = 0.5

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
for i, (colname, color) in enumerate(zip(['Electric Vehicles', 'Autonomous Vehicles', 'Shared Mobility', 'Public Transport'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(years, widths, left=starts, height=bar_width, label=colname, color=color)

# Add legend
ax.legend(ncol=2, bbox_to_anchor=(1, 1), loc='upper left')

# Add title and labels
ax.set_title('Future Technologies & Society: Adoption Rates (2024-2028)', fontsize=14, pad=20)
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Year')

plt.show()