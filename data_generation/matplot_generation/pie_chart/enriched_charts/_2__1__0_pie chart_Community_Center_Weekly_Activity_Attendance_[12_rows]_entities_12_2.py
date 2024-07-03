
import matplotlib.pyplot as plt

# Data setup
food_groups = ['Vegetables', 'Fruits', 'Grains', 'Protein', 'Dairy', 'Fats and Oils']
percentages = [30, 20, 25, 15, 10, 5]
colors = ['#ffcc99','#66c2a5','#fc8d62','#8da0cb','#e78ac3','#a6d854']

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # width and height of the chart
ax.pie(percentages, labels=food_groups, autopct='%1.1f%%', colors=colors, startangle=90)
ax.set_title('Proportion of Food Groups in a Balanced Diet', pad=20)

# Show plot
plt.show()