
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'DailyVisitors': [
        1500, 1800, 2200, 2500, 2700, 3000,
        3200, 3100, 2900, 2600, 2300, 2000
    ]
}

df = pd.DataFrame(data)

df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
], ordered=True)

plt.figure(figsize=(14, 7))

area_chart = sns.lineplot(data=df, x='Month', y='DailyVisitors', color="#FF5733")
area_chart.fill_between(df['Month'], df['DailyVisitors'], color="#FF5733", alpha=0.3)

for index, value in enumerate(df['DailyVisitors']):
    plt.text(df['Month'][index], value, f"{value}", 
             horizontalalignment='center', size='small', color='black')

plt.title('Monthly Average Daily Visitors', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

plt.show()