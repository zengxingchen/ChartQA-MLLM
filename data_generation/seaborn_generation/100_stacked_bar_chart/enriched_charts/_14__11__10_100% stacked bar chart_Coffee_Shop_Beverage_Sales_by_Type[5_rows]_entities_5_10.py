
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Art Creation': '35%', 'Design Studies': '25%', 'Art History': '15%', 'Digital Art': '15%', 'Traditional Crafts': '10%'},
    {'Date': '2023-02-01', 'Art Creation': '30%', 'Design Studies': '30%', 'Art History': '15%', 'Digital Art': '15%', 'Traditional Crafts': '10%'},
    {'Date': '2023-03-01', 'Art Creation': '32%', 'Design Studies': '28%', 'Art History': '18%', 'Digital Art': '12%', 'Traditional Crafts': '10%'},
    {'Date': '2023-04-01', 'Art Creation': '33%', 'Design Studies': '27%', 'Art History': '17%', 'Digital Art': '13%', 'Traditional Crafts': '10%'},
    {'Date': '2023-05-01', 'Art Creation': '31%', 'Design Studies': '29%', 'Art History': '19%', 'Digital Art': '11%', 'Traditional Crafts': '10%'},
    {'Date': '2023-06-01', 'Art Creation': '34%', 'Design Studies': '26%', 'Art History': '16%', 'Digital Art': '14%', 'Traditional Crafts': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Date', var_name='Activity', value_name='Percentage')
df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

categories = df.columns[1:]
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(12, 8))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Activity'] == category]
    plt.bar(
        category_data['Date'].dt.strftime('%Y-%m-%d'),
        category_data['Percentage'],
        width=0.6,
        bottom=left,
        color=colors[ix],
        edgecolor="white",
        label=category
    )
    left = left + category_data['Percentage'].values

plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.25, 0.5, 0.75, 1], labels=['0%', '25%', '50%', '75%', '100%'])
plt.ylabel('Percentage')
plt.title('Art & Design Activity Distribution Over Time', pad=20)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()