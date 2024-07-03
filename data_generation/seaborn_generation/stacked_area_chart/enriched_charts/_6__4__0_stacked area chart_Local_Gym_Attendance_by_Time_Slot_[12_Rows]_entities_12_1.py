
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Steps': [10000, 9500, 10500, 10300, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500],
    'Calories Burned': [2200, 2100, 2300, 2250, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750],
    'Active Minutes': [150, 145, 155, 153, 160, 165, 170, 175, 180, 185, 190, 195],
    'Heart Rate': [70, 68, 72, 71, 75, 76, 78, 80, 82, 84, 85, 88],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Metric', value_name='Amount')

# Plot
plt.figure(figsize=(14, 7))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(14, 7))

# Customization
plt.title('Monthly Fitness Metrics', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Amount', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Metrics', loc='upper left')

# Annotations
for i, metric in enumerate(df.columns[1:]):
    y = df[metric].cumsum() - (0.5 * df[metric])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{metric}', fontsize=10, ha='left', va='center')

plt.tight_layout()
plt.show()