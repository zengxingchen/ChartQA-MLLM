
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Books': [200, 190, 220, 240, 260, 250, 270, 280, 260, 250, 230, 220],
    'Movies': [180, 175, 190, 210, 230, 220, 240, 250, 230, 220, 210, 200],
    'Music': [150, 140, 160, 180, 200, 190, 210, 220, 200, 190, 170, 160],
    'Podcasts': [170, 160, 180, 200, 220, 210, 230, 240, 220, 210, 190, 180]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(14, 10))
pal = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
plt.stackplot(cumulative.index, cumulative['Books'], cumulative['Movies'],
              cumulative['Music'], cumulative['Podcasts'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Media Consumption by Type', fontsize=16, pad=20)
plt.xlabel('Month')
plt.ylabel('Consumption (in Hours)')

# Annotations
plt.annotate('Peak for Books', xy=(7.2, cumulative.loc['August', 'Books']),
             xytext=(8, cumulative.loc['August', 'Books']+100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Movies', xy=(7.2, cumulative.loc['August', 'Movies']),
             xytext=(8, cumulative.loc['August', 'Movies'] + cumulative.loc['August', 'Books'] + 100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Podcasts', xy=(7.2, cumulative.loc['August', 'Podcasts']),
             xytext=(8, cumulative.loc['August', 'Podcasts'] + cumulative.loc['August', 'Music'] + cumulative.loc['August', 'Movies'] + 100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))

plt.tight_layout()
plt.show()