
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Concerts': [800, 850, 900, 950, 1000, 1050, 
                 1100, 1150, 1200, 1250, 1300, 1350],
    'Exhibitions': [1200, 1150, 1100, 1050, 1000, 950,
                    900, 850, 800, 750, 700, 650],
    'Workshops': [400, 450, 500, 550, 600, 650,
                  700, 750, 800, 850, 900, 950]
})

data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

plt.figure(figsize=(16, 8))
sns.set_style("whitegrid")

colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

plt.stackplot(data.index, data['Concerts'], data['Exhibitions'], data['Workshops'], labels=['Concerts', 'Exhibitions', 'Workshops'], colors=colors)

plt.title('Monthly Event Attendance - 2021', fontsize=20)
plt.ylabel('Attendance', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

plt.text('June', 1050, 'Mid-year Spike', horizontalalignment='center', color='black')

sns.despine()
plt.show()