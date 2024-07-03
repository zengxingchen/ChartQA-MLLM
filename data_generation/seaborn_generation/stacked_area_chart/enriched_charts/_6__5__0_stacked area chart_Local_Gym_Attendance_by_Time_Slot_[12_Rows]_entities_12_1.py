
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Astronomy': [2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300],
    'Space Exploration': [3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600],
    'Future Technologies': [4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300],
    'Society Impact': [1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#00429d", "#93c2de", "#ff7f0e", "#d62728"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Category', value_name='Visits')

# Plot
plt.figure(figsize=(18, 10))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(18, 10))

# Customization
plt.title('Monthly Visits to Science & Technology Sections', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Visits', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Sections', loc='upper left')

# Annotations
for i, category in enumerate(df.columns[1:]):
    y = df[category].cumsum() - (0.5 * df[category])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{category}', fontsize=10, ha='left', va='center')

plt.tight_layout()
plt.show()