
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
advertising = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
sales = [1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500]
customer_support = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
research_development = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
operations = [700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

bar_height = 0.6

ax.barh(years, advertising, color='#FF5733', edgecolor='white', height=bar_height, label='Advertising')
ax.barh(years, sales, left=advertising, color='#33FF57', edgecolor='white', height=bar_height, label='Sales')
ax.barh(years, customer_support, left=[i+j for i,j in zip(advertising, sales)], color='#3357FF', edgecolor='white', height=bar_height, label='Customer Support')
ax.barh(years, research_development, left=[i+j+k for i,j,k in zip(advertising, sales, customer_support)], color='#FF33A8', edgecolor='white', height=bar_height, label='Research & Development')
ax.barh(years, operations, left=[i+j+k+l for i,j,k,l in zip(advertising, sales, customer_support, research_development)], color='#FFDD33', edgecolor='white', height=bar_height, label='Operations')

ax.set_xlabel('Spending in $1000s')
ax.set_title('Departmental Spending from 2015 to 2025', pad=20)
ax.set_yticks(years)
ax.set_xlim(0, 10000)  # Adjust to accommodate the sum of the data points
ax.legend(loc='upper right')

# Adding numerical labels to each bar
for i in range(len(years)):
    plt.text(advertising[i]/2, i, str(advertising[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(advertising[i] + sales[i]/2, i, str(sales[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(advertising[i] + sales[i] + customer_support[i]/2, i, str(customer_support[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(advertising[i] + sales[i] + customer_support[i] + research_development[i]/2, i, str(research_development[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(advertising[i] + sales[i] + customer_support[i] + research_development[i] + operations[i]/2, i, str(operations[i]), ha='center', va='center', color='black', fontweight='bold')

plt.show()