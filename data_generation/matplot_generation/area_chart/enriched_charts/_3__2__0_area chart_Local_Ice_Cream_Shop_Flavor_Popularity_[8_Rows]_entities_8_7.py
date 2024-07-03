
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'MeteorsObserved': [
        50, 45, 60, 55, 70, 65,
        75, 80, 90, 85, 95, 100
    ]
}

df = pd.DataFrame(data)

df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
], ordered=True)

plt.figure(figsize=(16, 8))

area_chart = sns.lineplot(data=df, x='Month', y='MeteorsObserved', color="#4B0082")
area_chart.fill_between(df['Month'], df['MeteorsObserved'], color="#4B0082", alpha=0.3)

for index, value in enumerate(df['MeteorsObserved']):
    plt.text(df['Month'][index], value, f"{value}", 
             horizontalalignment='center', size='small', color='black')

plt.title('Monthly Average Meteors Observed per Night', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Meteors Observed')

plt.show()