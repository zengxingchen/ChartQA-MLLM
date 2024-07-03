
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Yoga': [300, 320, 340, 360, 380, 400, 
             420, 440, 460, 480, 500, 520],
    'Gym': [200, 220, 240, 260, 280, 300,
            320, 340, 360, 380, 400, 420],
    'Running': [400, 420, 440, 460, 480, 500,
                520, 540, 560, 580, 600, 620]
})

data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

plt.figure(figsize=(18, 10))
sns.set_style("whitegrid")

colors = ["#FF6347", "#4682B4", "#32CD32"]

plt.stackplot(data.index, data['Yoga'], data['Gym'], data['Running'], labels=['Yoga', 'Gym', 'Running'], colors=colors)

plt.title('Monthly Fitness Activity Attendance - 2021', fontsize=20)
plt.ylabel('Attendance', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.text('July', 500, 'Summer Surge', horizontalalignment='center', color='black')

sns.despine()
plt.show()