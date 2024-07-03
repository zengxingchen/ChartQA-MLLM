
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Destination': ['Guitar', 'Piano', 'Violin', 'Drums', 'Flute', 'Saxophone', 'Trumpet', 'Cello', 'Clarinet', 'Harp', 'Trombone'],
    'Average_Cost': [1200, 2500, 1800, 2000, 800, 2200, 1500, 3000, 1000, 3500, 1600],
    'Popularity': [85, 95, 70, 60, 65, 75, 80, 90, 55, 50, 70],
    'Sales': [500, 300, 400, 350, 450, 250, 300, 200, 380, 150, 280]
}
df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
bubble = sns.scatterplot(data=df, x='Average_Cost', y='Sales', size='Popularity', hue='Destination', 
                         palette=['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', '#FFFF33', '#33FFFF', '#FF33FF', '#333FFF', '#33FF3F', '#3F33FF'], 
                         sizes=(20, 1000), alpha=0.7, edgecolor='w', linewidth=0.5)

plt.title('Musical Instrument Sales: Cost vs. Sales Popularity Bubble Chart', fontsize=16, pad=20)
plt.xlabel('Average Cost ($)', fontsize=12)
plt.ylabel('Sales (Units)', fontsize=12)

bubble.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Instruments')

plt.show()