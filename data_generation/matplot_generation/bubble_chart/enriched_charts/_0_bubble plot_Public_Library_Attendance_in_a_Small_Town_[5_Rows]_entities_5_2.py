
import matplotlib.pyplot as plt
import pandas as pd

# Creating a DataFrame from the given table data
data = {
    'Region': ['North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia',
               'South America', 'South America', 'Africa', 'Africa', 'Australia', 'Australia'],
    'Product': ['Widget A', 'Widget B', 'Widget A', 'Widget B', 'Widget A', 'Widget B',
                'Widget A', 'Widget B', 'Widget A', 'Widget B', 'Widget A', 'Widget B'],
    'Revenue': [20000, 24000, 22000, 26000, 18000, 30000, 15000, 28000, 8000, 12000, 16000, 22000],
    'Profit': [4000, 7000, 3000, 5000, 2000, 9000, 2500, 6500, 1000, 2000, 3500, 5500],
    'Units Sold': [500, 300, 400, 350, 600, 250, 550, 400, 350, 150, 450, 250]
}

df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))  # Change the width and height of the chart
scatter = ax.scatter(x='Revenue', y='Profit', s=df['Units Sold']*10,  # Multiply units sold by 10 for bubble sizes
                     alpha=0.6, c=['#FF5733', '#33FF57', '#3357FF', '#FF33D4', '#33FFF6',
                                   '#F633FF', '#FF8333', '#33FF83', '#8333FF', '#3357FF',
                                   '#57FF33', '#FFD333'], data=df)

# Customizing the chart
ax.set_title('Global Widget Sales - Revenue vs. Profit by Units Sold', fontsize=16)
ax.set_xlabel('Revenue (in USD)', fontsize=14)
ax.set_ylabel('Profit (in USD)', fontsize=14)
plt.grid(True)

# Adding legend with the size reference for bubbles
for area in [100, 300, 500]:  # Example bubble sizes
    plt.scatter([], [], c='grey', alpha=0.5, s=area,
                label=f'{area/10} Units Sold')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Units Sold')

# Show the plot
plt.tight_layout()
plt.show()