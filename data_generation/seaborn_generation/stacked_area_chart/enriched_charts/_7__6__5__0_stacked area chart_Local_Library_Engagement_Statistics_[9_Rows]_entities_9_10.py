
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Stocks': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300],
    'Bonds': [1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650],
    'Real Estate': [1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550],
    'Commodities': [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(14, 10))
pal = ['#4b8bbe', '#e87b2d', '#76c04e', '#d62c1a']
plt.stackplot(cumulative.index, cumulative['Stocks'], cumulative['Bonds'],
              cumulative['Real Estate'], cumulative['Commodities'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Revenue by Financial Sector', pad=20)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.annotate('Peak for Stocks', xy=(11.2, cumulative.loc['December', 'Stocks'] - 50),
             xytext=(8, cumulative.loc['December', 'Stocks'] + 800),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Peak for Commodities', xy=(11.2, cumulative.loc['December', 'Commodities']),
             xytext=(6, cumulative.loc['December', 'Commodities'] + cumulative.loc['December', 'Real Estate'] + 500),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.tight_layout()
plt.show()