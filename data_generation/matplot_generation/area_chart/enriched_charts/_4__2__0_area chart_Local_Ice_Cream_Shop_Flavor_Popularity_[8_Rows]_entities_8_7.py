
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'DailyExerciseMinutes': [
        30, 35, 45, 50, 60, 70,
        75, 72, 65, 55, 40, 35
    ]
}

df = pd.DataFrame(data)

df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
], ordered=True)

plt.figure(figsize=(16, 9))

area_chart = sns.lineplot(data=df, x='Month', y='DailyExerciseMinutes', color="#4B8BBE")
area_chart.fill_between(df['Month'], df['DailyExerciseMinutes'], color="#4B8BBE", alpha=0.3)

for index, value in enumerate(df['DailyExerciseMinutes']):
    plt.text(df['Month'][index], value, f"{value}", 
             horizontalalignment='center', size='small', color='black')

plt.title('Average Daily Exercise Minutes per Month', pad=20)
plt.xlabel('Month')
plt.ylabel('Minutes of Exercise')

plt.show()