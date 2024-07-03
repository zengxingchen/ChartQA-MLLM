
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Pop': '25%', 'Rock': '30%', 'Jazz': '20%', 'Classical': '15%', 'Hip Hop': '10%'},
    {'Date': '2023-02-01', 'Pop': '28%', 'Rock': '25%', 'Jazz': '22%', 'Classical': '15%', 'Hip Hop': '10%'},
    {'Date': '2023-03-01', 'Pop': '30%', 'Rock': '22%', 'Jazz': '18%', 'Classical': '20%', 'Hip Hop': '10%'},
    {'Date': '2023-04-01', 'Pop': '32%', 'Rock': '20%', 'Jazz': '18%', 'Classical': '20%', 'Hip Hop': '10%'},
    {'Date': '2023-05-01', 'Pop': '35%', 'Rock': '20%', 'Jazz': '15%', 'Classical': '20%', 'Hip Hop': '10%'},
    {'Date': '2023-06-01', 'Pop': '33%', 'Rock': '21%', 'Jazz': '17%', 'Classical': '19%', 'Hip Hop': '10%'},
    {'Date': '2023-07-01', 'Pop': '34%', 'Rock': '22%', 'Jazz': '16%', 'Classical': '18%', 'Hip Hop': '10%'},
    {'Date': '2023-08-01', 'Pop': '36%', 'Rock': '23%', 'Jazz': '15%', 'Classical': '16%', 'Hip Hop': '10%'},
    {'Date': '2023-09-01', 'Pop': '38%', 'Rock': '24%', 'Jazz': '14%', 'Classical': '14%', 'Hip Hop': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Date', var_name='Genre', value_name='Percentage')
df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

categories = df.columns[1:]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(10, 6))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Genre'] == category]
    plt.bar(
        category_data['Date'].dt.strftime('%Y-%m-%d'),
        category_data['Percentage'],
        width=0.8,
        bottom=left,
        color=colors[ix],
        edgecolor="white",
        label=category
    )
    left = left + category_data['Percentage'].values

plt.xticks(rotation=90)
plt.yticks(ticks=[0, 0.25, 0.5, 0.75, 1], labels=['0%', '25%', '50%', '75%', '100%'])
plt.ylabel('Percentage')
plt.title('Music Genre Popularity Over Time', pad=20)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()