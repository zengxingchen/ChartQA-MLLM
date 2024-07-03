
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Word Count': [2500, 2600, 2400, 2700, 2800, 2900, 
                   3000, 3100, 3200, 3300, 3400, 3500],
    'Reading Time': [6, 6.2, 5.8, 6.4, 6.6, 6.8,
                     7, 7.2, 7.4, 7.6, 7.8, 8],
    'Engagement Rate': [75, 76, 73, 77, 78, 79,
                        80, 81, 82, 83, 84, 85]
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
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

# Generating the stacked areas
plt.stackplot(data.index, data['Word Count'], data['Reading Time'], data['Engagement Rate'], 
              labels=['Word Count', 'Reading Time', 'Engagement Rate'], colors=colors)

# Aesthetics
plt.title('Monthly Blog Performance Indicators in 2021', fontsize=20)
plt.ylabel('Values', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Annotating a specific data point
plt.text('December', 3500, 'Highest Word Count', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()