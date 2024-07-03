
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['Museum', 'Library', 'Park', 'Gallery', 'Zoo', 'Theater', 'Stadium', 'Cinema',
                 'Beach', 'Historic Site', 'Festival', 'Aquarium', 'Botanical Garden', 'Amusement Park',
                 'Planetarium', 'Science Center'],
    'Type': ['Exhibits', 'Books', 'Events', 'Artworks', 'Animals', 'Performances', 'Sports', 'Movies',
             'Recreation', 'Tours', 'Concerts', 'Marine Life', 'Flora', 'Rides', 'Shows', 'Interactive'],
    'Visitors': [20000, 15000, 25000, 10000, 22000, 18000, 27000, 19000,
                 23000, 16000, 30000, 21000, 24000, 28000, 17000, 20000],
    'Revenue': [300000, 200000, 100000, 150000, 250000, 220000, 300000, 180000,
                50000, 140000, 250000, 200000, 110000, 350000, 190000, 210000],
    'Expenditure': [250000, 150000, 50000, 100000, 200000, 170000, 200000, 130000,
                    20000, 90000, 150000, 160000, 60000, 280000, 140000, 160000],
    'Popularity': [80, 70, 90, 60, 85, 75, 95, 72,
                   88, 65, 92, 83, 87, 97, 68, 80]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(18, 10))
scatter = ax.scatter(x='Revenue', y='Expenditure', s=df['Visitors']*0.1, alpha=0.6,
                     c=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                        '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94'], data=df)

ax.set_title('Visitor Attractions: Revenue vs. Expenditure by Visitors', fontsize=18, pad=20)
ax.set_xlabel('Revenue (in USD)', fontsize=14)
ax.set_ylabel('Expenditure (in USD)', fontsize=14)
plt.grid(True)

for area in [2000, 5000, 10000]:  
    plt.scatter([], [], c='grey', alpha=0.5, s=area,
                label=f'{area} Visitors')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Visitors')

plt.tight_layout()
plt.show()