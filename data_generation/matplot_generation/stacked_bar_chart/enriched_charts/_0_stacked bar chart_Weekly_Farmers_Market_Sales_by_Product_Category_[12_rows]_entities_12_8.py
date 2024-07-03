
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June']
rent = [1500, 1500, 1500, 1500, 1500, 1500]
utilities = [200, 180, 190, 200, 210, 220]
groceries = [600, 620, 610, 640, 600, 590]
transportation = [300, 310, 320, 330, 340, 350]

# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(10, 6))  # changing width and height of the chart

bar_width = 0.6  # change width of bars
index = range(len(months))

p1 = plt.barh(index, rent, bar_width, label='Rent', color='#A52A2A')
p2 = plt.barh(index, utilities, bar_width, left=rent, label='Utilities', color='#FFD700')
p3 = plt.barh(index, groceries, bar_width, left=[r + u for r, u in zip(rent, utilities)], label='Groceries', color='#6495ED')
p4 = plt.barh(index, transportation, bar_width, left=[r + u + g for r, u, g in zip(rent, utilities, groceries)], label='Transportation', color='#90EE90')

plt.xlabel('Expenses in USD')
plt.yticks(index, months)
plt.title('Household Monthly Expenses')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)

# Customizing the grid
plt.grid(axis='x')

plt.show()