
import matplotlib.pyplot as plt

# Data
categories = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']
product_a = [250, 260, 270, 280, 290, 300]
product_b = [200, 210, 220, 230, 240, 250]
product_c = [180, 190, 200, 210, 220, 230]
product_d = [150, 160, 170, 180, 190, 200]
product_e = [130, 140, 150, 160, 170, 180]

# Cumulative values for stacking
cumulative_a = product_a
cumulative_b = [a + b for a, b in zip(cumulative_a, product_b)]
cumulative_c = [b + c for b, c in zip(cumulative_b, product_c)]
cumulative_d = [c + d for c, d in zip(cumulative_c, product_d)]
cumulative_e = [d + e for d, e in zip(cumulative_d, product_e)]

# Figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bar chart
ax.bar(categories, product_a, color='#1f77b4', edgecolor='white', width=0.6, label='Product A')
ax.bar(categories, product_b, bottom=cumulative_a, color='#ff7f0e', edgecolor='white', width=0.6, label='Product B')
ax.bar(categories, product_c, bottom=cumulative_b, color='#2ca02c', edgecolor='white', width=0.6, label='Product C')
ax.bar(categories, product_d, bottom=cumulative_c, color='#d62728', edgecolor='white', width=0.6, label='Product D')
ax.bar(categories, product_e, bottom=cumulative_d, color='#9467bd', edgecolor='white', width=0.6, label='Product E')

# Adding labels and a title, and a legend
ax.set_ylabel('Number of Units Sold')
ax.set_title('Quarterly Sales by Product', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adding numerical labels
for i in range(len(categories)):
    plt.text(i, cumulative_a[i] / 2, str(product_a[i]), ha='center', va='center', color='white')
    plt.text(i, cumulative_a[i] + (product_b[i] / 2), str(product_b[i]), ha='center', va='center', color='white')
    plt.text(i, cumulative_b[i] + (product_c[i] / 2), str(product_c[i]), ha='center', va='center', color='white')
    plt.text(i, cumulative_c[i] + (product_d[i] / 2), str(product_d[i]), ha='center', va='center', color='white')
    plt.text(i, cumulative_d[i] + (product_e[i] / 2), str(product_e[i]), ha='center', va='center', color='white')

# Adjusting layout for better fit and visuals
plt.tight_layout()

# Show the plot
plt.show()