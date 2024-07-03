
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
salaries = [3000, 3200, 3100, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100]
investments = [500, 600, 550, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]
savings = [1000, 1200, 1100, 1300, 1250, 1350, 1400, 1450, 1500, 1550, 1600, 1650]
expenses = [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100]

# Stacked bar chart data accumulation
bars_investments = np.add(salaries, savings).tolist()

# Modify the color scheme using hexadecimal color codes
colors = ['#FFD700', '#ADFF2F', '#00CED1', '#FF4500']

fig, ax = plt.subplots(figsize=(12, 9)) # Change size of the chart

# Creating the vertical bar chart
ax.bar(months, salaries, color=colors[0], edgecolor='white', width=0.6, label='Salaries')
ax.bar(months, investments, bottom=salaries, color=colors[1], edgecolor='white', width=0.6, label='Investments')
ax.bar(months, savings, bottom=bars_investments, color=colors[2], edgecolor='white', width=0.6, label='Savings')
ax.bar(months, expenses, bottom=np.add(bars_investments, investments).tolist(), color=colors[3], edgecolor='white', width=0.6, label='Expenses')

# Customizing the vertical stacked bar chart with the new topic: 'Monthly Financial Distribution'
plt.title('Monthly Financial Distribution', pad=20)
plt.ylabel('Amount in USD')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the final plot
plt.show()