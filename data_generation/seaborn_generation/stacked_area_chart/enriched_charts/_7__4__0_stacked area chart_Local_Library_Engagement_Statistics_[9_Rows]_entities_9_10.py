
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Running': [50, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    'Cycling': [80, 85, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180],
    'Swimming': [60, 65, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
    'Yoga': [30, 35, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(16, 12))
pal = ['#FF4500', '#1E90FF', '#32CD32', '#FFD700']
plt.stackplot(cumulative.index, cumulative['Running'], cumulative['Cycling'],
              cumulative['Swimming'], cumulative['Yoga'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Sports Activity by Type', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Activity Duration (in Hours)', fontsize=14)

# Annotations
plt.annotate('Peak for Running', xy=(11.2, cumulative.loc['December', 'Running']),
             xytext=(12, cumulative.loc['December', 'Running']+50),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Cycling', xy=(11.2, cumulative.loc['December', 'Cycling']),
             xytext=(12, cumulative.loc['December', 'Cycling'] + cumulative.loc['December', 'Running'] + 50),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Yoga', xy=(11.2, cumulative.loc['December', 'Yoga']),
             xytext=(12, cumulative.loc['December', 'Yoga'] + cumulative.loc['December', 'Swimming'] + cumulative.loc['December', 'Cycling'] + 50),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))

plt.tight_layout()
plt.show()