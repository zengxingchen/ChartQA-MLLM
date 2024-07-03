
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'GDP Growth': [3.1, 3.0, 3.2, 3.4, 3.5, 3.6, 
                   3.7, 3.8, 3.9, 4.0, 4.1, 4.2],
    'Inflation Rate': [2.5, 2.6, 2.7, 2.8, 2.9, 3.0,
                       3.1, 3.2, 3.3, 3.4, 3.5, 3.6],
    'Unemployment Rate': [4.0, 3.9, 3.8, 3.7, 3.6, 3.5,
                          3.4, 3.3, 3.2, 3.1, 3.0, 2.9]
})

# Transform data for stacked area plot
data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

# Stacked area plot
plt.figure(figsize=(18, 10))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#3498db", "#e74c3c", "#2ecc71"]

# Generating the stacked areas
plt.stackplot(data.index, data['GDP Growth'], data['Inflation Rate'], data['Unemployment Rate'], labels=['GDP Growth', 'Inflation Rate', 'Unemployment Rate'], colors=colors)

# Aesthetics
plt.title('Economic Indicators Over 2021', fontsize=20)
plt.ylabel('Percentage (%)', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

# Annotating a specific data point
plt.text('December', 4.2, 'Peak GDP Growth', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()