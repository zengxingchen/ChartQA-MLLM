
import matplotlib.pyplot as plt

# Data
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025']
sales = [120, 150, 180, 200, 220, 210, 230, 250, 240, 260, 280, 300]

# Plotting the line chart
plt.figure(figsize=(16, 8))
plt.plot(quarters, sales, marker='o', linestyle='-', color='#3498db', linewidth=3)  # Modify color scheme

# Adding title and labels
plt.title('Quarterly Sales of XYZ Company (2023-2025)', fontsize=20, pad=20)
plt.xlabel('Quarter', fontsize=14)
plt.ylabel('Sales (in thousands)', fontsize=14)

# Adding an annotation for the highest sales
highest_sales_index = sales.index(max(sales))
highest_sales_quarter = quarters[highest_sales_index]
plt.annotate('Highest Sales', xy=(highest_sales_index, max(sales)), xytext=(highest_sales_index, max(sales) + 20),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05), fontsize=12)

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(100, 320)
plt.show()