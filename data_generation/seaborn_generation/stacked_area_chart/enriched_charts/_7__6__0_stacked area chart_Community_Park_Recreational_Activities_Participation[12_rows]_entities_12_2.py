
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Authors': [150, 200, 250, 300, 350, 400, 
                450, 500, 550, 600, 650, 700],
    'Books': [400, 450, 470, 500, 550, 600,
              650, 700, 750, 800, 850, 900],
    'Articles': [1000, 1100, 1200, 1300, 1400, 1500,
                 1600, 1700, 1800, 1900, 2000, 2100]
})

# Transform data for stacked area plot
data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

# Stacked area plot
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#e6194B", "#3cb44b", "#ffe119"]

# Generating the stacked areas
plt.stackplot(data.index, data['Authors'], data['Books'], data['Articles'], labels=['Authors', 'Books', 'Articles'], colors=colors)

# Aesthetics
plt.title('Monthly Literature Contributions - 2023', fontsize=20)
plt.ylabel('Contributions (count)', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

# Annotating a specific data point
plt.text('June', 1500, 'Mid-Year Peak for Books', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()