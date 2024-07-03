
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Beaches': [1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750],
    'Mountains': [1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050],
    'Historical Sites': [1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850],
    'Adventure Parks': [1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Destination', value_name='Visitors')

# Plot
plt.figure(figsize=(20, 12))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.8, figsize=(20, 12))

# Customization
plt.title('Monthly Visitors to Travel Destinations', fontsize=20, loc='right')
plt.xlabel('Month', fontsize=16)
plt.ylabel('Number of Visitors', fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='Destinations', loc='upper left')

# Annotations
for i, destination in enumerate(df.columns[1:]):
    y = df[destination].cumsum() - (0.5 * df[destination])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{destination}', fontsize=12, ha='left', va='center')

plt.tight_layout()
plt.show()