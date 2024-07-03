
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Event': 'Music Festival', 'Product Development': 30, 'Marketing': 25, 'Sales': 10, 'Customer Support': 15, 'Human Resources': 10, 'Finance': 10},
    {'Event': 'Theater Production', 'Product Development': 20, 'Marketing': 20, 'Sales': 25, 'Customer Support': 15, 'Human Resources': 10, 'Finance': 10},
    {'Event': 'Art Exhibition', 'Product Development': 15, 'Marketing': 10, 'Sales': 20, 'Customer Support': 30, 'Human Resources': 15, 'Finance': 10},
    {'Event': 'Travel Expo', 'Product Development': 25, 'Marketing': 20, 'Sales': 25, 'Customer Support': 10, 'Human Resources': 10, 'Finance': 10},
    {'Event': 'Education Fair', 'Product Development': 20, 'Marketing': 15, 'Sales': 25, 'Customer Support': 15, 'Human Resources': 15, 'Finance': 10},
    {'Event': 'Climate Conference', 'Product Development': 10, 'Marketing': 25, 'Sales': 30, 'Customer Support': 15, 'Human Resources': 10, 'Finance': 10},
    {'Event': 'Business Summit', 'Product Development': 35, 'Marketing': 20, 'Sales': 15, 'Customer Support': 10, 'Human Resources': 10, 'Finance': 10}
]

df = pd.DataFrame(data)
df = df.set_index('Event')

cumulative_sum = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(10, 14))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.5)
    bottom = cumulative_sum[column]

ax.legend(title='Department Allocation', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Event Type')
ax.set_title('Resource Allocation by Department in Various Events')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()