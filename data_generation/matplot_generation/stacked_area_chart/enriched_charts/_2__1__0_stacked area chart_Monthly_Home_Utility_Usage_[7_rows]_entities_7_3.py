
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
calories_burned = np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
steps_walked = np.array([10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500])
calories_consumed = np.array([2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050])
hours_slept = np.array([7.5, 7.6, 7.8, 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6])
water_intake = np.array([2.1, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3])

# Stacking the data
fitness_data = np.vstack([calories_burned, steps_walked, calories_consumed, hours_slept, water_intake])

# Plot
fig, ax = plt.subplots(figsize=(16, 8))
ax.stackplot(months, fitness_data, colors=['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#8A2BE2'])
ax.set_title('Monthly Fitness Data for 2023', fontsize=18, fontweight='bold', loc='center')
ax.set_ylabel('Fitness Metrics')

# Adding annotation on the chart for the maximum water intake
max_water_index = np.argmax(water_intake)
ax.annotate('Max Water Intake', xy=(max_water_index, water_intake[max_water_index]), xytext=(max_water_index, water_intake[max_water_index] + 10),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

plt.tight_layout()
plt.show()