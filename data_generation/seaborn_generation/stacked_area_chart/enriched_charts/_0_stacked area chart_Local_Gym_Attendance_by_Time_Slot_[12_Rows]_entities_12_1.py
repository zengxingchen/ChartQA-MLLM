
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Electronics': [4000, 4200, 4800, 4600, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400],
    'Clothing': [2000, 2100, 2400, 2200, 3000, 3200, 3400, 3500, 3600, 3700, 3800, 3900],
    'Home Goods': [1000, 1150, 1300, 1250, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850],
    'Books': [500, 600, 700, 650, 750, 800, 850, 900, 950, 1000, 1100, 1200],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#ff9999","#66b3ff","#99ff99","#ffcc99"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Category', value_name='Sales')

# Plot
plt.figure(figsize=(12, 6))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.5, figsize=(14, 7))

# Customization
plt.title('Monthly Sales Data for Various Product Categories', fontsize=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales Amount', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Product Categories')

# Annotations
for i, category in enumerate(df.columns[1:]):
    y = df[category].cumsum() - (0.5 * df[category])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{category}', fontsize=9, ha='left', va='center')

plt.tight_layout()
plt.show()