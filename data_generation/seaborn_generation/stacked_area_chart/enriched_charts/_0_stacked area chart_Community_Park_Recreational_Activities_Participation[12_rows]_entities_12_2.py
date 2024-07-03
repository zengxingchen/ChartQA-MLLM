
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Electronics': [5000, 5200, 5400, 5600, 5800, 6000, 
                    6200, 6400, 6600, 6800, 7000, 7200],
    'Clothing': [7000, 6800, 6400, 6500, 6700, 6900,
                 7100, 7300, 7500, 7700, 7800, 8000],
    'Furniture': [3000, 3100, 3200, 3300, 3500, 3700,
                  3800, 3900, 4000, 4100, 4300, 4400]
})

# Transform data for stacked area plot
data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

# Stacked area plot
plt.figure(figsize=(14, 7))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#3498db", "#e74c3c", "#2ecc71"]

# Generating the stacked areas
plt.stackplot(data.index, data['Electronics'], data['Clothing'], data['Furniture'], labels=['Electronics', 'Clothing', 'Furniture'], colors=colors)

# Aesthetics
plt.title('Monthly Sales Data - 2021', fontsize=18)
plt.ylabel('Sales (in USD)', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Annotating a specific data point
plt.text('November', 7000, 'Peak for Electronics', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()