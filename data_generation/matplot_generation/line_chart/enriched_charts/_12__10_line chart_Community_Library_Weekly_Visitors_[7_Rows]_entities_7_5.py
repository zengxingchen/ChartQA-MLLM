
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': '2023-01', 'Sales': 500},
    {'Month': '2023-02', 'Sales': 480},
    {'Month': '2023-03', 'Sales': 510},
    {'Month': '2023-04', 'Sales': 530},
    {'Month': '2023-05', 'Sales': 560},
    {'Month': '2023-06', 'Sales': 540},
    {'Month': '2023-07', 'Sales': 570},
    {'Month': '2023-08', 'Sales': 580},
    {'Month': '2023-09', 'Sales': 590},
    {'Month': '2023-10', 'Sales': 620},
    {'Month': '2023-11', 'Sales': 610},
    {'Month': '2023-12', 'Sales': 630}
]

# Extracting months and sales data
months = [entry['Month'] for entry in data]
sales = [entry['Sales'] for entry in data]

# Creating the line chart
plt.figure(figsize=(14, 7))
line, = plt.plot(months, sales, color='#228B22', linestyle='-', linewidth=2, marker='o', markerfacecolor='#FFD700', markeredgewidth=2, markersize=8)

# Highlighting the highest sales month
max_sales = max(sales)
max_month = months[sales.index(max_sales)]
plt.annotate(f'Peak\n{max_sales}', xy=(max_month, max_sales), xytext=(max_month, max_sales + 15),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='center')

# Highlighting the lowest sales month
min_sales = min(sales)
min_month = months[sales.index(min_sales)]
plt.annotate(f'Low\n{min_sales}', xy=(min_month, min_sales), xytext=(min_month, min_sales - 20),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='center')

# Aesthetic settings for the chart
plt.title('Monthly Sales Trends in 2023', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (in units)', fontsize=12)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the chart
plt.show()