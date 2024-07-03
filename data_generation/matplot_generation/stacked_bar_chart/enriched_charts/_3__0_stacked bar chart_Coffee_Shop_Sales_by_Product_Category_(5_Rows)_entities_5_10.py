
import matplotlib.pyplot as plt

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
clothing = [150, 160, 170, 180]
footwear = [120, 130, 140, 150]
accessories = [110, 115, 120, 125]
jewelry = [90, 95, 100, 110]

# Cumulative values for stacking
cumulative_clothing = clothing
cumulative_footwear = [c + f for c, f in zip(cumulative_clothing, footwear)]
cumulative_accessories = [f + a for f, a in zip(cumulative_footwear, accessories)]
cumulative_jewelry = [a + j for a, j in zip(cumulative_accessories, jewelry)]

# Figure and axis
fig, ax = plt.subplots(figsize=(8, 12))

# Stacked bar chart - vertical
ax.bar(quarters, clothing, color='#4e79a7', edgecolor='white', width=0.4, label='Clothing')
ax.bar(quarters, footwear, bottom=cumulative_clothing, color='#f28e2b', edgecolor='white', width=0.4, label='Footwear')
ax.bar(quarters, accessories, bottom=cumulative_footwear, color='#e15759', edgecolor='white', width=0.4, label='Accessories')
ax.bar(quarters, jewelry, bottom=cumulative_accessories, color='#76b7b2', edgecolor='white', width=0.4, label='Jewelry')

# Adding labels and a title, and a legend
ax.set_ylabel('Revenue (in millions)')
ax.set_title('Quarterly Revenue by Product Category in Fashion Industry')
ax.legend(loc='upper left')

# Adding numerical labels
for i, (c, f, a, j) in enumerate(zip(clothing, footwear, accessories, jewelry)):
    ax.text(i, c / 2, str(c), ha='center', va='center', color='white')
    ax.text(i, c + f / 2, str(f), ha='center', va='center', color='white')
    ax.text(i, c + f + a / 2, str(a), ha='center', va='center', color='white')
    ax.text(i, c + f + a + j / 2, str(j), ha='center', va='center', color='white')

# Adjusting layout for better fit and visuals
plt.tight_layout()

# Show the plot
plt.show()