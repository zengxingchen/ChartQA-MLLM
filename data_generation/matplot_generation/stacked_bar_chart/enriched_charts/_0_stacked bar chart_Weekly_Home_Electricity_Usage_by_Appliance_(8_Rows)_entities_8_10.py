
import matplotlib.pyplot as plt

# Data
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
Q1_sales = [12345, 10234, 9384, 6789, 4567]
Q2_sales = [13678, 11789, 10756, 7890, 5189]
Q3_sales = [14567, 12678, 11678, 8567, 5890]
Q4_sales = [15892, 13456, 12894, 9245, 6378]

# Colors for each quarter
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Figure size
plt.figure(figsize=(10, 8))

# Bar heights (change to width for horizontal bars)
bar_height = 0.15

# Plotting
plt.barh(regions, Q1_sales, color=colors[0], edgecolor='white', height=bar_height, label='Q1 Sales')
plt.barh(regions, Q2_sales, left=Q1_sales, color=colors[1], edgecolor='white', height=bar_height, label='Q2 Sales')
plt.barh(regions, [Q1_sales[i] + Q2_sales[i] for i in range(len(Q3_sales))], color=colors[2], edgecolor='white', height=bar_height, label='Q3 Sales')
plt.barh(regions, [Q1_sales[i] + Q2_sales[i] + Q3_sales[i] for i in range(len(Q4_sales))], color=colors[3], edgecolor='white', height=bar_height, label='Q4 Sales')

# Labels and Title
plt.xlabel('Sales in USD')
plt.title('Company Sales by Region and Quarter')
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()