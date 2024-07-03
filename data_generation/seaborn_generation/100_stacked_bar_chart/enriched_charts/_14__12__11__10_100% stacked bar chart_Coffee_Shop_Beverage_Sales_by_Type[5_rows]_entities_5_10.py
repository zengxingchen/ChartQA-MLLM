
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Adventure': '30%', 'Leisure': '25%', 'Cultural': '20%', 'Wildlife': '15%', 'Beach': '10%'},
    {'Date': '2023-02-01', 'Adventure': '35%', 'Leisure': '20%', 'Cultural': '25%', 'Wildlife': '10%', 'Beach': '10%'},
    {'Date': '2023-03-01', 'Adventure': '28%', 'Leisure': '22%', 'Cultural': '30%', 'Wildlife': '10%', 'Beach': '10%'},
    {'Date': '2023-04-01', 'Adventure': '33%', 'Leisure': '25%', 'Cultural': '20%', 'Wildlife': '12%', 'Beach': '10%'},
    {'Date': '2023-05-01', 'Adventure': '27%', 'Leisure': '23%', 'Cultural': '30%', 'Wildlife': '10%', 'Beach': '10%'},
    {'Date': '2023-06-01', 'Adventure': '30%', 'Leisure': '24%', 'Cultural': '26%', 'Wildlife': '10%', 'Beach': '10%'},
    {'Date': '2023-07-01', 'Adventure': '29%', 'Leisure': '25%', 'Cultural': '25%', 'Wildlife': '11%', 'Beach': '10%'},
    {'Date': '2023-08-01', 'Adventure': '32%', 'Leisure': '20%', 'Cultural': '25%', 'Wildlife': '13%', 'Beach': '10%'},
    {'Date': '2023-09-01', 'Adventure': '31%', 'Leisure': '21%', 'Cultural': '26%', 'Wildlife': '12%', 'Beach': '10%'},
    {'Date': '2023-10-01', 'Adventure': '34%', 'Leisure': '23%', 'Cultural': '22%', 'Wildlife': '11%', 'Beach': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Date', var_name='Type of Travel', value_name='Percentage')

df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

categories = df.columns[1:]
colors = ['#FF6347', '#FFD700', '#1E90FF', '#32CD32', '#FF69B4']

fig, ax = plt.subplots(figsize=(14, 10))

left = len(df_long['Date'].unique()) * [0]

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Type of Travel'] == category]
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
plt.title('Travel Preferences Over Time', pad=20)
plt.legend(title='Type of Travel', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()