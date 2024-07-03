
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Exercise': '20%', 'Reading': '25%', 'Social Media': '30%', 'Meditation': '15%', 'Sleep': '10%'},
    {'Date': '2023-02-01', 'Exercise': '22%', 'Reading': '23%', 'Social Media': '28%', 'Meditation': '17%', 'Sleep': '10%'},
    {'Date': '2023-03-01', 'Exercise': '24%', 'Reading': '21%', 'Social Media': '26%', 'Meditation': '19%', 'Sleep': '10%'},
    {'Date': '2023-04-01', 'Exercise': '26%', 'Reading': '20%', 'Social Media': '24%', 'Meditation': '20%', 'Sleep': '10%'},
    {'Date': '2023-05-01', 'Exercise': '27%', 'Reading': '19%', 'Social Media': '23%', 'Meditation': '21%', 'Sleep': '10%'},
    {'Date': '2023-06-01', 'Exercise': '25%', 'Reading': '18%', 'Social Media': '22%', 'Meditation': '25%', 'Sleep': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Date', var_name='Activity', value_name='Percentage')

df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

categories = df.columns[1:]
colors = ['#FFA07A', '#20B2AA', '#778899', '#9370DB', '#FFD700']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(10, 12))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Activity'] == category]
    plt.bar(
        category_data['Date'].dt.strftime('%Y-%m-%d'),
        category_data['Percentage'],
        width=0.5,
        bottom=left,
        color=colors[ix],
        edgecolor="white",
        label=category
    )
    left = left + category_data['Percentage'].values

plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.25, 0.5, 0.75, 1], labels=['0%', '25%', '50%', '75%', '100%'])
plt.ylabel('Percentage')
plt.title('Daily Activity Distribution Over Time (Health & Psychology)')
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()