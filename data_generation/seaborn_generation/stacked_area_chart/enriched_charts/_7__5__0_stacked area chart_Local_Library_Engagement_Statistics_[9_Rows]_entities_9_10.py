
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Electronics': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230],
    'Furniture': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],
    'Clothing': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Groceries': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(16, 12))
pal = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
plt.stackplot(cumulative.index, cumulative['Electronics'], cumulative['Furniture'],
              cumulative['Clothing'], cumulative['Groceries'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Sales by Product Category', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales (in thousands)')
plt.annotate('Peak for Electronics', xy=(11.2, cumulative.loc['December', 'Electronics']-20),
             xytext=(8, cumulative.loc['December', 'Electronics']+100),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Groceries', xy=(11.2, cumulative.loc['December', 'Groceries']),
             xytext=(6, cumulative.loc['December', 'Groceries'] + cumulative.loc['December', 'Clothing'] + 20),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.tight_layout()
plt.show()