
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Given chart data
data = [
    {'Item': 'Item 1', 'Coffee (%)': 25, 'Tea (%)': 12, 'Pastries (%)': 20, 'Sandwiches (%)': 10, 'Salads (%)': 8, 'Juices (%)': 5},
    {'Item': 'Item 2', 'Coffee (%)': 18, 'Tea (%)': 15, 'Pastries (%)': 22, 'Sandwiches (%)': 12, 'Salads (%)': 9, 'Juices (%)': 4},
    # ... other items
    {'Item': 'Item 12', 'Coffee (%)': 24, 'Tea (%)': 8, 'Pastries (%)': 22, 'Sandwiches (%)': 10, 'Salads (%)': 9, 'Juices (%)': 7}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to have category percentages in a single column
df_melted = df.melt(id_vars='Item', var_name='Category', value_name='Percentage')

# Pivot the melted data Frame for stacking
df_pivot = df_melted.pivot(index='Item', columns='Category', values='Percentage')

# Normalize the data to sum to 1 (100%)
df_pivot = df_pivot.divide(df_pivot.sum(axis=1), axis=0)

# Generate the bar plots
colors = sns.color_palette("husl", len(df_pivot.columns))
fig, ax = plt.subplots(figsize=(12, 8))

df_pivot.plot(kind='bar', stacked=True, color=colors, ax=ax)

# Customizing the plot
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Item')
ax.set_title('100% Stacked Bar Chart')

# Create a custom legend
handles, labels = ax.get_legend_handles_labels()
# Reverse the labels and handles to match the stack order
ax.legend(reversed(handles), reversed(labels), title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')

# Format to display in percentages
formatter = FuncFormatter(lambda y, _: '{:.0%}'.format(y)) 
ax.yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.show()