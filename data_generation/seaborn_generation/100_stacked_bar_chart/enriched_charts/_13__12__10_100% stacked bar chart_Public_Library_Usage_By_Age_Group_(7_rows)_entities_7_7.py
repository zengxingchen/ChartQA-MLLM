
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Destination': 'Yoga Studio', 'Product Development': '25%', 'Marketing': '20%', 'Sales': '10%', 'Customer Support': '15%', 'Human Resources': '10%', 'Finance': '20%'},
    {'Destination': 'Gym', 'Product Development': '30%', 'Marketing': '15%', 'Sales': '15%', 'Customer Support': '10%', 'Human Resources': '20%', 'Finance': '10%'},
    {'Destination': 'Martial Arts School', 'Product Development': '20%', 'Marketing': '10%', 'Sales': '20%', 'Customer Support': '15%', 'Human Resources': '15%', 'Finance': '20%'},
    {'Destination': 'Dance School', 'Product Development': '15%', 'Marketing': '25%', 'Sales': '10%', 'Customer Support': '20%', 'Human Resources': '15%', 'Finance': '15%'},
    {'Destination': 'Pilates Studio', 'Product Development': '20%', 'Marketing': '15%', 'Sales': '15%', 'Customer Support': '20%', 'Human Resources': '10%', 'Finance': '20%'},
    {'Destination': 'CrossFit Box', 'Product Development': '25%', 'Marketing': '10%', 'Sales': '20%', 'Customer Support': '15%', 'Human Resources': '20%', 'Finance': '10%'},
    {'Destination': 'Personal Training', 'Product Development': '15%', 'Marketing': '20%', 'Sales': '25%', 'Customer Support': '10%', 'Human Resources': '20%', 'Finance': '10%'}
]

df = pd.DataFrame(data)
df = df.set_index('Destination')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#3498DB', '#E74C3C', '#2ECC71', '#F1C40F', '#9B59B6', '#1ABC9C']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.5)
    bottom = cumulative_sum[column]

ax.legend(title='Department Allocation', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Fitness Center Type')
ax.set_title('Resource Allocation by Department in Various Fitness Centers')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()