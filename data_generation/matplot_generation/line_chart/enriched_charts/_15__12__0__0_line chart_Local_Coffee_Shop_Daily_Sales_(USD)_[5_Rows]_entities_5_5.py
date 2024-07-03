
import matplotlib.pyplot as plt

# Data
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025']
sales = [300, 280, 260, 250, 230, 210, 200, 180, 160, 140, 120, 100]

# Plotting the line chart
plt.figure(figsize=(14, 7))
plt.plot(quarters, sales, marker='o', linestyle='-', color='#8e44ad', linewidth=3)

# Adding title and labels
plt.title('Quarterly Sales Decline of ABC Company (2023-2025)', fontsize=20, pad=20)
plt.xlabel('Quarter', fontsize=14)
plt.ylabel('Sales (in thousands)', fontsize=14)

# Adding an annotation for the lowest sales
lowest_sales_index = sales.index(min(sales))
lowest_sales_quarter = quarters[lowest_sales_index]
plt.annotate('Lowest Sales', xy=(lowest_sales_index, min(sales)), xytext=(lowest_sales_index, min(sales) - 20),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05), fontsize=12)

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(320, 80)
plt.gca().invert_yaxis()
plt.show()