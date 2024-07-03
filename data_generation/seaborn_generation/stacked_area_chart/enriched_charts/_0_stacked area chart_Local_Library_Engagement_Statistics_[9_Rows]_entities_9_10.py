
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Residential': [120, 115, 130, 140, 160, 150, 165, 170, 155, 145, 130, 125],
    'Commercial': [100, 95, 105, 110, 130, 120, 135, 140, 125, 115, 105, 100],
    'Industrial': [150, 145, 160, 165, 175, 170, 180, 185, 175, 165, 155, 150],
    'Transportation': [130, 125, 135, 140, 150, 145, 155, 160, 150, 140, 135, 130]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(12, 8))
pal = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a']
plt.stackplot(cumulative.index, cumulative['Residential'], cumulative['Commercial'],
              cumulative['Industrial'], cumulative['Transportation'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Energy Consumption by Sector')
plt.xlabel('Month')
plt.ylabel('Energy Consumption (in Arbitrary Units)')
plt.annotate('Peak for Residential', xy=(4.8, cumulative.loc['May', 'Residential']-20),
             xytext=(5.5, cumulative.loc['May', 'Residential']+100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Industrial', xy=(7.2, cumulative.loc['August', 'Industrial']),
             xytext=(6.5, cumulative.loc['August', 'Industrial']+100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Transportation', xy=(7.2, cumulative.loc['August', 'Transportation']),
             xytext=(6.5, cumulative.loc['August', 'Transportation'] + cumulative.loc['August', 'Industrial'] + 20),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.tight_layout()
plt.show()