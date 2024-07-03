
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['Marathon', 'Yoga Retreat', 'Fitness Bootcamp', 'Cycling Event', 'CrossFit Competition', 
                 'Swim Meet', 'Dance Workshop', 'Tennis Tournament', 'Hiking Expedition', 'Gymnastics Showcase', 
                 'Soccer League', 'Basketball Tournament', 'Boxing Match', 'Triathlon', 'Martial Arts Expo', 
                 'Climbing Challenge'],
    'Type': ['Running', 'Wellness', 'Training', 'Biking', 'Strength', 'Swimming', 'Dance', 'Tennis', 'Hiking', 
             'Gymnastics', 'Soccer', 'Basketball', 'Boxing', 'Triathlon', 'Martial Arts', 'Climbing'],
    'Participants': [50000, 10000, 15000, 30000, 20000, 25000, 12000, 18000, 8000, 10000, 35000, 30000, 22000, 
                     18000, 14000, 9000],
    'Funding': [700000, 150000, 200000, 400000, 300000, 350000, 180000, 270000, 120000, 150000, 500000, 450000, 
                320000, 270000, 200000, 130000],
    'Expenses': [600000, 100000, 150000, 350000, 250000, 300000, 140000, 230000, 90000, 120000, 450000, 400000, 
                 280000, 220000, 160000, 110000],
    'Impact': [90, 80, 85, 88, 75, 83, 78, 80, 70, 85, 95, 92, 85, 88, 82, 75]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(20, 12))
scatter = ax.scatter(x='Funding', y='Expenses', s=df['Participants']*0.1, alpha=0.6,
                     c=['#ff5733', '#33ff57', '#3357ff', '#f033ff', '#33fff0', 
                        '#ff33a1', '#a1ff33', '#ff8c33', '#5733ff', '#f0ff33', 
                        '#33a1ff', '#33ff8c', '#ff3357', '#a133ff', '#ff5733', '#33ff57'], data=df)

ax.set_title('Sports Events: Funding vs. Expenses by Participants', fontsize=20, pad=20)
ax.set_xlabel('Funding (in USD)', fontsize=16)
ax.set_ylabel('Expenses (in USD)', fontsize=16)
plt.grid(True)

for area in [2000, 5000, 10000]:  
    plt.scatter([], [], c='grey', alpha=0.5, s=area,
                label=f'{area} Participants')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Participants')

plt.tight_layout()
plt.show()