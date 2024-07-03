
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Cardio': 0.30, 'Strength Training': 0.25, 'Flexibility': 0.15, 'Team Sports': 0.20, 'Other Activities': 0.10},
    {'Date': '2023-02-01', 'Cardio': 0.28, 'Strength Training': 0.27, 'Flexibility': 0.12, 'Team Sports': 0.22, 'Other Activities': 0.11},
    {'Date': '2023-03-01', 'Cardio': 0.32, 'Strength Training': 0.23, 'Flexibility': 0.18, 'Team Sports': 0.17, 'Other Activities': 0.10},
    {'Date': '2023-04-01', 'Cardio': 0.31, 'Strength Training': 0.24, 'Flexibility': 0.16, 'Team Sports': 0.19, 'Other Activities': 0.10},
    {'Date': '2023-05-01', 'Cardio': 0.29, 'Strength Training': 0.26, 'Flexibility': 0.15, 'Team Sports': 0.20, 'Other Activities': 0.10},
    {'Date': '2023-06-01', 'Cardio': 0.30, 'Strength Training': 0.25, 'Flexibility': 0.14, 'Team Sports': 0.21, 'Other Activities': 0.10}
]

df = pd.DataFrame(data)

df_long = df.melt(id_vars='Date', var_name='Activity', value_name='Percentage')

df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

activities = df.columns[1:]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(14, 10))

for ix, activity in enumerate(activities):
    activity_data = df_long[df_long['Activity'] == activity]
    plt.bar(
        activity_data['Date'].dt.strftime('%Y-%m-%d'),
        activity_data['Percentage'],
        width=0.8,
        bottom=left,
        color=colors[ix],
        edgecolor="white",
        label=activity
    )
    left = left + activity_data['Percentage'].values

plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.25, 0.5, 0.75, 1], labels=['0%', '25%', '50%', '75%', '100%'])
plt.ylabel('Percentage of Total Exercise Time')
plt.title('Monthly Exercise Time Allocation')
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()