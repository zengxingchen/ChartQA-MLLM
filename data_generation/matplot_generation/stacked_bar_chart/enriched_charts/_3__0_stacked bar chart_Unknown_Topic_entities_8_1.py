
import matplotlib.pyplot as plt

# Data from the table
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
protein = [1100, 1400, 1700, 1500, 1900, 2100, 2300, 2200, 2100, 1900, 1800, 2000]
carbohydrates = [1300, 1100, 1400, 1300, 1500, 1700, 1800, 1900, 2000, 1700, 1600, 1800]
fat = [1200, 1300, 1500, 1600, 1700, 1800, 1900, 2000, 1800, 1900, 2000, 2100]
fiber = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]

# Stacked bar data preparation
bar_width = 0.35
indices = range(len(months))

# Plotting
fig, ax = plt.subplots(figsize=(10, 12))

ax.bar(indices, protein, width=bar_width, color='#ff9999', label='Protein')
ax.bar(indices, carbohydrates, width=bar_width, bottom=protein, color='#66b3ff', label='Carbohydrates')
ax.bar(indices, fat, width=bar_width, bottom=[i+j for i,j in zip(protein, carbohydrates)], color='#99ff99', label='Fat')
ax.bar(indices, fiber, width=bar_width, bottom=[i+j+k for i,j,k in zip(protein, carbohydrates, fat)], color='#ffcc99', label='Fiber')

# Labels and Titles
ax.set_ylabel('Nutrient Intake (grams)')
ax.set_title('Monthly Nutrient Intake Data')
ax.set_xticks(indices)
ax.set_xticklabels(months, rotation=45, ha='right')
ax.legend(loc='upper left')

# Remove the spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Grid lines
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Numerical labels for each bar segment
for i in range(len(months)):
    ax.text(i, protein[i] / 2, str(protein[i]), ha='center', va='center', color='black', fontsize=8)
    ax.text(i, protein[i] + carbohydrates[i] / 2, str(carbohydrates[i]), ha='center', va='center', color='black', fontsize=8)
    ax.text(i, protein[i] + carbohydrates[i] + fat[i] / 2, str(fat[i]), ha='center', va='center', color='black', fontsize=8)
    ax.text(i, protein[i] + carbohydrates[i] + fat[i] + fiber[i] / 2, str(fiber[i]), ha='center', va='center', color='black', fontsize=8)

# Show plot
plt.tight_layout()
plt.show()