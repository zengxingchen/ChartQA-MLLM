
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Fiction': [5500, 5300, 6000, 5800, 6100, 6200, 
                6300, 6400, 6600, 6800, 7000, 7200],
    'Non-Fiction': [7000, 6800, 6400, 6500, 6700, 6900,
                    7100, 7300, 7500, 7700, 7800, 8000],
    'Science': [3000, 3200, 3400, 3500, 3600, 3700,
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
plt.figure(figsize=(16, 8))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

# Generating the stacked areas
plt.stackplot(data.index, data['Fiction'], data['Non-Fiction'], data['Science'], labels=['Fiction', 'Non-Fiction', 'Science'], colors=colors)

# Aesthetics
plt.title('Monthly Book Sales Data - 2021', fontsize=18)
plt.ylabel('Sales (in USD)', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Annotating a specific data point
plt.text('December', 7200, 'Peak for Fiction', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()