
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Flights': [8000, 8500, 9000, 9500, 10000, 10500, 
                11000, 11500, 12000, 12500, 13000, 13500],
    'Hotels': [12000, 11000, 11500, 11800, 12200, 12500,
               12800, 13000, 13300, 13500, 13800, 14000],
    'Activities': [4000, 4500, 4700, 4900, 5100, 5300,
                   5500, 5700, 5900, 6100, 6300, 6500]
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
plt.stackplot(data.index, data['Flights'], data['Hotels'], data['Activities'], labels=['Flights', 'Hotels', 'Activities'], colors=colors)

# Aesthetics
plt.title('Monthly Travel Expenditures - 2023', fontsize=20)
plt.ylabel('Expenditure (in USD)', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Annotating a specific data point
plt.text('July', 20000, 'Summer Peak for Hotels', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()