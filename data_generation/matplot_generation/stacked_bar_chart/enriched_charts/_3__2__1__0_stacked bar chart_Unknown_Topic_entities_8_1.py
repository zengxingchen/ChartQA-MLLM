
import matplotlib.pyplot as plt

# Data
years = ['2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
usa = [5000, 4500, 4800, 5300, 5500, 5700, 5900, 6100, 6300, 6500, 6700, 6900]
europe = [4200, 4100, 4000, 4300, 4500, 4700, 4900, 5100, 5300, 5500, 5700, 5900]
asia = [3800, 3500, 3600, 3900, 4000, 4200, 4300, 4400, 4500, 4600, 4700, 4800]
south_america = [2900, 2700, 2800, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800]

# Stacked bar data preparation
bar_width = 0.8
indices = range(len(years))

# Plotting
fig, ax = plt.subplots(figsize=(12, 10))

ax.bar(indices, usa, width=bar_width, color='#4e79a7', label='USA')
ax.bar(indices, europe, width=bar_width, bottom=usa, color='#f28e2b', label='Europe')
ax.bar(indices, asia, width=bar_width, bottom=[i+j for i,j in zip(usa, europe)], color='#e15759', label='Asia')
ax.bar(indices, south_america, width=bar_width, bottom=[i+j+k for i,j,k in zip(usa, europe, asia)], color='#76b7b2', label='South America')

# Labels and Titles
ax.set_ylabel('Number of Tourists')
ax.set_title('Annual Tourist Arrivals by Region', pad=20)
ax.set_xticks(indices)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Add numerical labels to each bar segment
for idx in indices:
    ax.text(idx, usa[idx] / 2, str(usa[idx]), va='center', ha='center', color='white', fontsize=8)
    ax.text(idx, usa[idx] + europe[idx] / 2, str(europe[idx]), va='center', ha='center', color='white', fontsize=8)
    ax.text(idx, usa[idx] + europe[idx] + asia[idx] / 2, str(asia[idx]), va='center', ha='center', color='white', fontsize=8)
    ax.text(idx, usa[idx] + europe[idx] + asia[idx] + south_america[idx] / 2, str(south_america[idx]), va='center', ha='center', color='white', fontsize=8)

# Remove the spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Grid lines
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Show plot
plt.tight_layout()
plt.show()