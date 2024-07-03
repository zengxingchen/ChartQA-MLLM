
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Beaches': [400, 420, 450, 470, 500, 520, 550, 580, 600, 620, 650, 680],
    'Mountains': [350, 340, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450],
    'Cities': [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520],
    'Deserts': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(16, 12))
pal = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
plt.stackplot(cumulative.index, cumulative['Beaches'], cumulative['Mountains'],
              cumulative['Cities'], cumulative['Deserts'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Tourists by Destination Type', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Tourists')
plt.annotate('Peak for Beaches', xy=(11.2, cumulative.loc['December', 'Beaches']-20),
             xytext=(8, cumulative.loc['December', 'Beaches']+200),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Deserts', xy=(11.2, cumulative.loc['December', 'Deserts']),
             xytext=(6, cumulative.loc['December', 'Deserts'] + cumulative.loc['December', 'Cities'] + 100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.tight_layout()
plt.show()