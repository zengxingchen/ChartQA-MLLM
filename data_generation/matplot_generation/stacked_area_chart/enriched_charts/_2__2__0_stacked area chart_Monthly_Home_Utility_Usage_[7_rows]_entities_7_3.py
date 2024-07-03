
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
retail = np.array([120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230])
healthcare = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310])
technology = np.array([300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410])
real_estate = np.array([250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360])
energy = np.array([180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290])

# Stacking the data
sales_data = np.vstack([retail, healthcare, technology, real_estate, energy])

# Plot
fig, ax = plt.subplots(figsize=(16, 8))  # Modified chart size
ax.stackplot(months, sales_data, colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFD433'])
ax.set_title('Monthly Sales by Sector in 2023', fontsize=18, fontweight='bold', loc='center')  # Changed title
ax.set_ylabel('Sales (in million $)')
ax.set_xlabel('Month')

# Adding annotation on the chart for the maximum technology sales
max_tech_index = np.argmax(technology)
ax.annotate('Peak Technology Sales', xy=(max_tech_index, technology[max_tech_index]), xytext=(max_tech_index, technology[max_tech_index] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

plt.tight_layout()
plt.show()