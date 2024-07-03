
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Books': [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340],
    'Movies': [230, 260, 290, 310, 340, 370, 400, 420, 450, 480, 500, 530],
    'Music': [410, 430, 460, 480, 510, 530, 550, 580, 600, 630, 650, 680]
})

data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

plt.figure(figsize=(16, 8))
sns.set_style("whitegrid")

colors = ["#FF6347", "#4682B4", "#3CB371"]

plt.stackplot(data.index, data['Books'], data['Movies'], data['Music'], labels=['Books', 'Movies', 'Music'], colors=colors)

plt.title('Monthly Entertainment Activities - 2023', fontsize=18, pad=20)
plt.ylabel('Number of Activities', fontsize=12)
plt.xlabel('Month', fontsize=12)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.text('August', 500, 'Summer Surge', horizontalalignment='center', color='black')

sns.despine()
plt.show()