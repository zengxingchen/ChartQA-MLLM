
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Transportation': [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
    'Accommodation': [1200, 1150, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700],
    'Food': [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150],
    'Activities': [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Expense Type', value_name='Amount')

# Plot
plt.figure(figsize=(20, 12))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(20, 12))

# Customization
plt.title('Monthly Travel Expense Analysis', fontsize=24, pad=30)
plt.xlabel('Month', fontsize=18)
plt.ylabel('Amount ($)', fontsize=18)
plt.xticks(rotation=45)
plt.legend(title='Expense Types', loc='upper right')

# Annotations
for i, expense in enumerate(df.columns[1:]):
    y = df[expense].cumsum() - (0.5 * df[expense])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{expense}', fontsize=14, ha='left', va='center')

plt.tight_layout()
plt.show()