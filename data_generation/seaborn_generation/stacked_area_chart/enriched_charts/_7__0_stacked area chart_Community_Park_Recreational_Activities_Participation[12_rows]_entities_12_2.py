
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Transportation': [1200, 1100, 1300, 1250, 1400, 1350, 
                       1500, 1450, 1550, 1600, 1700, 1650],
    'Accommodation': [1500, 1450, 1550, 1600, 1650, 1700,
                      1750, 1800, 1850, 1900, 1950, 2000],
    'Food': [800, 900, 850, 950, 1000, 1050,
             1100, 1150, 1200, 1250, 1300, 1350]
})

# Transform data for stacked area plot
data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

# Stacked area plot
plt.figure(figsize=(16, 9))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

# Generating the stacked areas
plt.stackplot(data.index, data['Transportation'], data['Accommodation'], data['Food'], labels=['Transportation', 'Accommodation', 'Food'], colors=colors)

# Aesthetics
plt.title('Monthly Travel Expenses - 2021', fontsize=20, pad=20)
plt.ylabel('Expenses (in USD)', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

# Annotating a specific data point
plt.text('July', 4500, 'Peak Travel Season', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()