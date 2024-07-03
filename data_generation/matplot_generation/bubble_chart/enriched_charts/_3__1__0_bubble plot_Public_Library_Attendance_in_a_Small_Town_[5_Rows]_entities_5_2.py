
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Sport': ['Art', 'Art', 'Sculpture', 'Sculpture', 'Photography', 'Photography',
              'Literature', 'Literature', 'Music', 'Music', 'Theater', 'Theater',
              'Dance', 'Dance', 'Fashion', 'Fashion'],
    'Type': ['Brushes', 'Paints', 'Clay', 'Tools', 'Cameras', 'Film',
             'Books', 'Magazines', 'Instruments', 'Accessories', 'Props', 'Costumes',
             'Shoes', 'Clothing', 'Jewelry', 'Clothing'],
    'Revenue': [9000, 15000, 12000, 14000, 20000, 10000,
                18000, 16000, 22000, 11000, 13000, 14000,
                10000, 12000, 20000, 21000],
    'Profit': [3000, 7000, 5000, 6000, 9000, 5000,
               8000, 7000, 10000, 5000, 6000, 7000,
               4000, 5000, 9000, 9500],
    'Units Sold': [150, 200, 250, 300, 400, 250,
                   350, 300, 500, 200, 250, 300,
                   200, 250, 300, 350]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 8))
scatter = ax.scatter(x='Revenue', y='Profit', s=df['Units Sold']*10, alpha=0.6,
                     c=['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD',
                        '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF',
                        '#1A55B3', '#FF5733', '#33FF57', '#FF33D4', '#33FFF6', '#F633FF'], data=df)

ax.set_title('Creative Arts Sales - Revenue vs. Profit by Units Sold', fontsize=18, pad=20)
ax.set_xlabel('Revenue (in USD)', fontsize=14)
ax.set_ylabel('Profit (in USD)', fontsize=14)
plt.grid(True)

for area in [100, 300, 500]:
    plt.scatter([], [], c='grey', alpha=0.5, s=area,
                label=f'{area/10} Units Sold')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Units Sold')

plt.tight_layout()
plt.show()