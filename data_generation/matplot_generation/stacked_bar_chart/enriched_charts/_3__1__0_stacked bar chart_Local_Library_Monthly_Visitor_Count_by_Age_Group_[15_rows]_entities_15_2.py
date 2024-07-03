
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
fruits = [85, 95, 90, 100, 110, 115, 125, 120, 110, 115, 100, 90]
vegetables = [78, 85, 80, 88, 95, 100, 105, 102, 90, 98, 85, 80]
grains = [95, 105, 100, 110, 120, 125, 135, 130, 120, 125, 110, 100]

# Color codes for each food type
colors = ['#FF6347', '#32CD32', '#FFD700']

# Plot stacked bar chart
plt.figure(figsize=(14, 8)) # Width and height of the chart in inches
bar_height = 0.6 # Height of the bars

plt.barh(months, fruits, color=colors[0], edgecolor='white', height=bar_height, label='Fruits')
plt.barh(months, vegetables, left=fruits, color=colors[1], edgecolor='white', height=bar_height, label='Vegetables')
plt.barh(months, grains, left=[i+j for i,j in zip(fruits, vegetables)], color=colors[2], edgecolor='white', height=bar_height, label='Grains')

# Add labels and title
plt.xlabel('Consumption')
plt.ylabel('Month')
plt.title('Monthly Consumption of Different Food Types', pad=20)
plt.legend(loc='lower right')

# Assign numerical labels to each bar
for i in range(len(months)):
    plt.text(fruits[i] / 2, i, str(fruits[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(fruits[i] + vegetables[i] / 2, i, str(vegetables[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(fruits[i] + vegetables[i] + grains[i] / 2, i, str(grains[i]), ha='center', va='center', color='black', fontweight='bold')

# Display the final result
plt.show()