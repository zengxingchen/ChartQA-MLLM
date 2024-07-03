
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
makeup = np.array([250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360])
skincare = np.array([300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410])
haircare = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310])
fragrance = np.array([150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260])
nailcare = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210])

# Stacking the data
beauty_sales = np.vstack([makeup, skincare, haircare, fragrance, nailcare])

# Plot
fig, ax = plt.subplots(figsize=(14, 7))  # Modified chart size
ax.stackplot(months, beauty_sales, colors=['#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#33fff5'])
ax.set_title('Monthly Beauty Product Sales in 2023', fontsize=16, fontweight='bold')  # Changed title
ax.set_ylabel('Sales (in thousand units)')
ax.set_xlabel('Months')

# Adding annotation on the chart for the maximum skincare sales
max_skincare_index = np.argmax(skincare)
ax.annotate('Max Skincare', xy=(months[max_skincare_index], skincare[max_skincare_index]), xytext=(months[max_skincare_index], skincare[max_skincare_index] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

plt.tight_layout()
plt.show()