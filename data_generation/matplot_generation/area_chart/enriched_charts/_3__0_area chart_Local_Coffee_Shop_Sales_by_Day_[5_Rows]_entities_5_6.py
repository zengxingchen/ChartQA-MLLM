
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'AverageSteps': [8000, 7500, 9000, 10000, 12000, 13000, 15000, 14000, 11000, 9500, 8500, 7000]
}
df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(14, 10))
sns.set_theme(style="whitegrid")
area_chart = sns.lineplot(data=df, x='Month', y='AverageSteps', sort=False, lw=1.5, color='#FF5733')

plt.fill_between(x=df['Month'], y1=df['AverageSteps'], color='#FFBD69', alpha=0.6)

for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['AverageSteps'][i] + 200, str(df['AverageSteps'][i]), horizontalalignment='center')

area_chart.set_xlabel('Month')
area_chart.set_ylabel('Average Steps')
area_chart.set_title('Monthly Average Step Count in 2023', fontsize=16)

plt.show()