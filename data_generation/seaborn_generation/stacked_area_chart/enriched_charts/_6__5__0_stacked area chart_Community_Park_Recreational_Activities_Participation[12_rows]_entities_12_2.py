
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Flights': [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
    'Hotels': [700, 680, 660, 640, 620, 600, 580, 560, 540, 520, 500, 480],
    'Restaurants': [300, 320, 350, 380, 410, 440, 470, 500, 530, 560, 590, 620]
})

data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

plt.figure(figsize=(14, 7))
sns.set_style("whitegrid")

colors = ["#4E79A7", "#F28E2B", "#E15759"]

plt.stackplot(data.index, data['Flights'], data['Hotels'], data['Restaurants'], labels=['Flights', 'Hotels', 'Restaurants'], colors=colors)

plt.title('Monthly Tourism Activities - 2023', fontsize=18, pad=20)
plt.ylabel('Number of Activities', fontsize=12)
plt.xlabel('Month', fontsize=12)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.text('July', 750, 'Summer Peak', horizontalalignment='center', color='black')

sns.despine()
plt.show()