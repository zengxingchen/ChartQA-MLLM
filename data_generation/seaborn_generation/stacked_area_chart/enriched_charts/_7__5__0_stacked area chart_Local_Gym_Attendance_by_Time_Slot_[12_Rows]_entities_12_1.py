
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Healthy Recipes': [1200, 1350, 1450, 1550, 1600, 1750, 1850, 1950, 2050, 2200, 2300, 2450],
    'Diet Plans': [3000, 3150, 3300, 3500, 3650, 3800, 3950, 4100, 4250, 4400, 4550, 4700],
    'Nutritional Facts': [2500, 2650, 2750, 2900, 3000, 3100, 3250, 3350, 3500, 3650, 3750, 3900],
    'Exercise Routines': [1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#8e44ad","#2980b9","#27ae60","#f39c12"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Category', value_name='Visits')

# Plot
plt.figure(figsize=(18, 9))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(18, 9))

# Customization
plt.title('Monthly Website Visits to Health & Fitness Blog Sections', fontsize=20, pad=20)
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