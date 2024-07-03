
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Calories': [2200, 2100, 2300, 2250, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750],
    'Proteins': [120, 115, 125, 122, 130, 133, 135, 138, 140, 142, 145, 148],
    'Carbohydrates': [300, 290, 310, 305, 320, 330, 335, 340, 345, 350, 355, 360],
    'Fats': [70, 68, 72, 71, 75, 76, 78, 80, 82, 84, 85, 88],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#6baed6", "#fd8d3c", "#74c476", "#e377c2"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Nutrient', value_name='Amount')

# Plot
plt.figure(figsize=(18, 10))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(18, 10))

# Customization
plt.title('Monthly Nutrient Intake Analysis', fontsize=20, pad=25)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Amount', fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='Nutrient Types', loc='upper left')

# Annotations
for i, nutrient in enumerate(df.columns[1:]):
    y = df[nutrient].cumsum() - (0.5 * df[nutrient])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{nutrient}', fontsize=12, ha='left', va='center')

plt.tight_layout()
plt.show()