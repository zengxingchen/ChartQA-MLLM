import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Count': [120, 150, 180, 210, 250, 300, 350, 320, 280, 240, 200, 160]
}
df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(14, 10))
sns.set_theme(style="whitegrid")
area_chart = sns.lineplot(data=df, x='Month', y='Count', sort=False, lw=1, color='#FF5733')

plt.fill_between(x=df['Month'], y1=df['Count'], color='#FFBD33', alpha=0.6)

for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Count'][i]+5, str(df['Count'][i]), horizontalalignment='center', fontsize=10)

area_chart.set_xlabel('Month')
area_chart.set_ylabel('Visitor Count')
area_chart.set_title('Monthly Visitor Count for Museum A', pad=20)

plt.show()