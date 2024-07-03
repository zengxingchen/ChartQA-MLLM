
import matplotlib.pyplot as plt

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [120, 130, 140, 150]
product_b = [100, 110, 115, 120]
product_c = [90, 95, 100, 105]
product_d = [80, 85, 88, 90]

# Cumulative values for stacking
cumulative_a = product_a
cumulative_b = [a + b for a, b in zip(cumulative_a, product_b)]
cumulative_c = [b + c for b, c in zip(cumulative_b, product_c)]
cumulative_d = [c + d for c, d in zip(cumulative_c, product_d)]

# Figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Stacked horizontal bar chart - so the 'bottom' parameter changes to 'left'
ax.barh(quarters, product_a, color='#1f77b4', edgecolor='white', height=0.6, label='Product A')
ax.barh(quarters, product_b, left=cumulative_a, color='#ff7f0e', edgecolor='white', height=0.6, label='Product B')
ax.barh(quarters, product_c, left=cumulative_b, color='#2ca02c', edgecolor='white', height=0.6, label='Product C')
ax.barh(quarters, product_d, left=cumulative_c, color='#d62728', edgecolor='white', height=0.6, label='Product D')

# Adding labels and a title, and a legend
ax.set_xlabel('Sales Revenue (in millions)')
ax.set_title('Quarterly Sales Revenue by Product')
ax.legend()

# Adjusting layout for better fit and visuals
plt.tight_layout()

# Show the plot
plt.show()