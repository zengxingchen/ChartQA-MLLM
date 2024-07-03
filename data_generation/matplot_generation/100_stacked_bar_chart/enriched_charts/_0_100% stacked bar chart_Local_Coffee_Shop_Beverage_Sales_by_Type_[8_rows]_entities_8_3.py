
import matplotlib.pyplot as plt

# Table data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
rent = [700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810]
groceries = [500, 480, 460, 450, 470, 490, 510, 530, 540, 550, 560, 580]
utilities = [200, 210, 220, 230, 210, 200, 190, 180, 170, 160, 150, 140]
entertainment = [100, 100, 100, 100, 80, 60, 40, 20, 10, 0, 0, 0]

# Convert the raw numbers to percentages of the total for each category
total = [sum(x) for x in zip(rent, groceries, utilities, entertainment)]
rent_percent = [i / j * 100 for i, j in zip(rent, total)]
groceries_percent = [i / j * 100 for i, j in zip(groceries, total)]
utilities_percent = [i / j * 100 for i, j in zip(utilities, total)]
entertainment_percent = [i / j * 100 for i, j in zip(entertainment, total)]

# The position of the bars on the x-axis
r = range(len(months))

fig, ax = plt.subplots(figsize=(14, 8))

# Stacked bar chart with modified parameters
barWidth = 0.85
ax.barh(r, rent_percent, color='#1E88E5', edgecolor='white', height=barWidth, label="Rent")
ax.barh(r, groceries_percent, left=rent_percent, color='#FFC107', edgecolor='white', height=barWidth, label="Groceries")
ax.barh(r, utilities_percent, left=[i + j for i, j in zip(rent_percent, groceries_percent)], color='#D81B60', edgecolor='white', height=barWidth, label="Utilities")
ax.barh(r, entertainment_percent, left=[i + j + k for i, j, k in zip(rent_percent, groceries_percent, utilities_percent)], color='#004D40', edgecolor='white', height=barWidth, label="Entertainment")

# Custom X axis
plt.yticks(r, months)
plt.xlabel("Percentage")
plt.title("Monthly Distribution of Household Expenses (Percentage)")

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Categories")

# Show graphic
plt.show()