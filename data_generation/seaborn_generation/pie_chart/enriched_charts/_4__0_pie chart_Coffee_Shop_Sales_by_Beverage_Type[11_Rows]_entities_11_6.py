
import matplotlib.pyplot as plt

# Data
expense_categories = ['Housing', 'Food', 'Transportation', 'Healthcare', 'Entertainment', 'Savings', 'Utilities']
amounts = [35, 20, 15, 10, 8, 7, 5]
colors = ['#ff9999','#66b3ff','#99cc99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f']

# Pie chart
plt.figure(figsize=(10, 7))  # Change width and height of the chart
plt.pie(amounts, labels=expense_categories, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Monthly Household Expenses Distribution', y=1.08)

# Display the chart
plt.show()