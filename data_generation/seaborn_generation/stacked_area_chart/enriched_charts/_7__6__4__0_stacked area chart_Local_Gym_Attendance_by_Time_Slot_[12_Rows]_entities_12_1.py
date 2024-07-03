
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Books Read': [2, 3, 1, 4, 2, 5, 3, 4, 2, 3, 4, 5],
    'Pages Read': [500, 750, 250, 1000, 500, 1250, 750, 1000, 500, 750, 1000, 1250],
    'Hours Spent': [10, 15, 5, 20, 10, 25, 15, 20, 10, 15, 20, 25],
    'New Words Learned': [20, 25, 10, 35, 20, 40, 25, 30, 20, 25, 35, 40],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Metric', value_name='Amount')

# Plot
plt.figure(figsize=(16, 9))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(16, 9))

# Customization
plt.title('Monthly Reading Metrics', fontsize=22, pad=30)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Amount', fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='Metrics', loc='upper right')

# Annotations
for i, metric in enumerate(df.columns[1:]):
    y = df[metric].cumsum() - (0.5 * df[metric])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{metric}', fontsize=12, ha='left', va='center')

plt.tight_layout()
plt.show()