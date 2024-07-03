
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Region': ['North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia',
               'South America', 'South America', 'Africa', 'Africa', 'Australia', 'Australia',
               'North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia'],
    'Designer': ['Designer A', 'Designer B', 'Designer A', 'Designer B', 'Designer A', 'Designer B',
                 'Designer A', 'Designer B', 'Designer A', 'Designer B', 'Designer A', 'Designer B',
                 'Designer C', 'Designer C', 'Designer C', 'Designer C', 'Designer C', 'Designer C'],
    'Revenue': [32000, 34000, 30000, 36000, 25000, 42000, 21000, 38000, 13000, 19000, 18000, 26000,
                29000, 31000, 28000, 23000, 15000, 22000],
    'Profit': [9000, 10000, 8000, 9500, 6000, 12000, 5000, 11000, 3000, 4500, 5500, 7000,
               8000, 8500, 7500, 6000, 3500, 5000],
    'Units Sold': [600, 550, 450, 500, 700, 300, 650, 450, 200, 350, 400, 300,
                   500, 400, 600, 500, 250, 350]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 10))
scatter = ax.scatter(x='Revenue', y='Profit', s=df['Units Sold']*10, 
                     alpha=0.6, c=['#FF5733', '#33FF57', '#3357FF', '#FF33D4', '#33FFF6',
                                   '#F633FF', '#FF8333', '#33FF83', '#8333FF', '#3357FF',
                                   '#57FF33', '#FFD333', '#FF5733', '#33FF57', '#3357FF',
                                   '#FF33D4', '#33FFF6', '#F633FF'], data=df)

ax.set_title('Fashion Designer Sales - Revenue vs. Profit by Units Sold', fontsize=18)
ax.set_xlabel('Revenue (in USD)', fontsize=14)
ax.set_ylabel('Profit (in USD)', fontsize=14)
plt.grid(True)

for area in [100, 300, 500, 700]: 
    plt.scatter([], [], c='grey', alpha=0.5, s=area,
                label=f'{area/10} Units Sold')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Units Sold', loc='upper left')

plt.tight_layout()
plt.show()