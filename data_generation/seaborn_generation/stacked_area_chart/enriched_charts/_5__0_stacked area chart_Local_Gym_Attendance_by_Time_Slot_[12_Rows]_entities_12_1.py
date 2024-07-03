
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Adventure': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300],
    'Destinations': [3000, 3100, 3300, 3500, 3600, 3800, 3900, 4100, 4200, 4400, 4500, 4700],
    'Travel Tips': [2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600],
    'Reviews': [1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#ff6f69","#ffcc5c","#88d8b0","#6b5b95"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Category', value_name='Visits')

# Plot
plt.figure(figsize=(16, 8))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(16, 8))

# Customization
plt.title('Monthly Website Visits to Travel Blog Sections', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Visits', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Blog Sections', loc='upper left')

# Annotations
for i, category in enumerate(df.columns[1:]):
    y = df[category].cumsum() - (0.5 * df[category])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{category}', fontsize=10, ha='left', va='center')

plt.tight_layout()
plt.show()