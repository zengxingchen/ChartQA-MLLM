
import matplotlib.pyplot as plt

# Data
age_groups = ['10-15', '16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56-60', '61-65', '66-70', '71-75', '76-80']
average_screen_time = [3.5, 4.0, 4.5, 4.2, 3.8, 3.5, 3.0, 2.5, 2.0, 1.8, 1.5, 1.2, 1.0, 0.8]
population = [2500, 3000, 3500, 3300, 2800, 2600, 2300, 2000, 1700, 1500, 1200, 1000, 800, 600]
colors = ['#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107']
sizes = [i / 10 for i in population]

fig, ax = plt.subplots(figsize=(12, 8))  # Modify width and height of the chart

# Bubble chart
for i in range(len(age_groups)):
    ax.scatter(age_groups[i], average_screen_time[i], s=sizes[i], alpha=0.6, color=colors[i], edgecolor='black')

# Title and labels
ax.set_title('Average Daily Screen Time by Age Group', pad=20)
ax.set_xlabel('Age Group')
ax.set_ylabel('Average Screen Time (Hours)')

plt.show()