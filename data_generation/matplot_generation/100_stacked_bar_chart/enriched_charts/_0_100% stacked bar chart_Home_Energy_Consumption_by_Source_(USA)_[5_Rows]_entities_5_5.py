
import matplotlib.pyplot as plt
import pandas as pd

# Creating DataFrame from the provided dataset
data = {
    'Sector': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
    'Residential': [21, 22, 21, 20, 21, 22, 21, 22, 20, 21],
    'Commercial': [18, 18, 17, 19, 18, 19, 19, 18, 18, 18],
    'Industrial': [32, 31, 32, 33, 32, 30, 31, 31, 33, 32],
    'Transportation': [29, 29, 30, 28, 29, 29, 29, 29, 29, 29]
}

df = pd.DataFrame(data)
df.set_index('Sector', inplace=True)

# Calculating percentage for each category
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))

colors = ['#1D2F6F', '#8390FA', '#6EAF46', '#FAC748']

# Stacking bars horizontally
bottoms = [0] * len(df_percentage)
for i, col in enumerate(df_percentage.columns):
    ax.barh(df_percentage.index, df_percentage[col], left=bottoms, color=colors[i], edgecolor='white', height=0.8)
    bottoms = bottoms + df_percentage[col].values

# Customizing the plot
ax.set_xlabel('Percentage')
ax.set_title('Annual Energy Consumption Share by Sector')
ax.legend(df_percentage.columns, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=len(df_percentage.columns))

# Show the grid behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(True, color='gray', linestyle='dashed', alpha=0.7)

plt.tight_layout()
plt.show()