
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Destination': 'Tech Start-up', 'Product Development': '35%', 'Marketing': '20%', 'Sales': '15%', 'Customer Support': '10%', 'Human Resources': '10%', 'Finance': '10%'},
    {'Destination': 'Retail Company', 'Product Development': '10%', 'Marketing': '25%', 'Sales': '30%', 'Customer Support': '15%', 'Human Resources': '10%', 'Finance': '10%'},
    {'Destination': 'Healthcare Provider', 'Product Development': '15%', 'Marketing': '10%', 'Sales': '20%', 'Customer Support': '30%', 'Human Resources': '15%', 'Finance': '10%'},
    {'Destination': 'Financial Services', 'Product Development': '20%', 'Marketing': '10%', 'Sales': '25%', 'Customer Support': '15%', 'Human Resources': '20%', 'Finance': '10%'},
    {'Destination': 'Manufacturing', 'Product Development': '25%', 'Marketing': '15%', 'Sales': '20%', 'Customer Support': '10%', 'Human Resources': '15%', 'Finance': '15%'},
    {'Destination': 'Education', 'Product Development': '10%', 'Marketing': '15%', 'Sales': '25%', 'Customer Support': '20%', 'Human Resources': '15%', 'Finance': '15%'},
    {'Destination': 'Non-Profit', 'Product Development': '5%', 'Marketing': '10%', 'Sales': '15%', 'Customer Support': '40%', 'Human Resources': '20%', 'Finance': '10%'}
]

df = pd.DataFrame(data)
df = df.set_index('Destination')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF5733', '#33FF57', '#3357FF', '#F0E68C', '#8A2BE2', '#FF7F50']

fig, ax = plt.subplots(figsize=(14, 10))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.6)
    bottom = cumulative_sum[column]

ax.legend(title='Department Allocation', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Company Type')
ax.set_title('Resource Allocation by Department in Various Companies')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()