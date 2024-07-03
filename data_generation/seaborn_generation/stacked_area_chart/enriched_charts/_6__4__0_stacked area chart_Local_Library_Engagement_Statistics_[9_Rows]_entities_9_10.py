
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Fruits': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Vegetables': [130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240],
    'Grains': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230],
    'Protein': [140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

cumulative = df.cumsum(axis=1)

plt.figure(figsize=(16, 12))
colors = ['#FFA07A', '#20B2AA', '#778899', '#FF6347']
plt.stackplot(cumulative.index, cumulative['Fruits'], cumulative['Vegetables'],
              cumulative['Grains'], cumulative['Protein'], labels=cumulative.columns, colors=colors)
plt.legend(loc='upper left')
plt.title('Monthly Food Consumption by Type', fontsize=18, pad=20)
plt.xlabel('Month')
plt.ylabel('Consumption (in kg)')

plt.annotate('Peak for Fruits', xy=(11, cumulative.loc['December', 'Fruits']),
             xytext=(11, cumulative.loc['December', 'Fruits'] + 100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Vegetables', xy=(11, cumulative.loc['December', 'Vegetables']),
             xytext=(11, cumulative.loc['December', 'Vegetables'] + cumulative.loc['December', 'Fruits'] + 100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Grains', xy=(11, cumulative.loc['December', 'Grains']),
             xytext=(11, cumulative.loc['December', 'Grains'] + cumulative.loc['December', 'Vegetables'] + cumulative.loc['December', 'Fruits'] + 100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))

plt.tight_layout()
plt.show()