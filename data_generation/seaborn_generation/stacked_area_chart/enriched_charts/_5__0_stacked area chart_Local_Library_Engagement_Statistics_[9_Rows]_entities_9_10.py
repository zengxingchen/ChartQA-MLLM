
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Primary School': [200, 190, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],
    'Secondary School': [180, 175, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285],
    'Undergraduate': [160, 155, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265],
    'Postgraduate': [140, 135, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(14, 10))
pal = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']
plt.stackplot(cumulative.index, cumulative['Primary School'], cumulative['Secondary School'],
              cumulative['Undergraduate'], cumulative['Postgraduate'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Enrollment by Education Level', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Students')
plt.annotate('Peak for Primary School', xy=(11.2, cumulative.loc['December', 'Primary School']-20),
             xytext=(8, cumulative.loc['December', 'Primary School']+100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Postgraduate', xy=(11.2, cumulative.loc['December', 'Postgraduate']),
             xytext=(6, cumulative.loc['December', 'Postgraduate'] + cumulative.loc['December', 'Undergraduate'] + 20),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.tight_layout()
plt.show()