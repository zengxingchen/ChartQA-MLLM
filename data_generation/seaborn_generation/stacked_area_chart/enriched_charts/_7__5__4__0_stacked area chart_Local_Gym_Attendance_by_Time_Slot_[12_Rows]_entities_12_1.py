
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Active Calories': [1200, 1100, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700],
    'Steps': [10000, 9500, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000],
    'Distance (km)': [8.0, 7.5, 8.3, 8.8, 9.2, 9.6, 10.0, 10.5, 11.0, 11.4, 11.8, 12.0],
    'Floors Climbed': [12, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Activity', value_name='Amount')

# Plot
plt.figure(figsize=(14, 8))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(14, 8))

# Customization
plt.title('Monthly Physical Activity Analysis', fontsize=20, pad=25)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Amount', fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='Activity Types', loc='upper left')

# Annotations
for i, activity in enumerate(df.columns[1:]):
    y = df[activity].cumsum() - (0.5 * df[activity])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{activity}', fontsize=12, ha='left', va='center')

plt.tight_layout()
plt.show()