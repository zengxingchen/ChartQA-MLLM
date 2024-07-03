
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calories_carbs = [200, 220, 250, 230, 270, 280, 290, 300, 310, 320, 330, 340]
calories_fats = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
calories_protein = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

# Color codes for each calorie type
colors = ['#ff6347', '#4682b4', '#32cd32']

# Plot stacked horizontal bar chart
plt.figure(figsize=(14, 8)) # Width and height of the chart in inches
bar_height = 0.6 # Height of the bars

plt.barh(months, calories_carbs, color=colors[0], edgecolor='white', height=bar_height, label='Carbs')
plt.barh(months, calories_fats, left=calories_carbs, color=colors[1], edgecolor='white', height=bar_height, label='Fats')
plt.barh(months, calories_protein, left=[i+j for i,j in zip(calories_carbs, calories_fats)], color=colors[2], edgecolor='white', height=bar_height, label='Protein')

# Add labels and title
plt.xlabel('Calories')
plt.ylabel('Month')
plt.title('Monthly Caloric Intake from Different Nutrients')
plt.legend(loc='lower right')

# Add numerical labels
for i, (carb, fat, protein) in enumerate(zip(calories_carbs, calories_fats, calories_protein)):
    plt.text(carb / 2, i, str(carb), ha='center', va='center', color='white', fontweight='bold')
    plt.text(carb + fat / 2, i, str(fat), ha='center', va='center', color='white', fontweight='bold')
    plt.text(carb + fat + protein / 2, i, str(protein), ha='center', va='center', color='white', fontweight='bold')

# Display the final result
plt.show()