
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
ai_research = np.array([130, 140, 160, 170, 180, 185, 190, 180, 170, 160, 150, 140])
quantum_computing = np.array([160, 170, 180, 185, 195, 200, 205, 200, 190, 180, 170, 160])
robotics = np.array([135, 130, 145, 150, 155, 160, 165, 160, 155, 150, 145, 140])
space_exploration = np.array([210, 220, 230, 235, 240, 250, 255, 250, 240, 230, 220, 210])
green_technology = np.array([140, 135, 125, 115, 105, 95, 85, 90, 105, 115, 130, 145])
bioengineering = np.array([120, 125, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120])

# Stacking the data
tech_research = np.vstack([ai_research, quantum_computing, robotics, space_exploration, green_technology, bioengineering])

# Plot
fig, ax = plt.subplots(figsize=(18, 9))
ax.stackplot(months, tech_research, colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFA6'])
ax.set_title('Monthly Research Investment in Future Technologies (2023)', fontsize=20, fontweight='bold', loc='left')
ax.set_ylabel('Investment (Million USD)', fontsize=14)
ax.set_xlabel('Months', fontsize=14)

# Adding annotation on the chart for the maximum space exploration investment
max_space_index = np.argmax(space_exploration)
ax.annotate('Max Space Exploration', xy=(months[max_space_index], space_exploration[max_space_index]), xytext=(months[max_space_index], space_exploration[max_space_index] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center', fontsize=12)

# Adding annotation for AI research in July
ai_july_index = 6
ax.annotate('High AI Research', xy=(months[ai_july_index], ai_research[ai_july_index]), xytext=(months[ai_july_index], ai_research[ai_july_index] + 50),
            arrowprops=dict(facecolor='blue', arrowstyle='->'), ha='center', fontsize=12)

plt.tight_layout()
plt.show()