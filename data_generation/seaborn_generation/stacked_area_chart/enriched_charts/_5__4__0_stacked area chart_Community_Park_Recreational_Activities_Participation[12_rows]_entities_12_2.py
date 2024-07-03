
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Wind': [6500, 6200, 6800, 7000, 7300, 7500, 
             7800, 8000, 8200, 8300, 8500, 8700],
    'Solar': [4800, 5000, 5300, 5200, 5500, 5700,
              5900, 6100, 6000, 6200, 6400, 6600],
    'Hydro': [5600, 5400, 6000, 6200, 6400, 6600,
              6800, 7000, 7100, 7200, 7400, 7600]
})

# Transform data for stacked area plot
data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

# Stacked area plot
plt.figure(figsize=(18, 9))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#FF6347", "#FFD700", "#00FA9A"]

# Generating the stacked areas
plt.stackplot(data.index, data['Wind'], data['Solar'], data['Hydro'], labels=['Wind', 'Solar', 'Hydro'], colors=colors)

# Aesthetics
plt.title('Monthly Renewable Energy Production - 2021', fontsize=20, pad=20)
plt.ylabel('Energy Production (in GWh)', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Annotating a specific data point
plt.text('December', 8700, 'Peak for Wind', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()