
import matplotlib.pyplot as plt

# Data from the table
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
product_a = [1400, 1700, 2000, 1800, 2200, 2400, 2300, 2200]
product_b = [900, 1100, 1300, 1200, 1400, 1500, 1600, 1700]
product_c = [1600, 1800, 1900, 1700, 2000, 1800, 2100, 1900]
product_d = [700, 600, 800, 900, 1000, 1100, 1200, 1300]

# Stacked bar data preparation
bar_width = 0.35
indices = range(len(quarters))

# Plotting
fig, ax = plt.subplots(figsize=(16, 10))

ax.bar(indices, product_a, width=bar_width, color='#ff9999', label='Product A')
ax.bar(indices, product_b, width=bar_width, bottom=product_a, color='#66b3ff', label='Product B')
ax.bar(indices, product_c, width=bar_width, bottom=[i+j for i,j in zip(product_a, product_b)], color='#99ff99', label='Product C')
ax.bar(indices, product_d, width=bar_width, bottom=[i+j+k for i,j,k in zip(product_a, product_b, product_c)], color='#ffcc99', label='Product D')

# Labels and Titles
ax.set_ylabel('Sales in Units')
ax.set_title('Quarterly Sales Data by Product', pad=20)
ax.set_xticks(indices)
ax.set_xticklabels(quarters)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Remove the spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Grid lines
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Show plot
plt.tight_layout()
plt.show()