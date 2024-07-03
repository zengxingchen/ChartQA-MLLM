
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Sport': ['Basketball', 'Basketball', 'Soccer', 'Soccer', 'Tennis', 'Tennis',
              'Baseball', 'Baseball', 'Golf', 'Golf', 'Running', 'Cycling',
              'Swimming', 'Swimming', 'Running', 'Cycling'],
    'Type': ['Balls', 'Shoes', 'Balls', 'Shoes', 'Balls', 'Shoes',
             'Balls', 'Shoes', 'Balls', 'Shoes', 'Shoes', 'Shoes',
             'Suits', 'Goggles', 'Suits', 'Helmets'],
    'Revenue': [12000, 14000, 16000, 18000, 8000, 10000, 
                6000, 12000, 15000, 20000, 18000, 22000, 
                10000, 12000, 14000, 16000],
    'Profit': [4000, 5000, 6000, 7000, 3000, 4000, 
               2000, 5000, 5000, 7000, 8000, 9000, 
               3000, 4000, 5000, 6000],
    'Units Sold': [300, 200, 500, 400, 150, 250, 
                   100, 350, 250, 300, 400, 500, 
                   200, 300, 350, 450]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 9))
scatter = ax.scatter(x='Revenue', y='Profit', s=df['Units Sold']*10, alpha=0.6,
                     c=['#FF5733', '#33FF57', '#3357FF', '#FF33D4', '#33FFF6',
                        '#F633FF', '#FF8333', '#33FF83', '#8333FF', '#3357FF',
                        '#57FF33', '#FFD333', '#33FFB5', '#FF33B5', '#B533FF', '#33B5FF'], data=df)

ax.set_title('Sports Equipment Sales - Revenue vs. Profit by Units Sold', fontsize=18)
ax.set_xlabel('Revenue (in USD)', fontsize=14)
ax.set_ylabel('Profit (in USD)', fontsize=14)
plt.grid(True)

for area in [100, 300, 500]:  
    plt.scatter([], [], c='grey', alpha=0.5, s=area,
                label=f'{area/10} Units Sold')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Units Sold')

plt.tight_layout()
plt.show()