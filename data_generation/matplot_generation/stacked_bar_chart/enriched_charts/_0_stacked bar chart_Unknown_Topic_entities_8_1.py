
import matplotlib.pyplot as plt

# Data from the table
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
region_a = [1200, 1500, 1800, 1600, 2000, 2200, 2400, 2300, 2200, 2000, 1900, 2100]
region_b = [800, 900, 1100, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
region_c = [1500, 1400, 1600, 1700, 1900, 1800, 2000, 2100, 1900, 2200, 2100, 2200]
region_d = [700, 600, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]

# Stacked bar data preparation
bar_width = 0.5
indices = range(len(months))

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

ax.barh(indices, region_a, height=bar_width, color='#1f77b4', label='Region A')
ax.barh(indices, region_b, height=bar_width, left=region_a, color='#ff7f0e', label='Region B')
ax.barh(indices, region_c, height=bar_width, left=[i+j for i,j in zip(region_a, region_b)], color='#2ca02c', label='Region C')
ax.barh(indices, region_d, height=bar_width, left=[i+j+k for i,j,k in zip(region_a, region_b, region_c)], color='#d62728', label='Region D')

# Labels and Titles
ax.set_xlabel('Sales in Units')
ax.set_title('Monthly Sales Data by Region')
ax.set_yticks(indices)
ax.set_yticklabels(months)
ax.legend(loc='best')

# Remove the spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Grid lines
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Show plot
plt.tight_layout()
plt.show()