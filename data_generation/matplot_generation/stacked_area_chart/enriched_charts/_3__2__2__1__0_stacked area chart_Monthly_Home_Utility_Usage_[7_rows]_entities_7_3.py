
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
physical_activity = np.array([120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230])
healthy_eating = np.array([150, 140, 135, 130, 125, 120, 115, 110, 105, 100, 95, 90])
mental_wellbeing = np.array([130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185])
sleep_quality = np.array([140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195])
social_connections = np.array([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165])

# Stacking the data
wellness = np.vstack([physical_activity, healthy_eating, mental_wellbeing, sleep_quality, social_connections])

# Plot
fig, ax = plt.subplots(figsize=(16, 8))
ax.stackplot(months, wellness, colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF'])
ax.set_title('Monthly Wellness Activities in 2023', fontsize=20, fontweight='bold', loc='center')
ax.set_ylabel('Activity Level', fontsize=14)
ax.set_xlabel('Months', fontsize=14)

# Adding annotation for high physical activity in December
physical_december_index = 11
ax.annotate('High Physical Activity', xy=(months[physical_december_index], physical_activity[physical_december_index]), xytext=(months[physical_december_index], physical_activity[physical_december_index] + 50),
            arrowprops=dict(facecolor='red', arrowstyle='->'), ha='center', fontsize=12)

# Adding annotation for peak mental wellbeing in December
mental_december_index = 11
ax.annotate('Peak Mental Wellbeing', xy=(months[mental_december_index], mental_wellbeing[mental_december_index]), xytext=(months[mental_december_index], mental_wellbeing[mental_december_index] + 50),
            arrowprops=dict(facecolor='blue', arrowstyle='->'), ha='center', fontsize=12)

plt.legend(['Physical Activity', 'Healthy Eating', 'Mental Wellbeing', 'Sleep Quality', 'Social Connections'], loc='upper left')
plt.tight_layout()
plt.show()