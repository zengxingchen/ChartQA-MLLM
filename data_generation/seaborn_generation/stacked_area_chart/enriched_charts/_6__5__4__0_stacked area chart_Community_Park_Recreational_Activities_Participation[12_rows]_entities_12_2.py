
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Product_A': [3000, 3500, 3300, 3600, 3800, 4000, 
                  4200, 4400, 4600, 4800, 5000, 5200],
    'Product_B': [2000, 2100, 2200, 2300, 2400, 2500,
                  2600, 2700, 2800, 2900, 3000, 3100],
    'Product_C': [4000, 4200, 4100, 4500, 4600, 4700,
                  4800, 4900, 5000, 5100, 5200, 5300]
})

# Transform data for stacked area plot
data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

# Stacked area plot
plt.figure(figsize=(20, 10))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

# Generating the stacked areas
plt.stackplot(data.index, data['Product_A'], data['Product_B'], data['Product_C'], labels=['Product A', 'Product B', 'Product C'], colors=colors)

# Aesthetics
plt.title('Monthly Sales Revenue - 2021', fontsize=22, pad=30)
plt.ylabel('Revenue (in $1000s)', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

# Annotating a specific data point
plt.text('December', 5300, 'Peak for Product C', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()