
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Adventure': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Food & Nutrition': [130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185],
    'Health & Wellness': [140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],
    'Education': [110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(16, 12))
pal = ['#FF7F0E', '#2CA02C', '#1F77B4', '#D62728']
plt.stackplot(cumulative.index, cumulative['Adventure'], cumulative['Food & Nutrition'],
              cumulative['Health & Wellness'], cumulative['Education'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Engagement in Different Activities', fontsize=18, pad=20)
plt.xlabel('Month')
plt.ylabel('Engagement Level')
plt.annotate('Significant Rise in Adventure', xy=(11, cumulative.loc['December', 'Adventure']),
             xytext=(10, cumulative.loc['December', 'Adventure']+300),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Steady Growth in Food & Nutrition', xy=(11, cumulative.loc['December', 'Food & Nutrition']),
             xytext=(10, cumulative.loc['December', 'Food & Nutrition']+150),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.tight_layout()
plt.show()