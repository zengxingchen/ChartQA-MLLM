
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
income = [2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600]
savings = [800, 850, 900, 750, 820, 880, 900, 850, 830, 870, 920, 950]
investment = [600, 650, 700, 720, 750, 800, 850, 870, 900, 950, 1000, 1100]
entertainment = [300, 310, 320, 340, 330, 350, 360, 370, 380, 390, 400, 410]
transport = [200, 210, 220, 230, 210, 250, 260, 270, 280, 290, 300, 310]

# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(14, 10))  # changing width and height of the chart

bar_height = 0.5  # change height of bars
index = range(len(months))

p1 = plt.barh(index, income, bar_height, label='Income', color='#FF5733')
p2 = plt.barh(index, savings, bar_height, left=income, label='Savings', color='#33FF57')
p3 = plt.barh(index, investment, bar_height, left=[i + s for i, s in zip(income, savings)], label='Investment', color='#3357FF')
p4 = plt.barh(index, entertainment, bar_height, left=[i + s + inv for i, s, inv in zip(income, savings, investment)], label='Entertainment', color='#FF33A5')
p5 = plt.barh(index, transport, bar_height, left=[i + s + inv + e for i, s, inv, e in zip(income, savings, investment, entertainment)], label='Transport', color='#33A5FF')

plt.xlabel('Amount in USD')
plt.yticks(index, months)
plt.title('Monthly Income Allocation', pad=20)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=3)

# Customizing the grid
plt.grid(axis='x')

# Adding numerical labels to each bar segment
for i in range(len(months)):
    plt.text(income[i]/2, i, str(income[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(income[i] + savings[i]/2, i, str(savings[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(income[i] + savings[i] + investment[i]/2, i, str(investment[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(income[i] + savings[i] + investment[i] + entertainment[i]/2, i, str(entertainment[i]), va='center', ha='center', color='white', fontweight='bold')
    plt.text(income[i] + savings[i] + investment[i] + entertainment[i] + transport[i]/2, i, str(transport[i]), va='center', ha='center', color='white', fontweight='bold')

plt.show()