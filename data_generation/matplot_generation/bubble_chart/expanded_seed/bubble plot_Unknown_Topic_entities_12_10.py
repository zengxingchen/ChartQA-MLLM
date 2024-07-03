
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# The data provided
data = [
    {'Month': 'January', 'Print Books': 4603, 'Audio Books': 502, 'E-books': 1545, 'Library Visitors': 4035, 'Library Members': 14025, 'Total Checkouts': 6650},
    {'Month': 'February', 'Print Books': 4210, 'Audio Books': 560, 'E-books': 1620, 'Library Visitors': 3750, 'Library Members': 14050, 'Total Checkouts': 6390},
    # ... Continue with all months
    {'Month': 'December', 'Print Books': 5400, 'Audio Books': 820, 'E-books': 2045, 'Library Visitors': 4200, 'Library Members': 14250, 'Total Checkouts': 8265}
]

# Prepare data
months = [d['Month'] for d in data]
total_checkouts = np.array([d['Total Checkouts'] for d in data])
library_members = np.array([d['Library Members'] for d in data])
library_visitors_size = np.array([d['Library Visitors'] for d in data])

# Normalize library_visitors_size for bubble sizes
sizes = (library_visitors_size - library_visitors_size.min()) / (library_visitors_size.max() - library_visitors_size.min()) * 1000

# Color mapping for months
cmap = plt.cm.get_cmap('viridis', len(months))
month_to_color = {m: cmap(i) for i, m in enumerate(months)}

# Create the bubble chart
plt.figure(figsize=(12, 8))
scatter = plt.scatter(total_checkouts, library_members, s=sizes, c=[month_to_color[m] for m in months], alpha=0.6, edgecolors='w')

# Add a color bar
scalarmappaple = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=len(months)-1))
scalarmappaple.set_array(range(len(months)))
cbar = plt.colorbar(scalarmappaple, ticks=range(len(months)))
cbar.ax.set_yticklabels(months)

# Plot details
plt.title('Bubble chart representing library activities over a year')
plt.xlabel('Total Checkouts')
plt.ylabel('Library Members')
plt.grid(True, which='both', linestyle='--', linewidth=0.8)

# Show the plot
plt.show()