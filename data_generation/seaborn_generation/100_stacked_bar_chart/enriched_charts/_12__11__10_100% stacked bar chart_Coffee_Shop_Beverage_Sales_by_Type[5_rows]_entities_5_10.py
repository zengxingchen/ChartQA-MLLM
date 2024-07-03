
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Technology': '25%', 'Finance': '20%', 'Healthcare': '30%', 'Education': '15%', 'Environment': '10%'},
    {'Date': '2023-02-01', 'Technology': '30%', 'Finance': '25%', 'Healthcare': '20%', 'Education': '15%', 'Environment': '10%'},
    {'Date': '2023-03-01', 'Technology': '28%', 'Finance': '22%', 'Healthcare': '25%', 'Education': '15%', 'Environment': '10%'},
    {'Date': '2023-04-01', 'Technology': '32%', 'Finance': '20%', 'Healthcare': '23%', 'Education': '15%', 'Environment': '10%'},
    {'Date': '2023-05-01', 'Technology': '27%', 'Finance': '25%', 'Healthcare': '20%', 'Education': '18%', 'Environment': '10%'},
    {'Date': '2023-06-01', 'Technology': '29%', 'Finance': '24%', 'Healthcare': '22%', 'Education': '15%', 'Environment': '10%'},
    {'Date': '2023-07-01', 'Technology': '26%', 'Finance': '23%', 'Healthcare': '24%', 'Education': '17%', 'Environment': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Date', var_name='Sector', value_name='Percentage')

df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

categories = df.columns[1:]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(16, 8))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Sector'] == category]
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
plt.title('Sector Distribution Over Time')
plt.legend(title='Sector', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()