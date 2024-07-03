
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
waterfall = np.array([110, 130, 150, 180, 200, 210, 220, 230, 240, 250, 260, 270])
glacier = np.array([120, 140, 160, 185, 210, 220, 230, 240, 250, 260, 270, 280])
volcano = np.array([130, 150, 170, 190, 220, 230, 240, 250, 260, 270, 280, 290])
desert = np.array([180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235])
rainforest = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310])

# Stacking the data
natural_wonders = np.vstack([waterfall, glacier, volcano, desert, rainforest])

# Plot
fig, ax = plt.subplots(figsize=(14, 7))  # Modified chart size
ax.stackplot(months, natural_wonders, colors=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD'])
ax.set_title('Monthly Visitor Numbers to Natural Wonders in 2023', fontsize=18, fontweight='bold')  # Changed title
ax.set_ylabel('Visitor Numbers (in thousands)', fontsize=14)

# Adding annotation on the chart for the maximum visitor numbers to Rainforest
max_rainforest_index = np.argmax(rainforest)
ax.annotate('Peak Visitors', xy=(max_rainforest_index, rainforest[max_rainforest_index]), 
            xytext=(max_rainforest_index, rainforest[max_rainforest_index] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

# Adding legend
ax.legend(['Waterfall', 'Glacier', 'Volcano', 'Desert', 'Rainforest'], loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()