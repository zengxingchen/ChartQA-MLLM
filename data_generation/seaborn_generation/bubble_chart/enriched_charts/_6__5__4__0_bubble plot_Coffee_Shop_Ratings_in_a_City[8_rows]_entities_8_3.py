
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Instrument': ['Guitar', 'Piano', 'Violin', 'Drums', 'Flute', 'Saxophone', 'Trumpet', 'Cello', 'Clarinet', 'Harp', 'Trombone', 'Keyboard', 'Oboe', 'Tuba', 'French Horn'],
    'Average_Cost': [1200, 2500, 1800, 2000, 800, 2200, 1500, 3000, 1000, 3500, 1600, 900, 1100, 1900, 2100],
    'Popularity': [85, 95, 70, 60, 65, 75, 80, 90, 55, 50, 70, 60, 75, 80, 85],
    'Sales': [500, 300, 400, 350, 450, 250, 300, 200, 380, 150, 280, 320, 370, 240, 260]
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
bubble = sns.scatterplot(data=df, x='Average_Cost', y='Sales', size='Popularity', hue='Instrument', 
                         palette=['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33', '#A65628', '#F781BF', '#999999', '#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3', '#A6D854', '#FFD92F'], 
                         sizes=(20, 1000), alpha=0.7, edgecolor='w', linewidth=0.5)

plt.title('Musical Instrument Market: Cost vs. Sales Analysis', fontsize=18, pad=20)
plt.xlabel('Average Cost ($)', fontsize=14)
plt.ylabel('Sales (Units)', fontsize=14)

bubble.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Instruments')

plt.show()