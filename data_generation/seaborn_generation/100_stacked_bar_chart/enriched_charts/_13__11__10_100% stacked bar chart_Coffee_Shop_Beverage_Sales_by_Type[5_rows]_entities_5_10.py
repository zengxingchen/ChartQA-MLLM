
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Product Quality': 0.35, 'Marketing': 0.25, 'Research & Development': 0.15, 'Customer Service': 0.15, 'Logistics': 0.10},
    {'Date': '2023-02-01', 'Product Quality': 0.30, 'Marketing': 0.30, 'Research & Development': 0.10, 'Customer Service': 0.20, 'Logistics': 0.10},
    {'Date': '2023-03-01', 'Product Quality': 0.33, 'Marketing': 0.27, 'Research & Development': 0.20, 'Customer Service': 0.10, 'Logistics': 0.10},
    {'Date': '2023-04-01', 'Product Quality': 0.32, 'Marketing': 0.25, 'Research & Development': 0.18, 'Customer Service': 0.15, 'Logistics': 0.10},
    {'Date': '2023-05-01', 'Product Quality': 0.31, 'Marketing': 0.28, 'Research & Development': 0.17, 'Customer Service': 0.14, 'Logistics': 0.10},
    {'Date': '2023-06-01', 'Product Quality': 0.34, 'Marketing': 0.26, 'Research & Development': 0.16, 'Customer Service': 0.14, 'Logistics': 0.10}
]

df = pd.DataFrame(data)

df_long = df.melt(id_vars='Date', var_name='Department', value_name='Percentage')

df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long.sort_values(by='Date', inplace=True)

categories = df.columns[1:]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFBD33']

left = len(df_long['Date'].unique()) * [0]

fig, ax = plt.subplots(figsize=(12, 8))

for ix, category in enumerate(categories):
    category_data = df_long[df_long['Department'] == category]
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
plt.ylabel('Percentage of Total Budget')
plt.title('Company Budget Allocation Over Time')
plt.legend(title='Department', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()