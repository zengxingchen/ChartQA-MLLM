
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data preparation
data = [
    {'Month': '2023-01', 'Adventure': '20%', 'Leisure': '30%', 'Historical': '15%', 'Wildlife': '25%', 'Cultural': '10%', 'Other': '0%'},
    {'Month': '2023-02', 'Adventure': '22%', 'Leisure': '28%', 'Historical': '18%', 'Wildlife': '22%', 'Cultural': '10%', 'Other': '0%'},
    {'Month': '2023-03', 'Adventure': '18%', 'Leisure': '32%', 'Historical': '20%', 'Wildlife': '20%', 'Cultural': '10%', 'Other': '0%'},
    {'Month': '2023-04', 'Adventure': '25%', 'Leisure': '25%', 'Historical': '15%', 'Wildlife': '25%', 'Cultural': '10%', 'Other': '0%'},
    {'Month': '2023-05', 'Adventure': '21%', 'Leisure': '27%', 'Historical': '18%', 'Wildlife': '24%', 'Cultural': '10%', 'Other': '0%'},
    {'Month': '2023-06', 'Adventure': '23%', 'Leisure': '30%', 'Historical': '17%', 'Wildlife': '20%', 'Cultural': '10%', 'Other': '0%'},
    {'Month': '2023-07', 'Adventure': '19%', 'Leisure': '29%', 'Historical': '20%', 'Wildlife': '22%', 'Cultural': '10%', 'Other': '0%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Month':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Category', value_name='Percentage')

df_long['Month'] = pd.to_datetime(df_long['Month'])
df_long.sort_values(by='Month', inplace=True)

categories = df.columns[1:]
colors = ['#4CAF50', '#FF9800', '#F44336', '#2196F3', '#9C27B0', '#795548']

left = len(df_long['Month'].unique()) * [0]

fig, ax = plt.subplots(figsize=(12, 10))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Category'] == category]
    plt.bar(
        category_data['Month'].dt.strftime('%Y-%m'),
        category_data['Percentage'],
        width=0.7,
        bottom=left,
        color=colors[ix],
        edgecolor="white",
        label=category
    )
    left = left + category_data['Percentage'].values

plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.25, 0.5, 0.75, 1], labels=['0%', '25%', '50%', '75%', '100%'])
plt.ylabel('Percentage')
plt.title('Distribution of Travel Adventure Types Over Time')
plt.legend(title='Adventure Type', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()