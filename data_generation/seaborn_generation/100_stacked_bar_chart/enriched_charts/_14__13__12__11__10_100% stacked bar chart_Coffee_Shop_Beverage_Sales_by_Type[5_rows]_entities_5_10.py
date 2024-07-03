
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': '2023-01', 'Fruits': '25%', 'Vegetables': '35%', 'Grains': '15%', 'Dairy': '10%', 'Proteins': '10%', 'Other': '5%'},
    {'Month': '2023-02', 'Fruits': '30%', 'Vegetables': '30%', 'Grains': '10%', 'Dairy': '10%', 'Proteins': '15%', 'Other': '5%'},
    {'Month': '2023-03', 'Fruits': '20%', 'Vegetables': '40%', 'Grains': '15%', 'Dairy': '10%', 'Proteins': '10%', 'Other': '5%'},
    {'Month': '2023-04', 'Fruits': '35%', 'Vegetables': '25%', 'Grains': '10%', 'Dairy': '10%', 'Proteins': '15%', 'Other': '5%'},
    {'Month': '2023-05', 'Fruits': '28%', 'Vegetables': '32%', 'Grains': '12%', 'Dairy': '12%', 'Proteins': '11%', 'Other': '5%'},
    {'Month': '2023-06', 'Fruits': '32%', 'Vegetables': '28%', 'Grains': '10%', 'Dairy': '10%', 'Proteins': '15%', 'Other': '5%'},
    {'Month': '2023-07', 'Fruits': '30%', 'Vegetables': '30%', 'Grains': '15%', 'Dairy': '10%', 'Proteins': '10%', 'Other': '5%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Month':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Category', value_name='Percentage')

df_long['Month'] = pd.to_datetime(df_long['Month'])
df_long.sort_values(by='Month', inplace=True)

categories = df.columns[1:]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#A9A9A9']

left = len(df_long['Month'].unique()) * [0]

fig, ax = plt.subplots(figsize=(14, 8))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Category'] == category]
    plt.bar(
        category_data['Month'].dt.strftime('%Y-%m'),
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
plt.title('Distribution of Food Types Over Time', pad=20)
plt.legend(title='Food Type', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()