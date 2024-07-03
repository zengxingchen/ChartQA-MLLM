
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Fruits': '30%', 'Vegetables': '20%', 'Meat': '25%', 'Dairy': '15%', 'Grains': '10%'},
    {'Date': '2023-02-01', 'Fruits': '28%', 'Vegetables': '22%', 'Meat': '26%', 'Dairy': '14%', 'Grains': '10%'},
    {'Date': '2023-03-01', 'Fruits': '26%', 'Vegetables': '24%', 'Meat': '24%', 'Dairy': '16%', 'Grains': '10%'},
    {'Date': '2023-04-01', 'Fruits': '25%', 'Vegetables': '25%', 'Meat': '23%', 'Dairy': '17%', 'Grains': '10%'},
    {'Date': '2023-05-01', 'Fruits': '24%', 'Vegetables': '26%', 'Meat': '22%', 'Dairy': '18%', 'Grains': '10%'},
    {'Date': '2023-06-01', 'Fruits': '22%', 'Vegetables': '28%', 'Meat': '20%', 'Dairy': '20%', 'Grains': '10%'}
]

df = pd.DataFrame(data)

for col in df.columns:
    if col != 'Date':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Date', var_name='Category', value_name='Percentage')

df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

categories = df.columns[1:]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC300']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(12, 10))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Category'] == category]
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
plt.title('Monthly Food Consumption Distribution (Food & Nutrition)', pad=20)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()