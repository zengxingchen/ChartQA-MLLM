
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Python dictionary
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sector A': [300, 320, 350, 310, 300, 360],
    'Sector B': [400, 410, 420, 430, 440, 450],
    'Sector C': [500, 510, 520, 550, 530, 540],
    'Sector D': [200, 220, 230, 240, 250, 260]
}

# Create a DataFrame
df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

# Plotting the stacked area chart
plt.figure(figsize=(12, 8))
pal = ['#FFD700', '#FF8C00', '#1E90FF', '#32CD32']

# Cumulate the values
df_cum = df.cumsum(axis=1)

# Plot the categories in reverse order
category_names = df.columns[::-1]
for i, column in enumerate(category_names):
    sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])

# Fill the area between the lines
for i, column in enumerate(category_names):
    if i == 0:
        sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])
        plt.fill_between(df.index, 0, df_cum[column], facecolor=pal[i], alpha=0.5)
    else:
        sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])
        plt.fill_between(df.index, df_cum[category_names[i - 1]], df_cum[column], facecolor=pal[i], alpha=0.5)

# Add annotations
for i, value in enumerate(df_cum['Sector D']):
    plt.text(i, value + 10, f"{value}", ha='center', va='bottom', fontsize=9)

# Customize the chart
plt.title('Monthly Energy Consumption by Sector', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Energy Consumption (MWh)', fontsize=12)
plt.tight_layout()
plt.show()