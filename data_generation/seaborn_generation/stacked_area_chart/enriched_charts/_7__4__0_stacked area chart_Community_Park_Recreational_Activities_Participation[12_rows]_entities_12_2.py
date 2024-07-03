
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Soccer': [4500, 4800, 5000, 5200, 5400, 5600, 
               5800, 6000, 6200, 6400, 6600, 6800],
    'Basketball': [5200, 5000, 5300, 5100, 5200, 5300, 
                   5400, 5500, 5600, 5700, 5800, 5900],
    'Swimming': [6100, 6200, 6300, 6400, 6500, 6600, 
                 6700, 6800, 6900, 7000, 7100, 7200]
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
colors = ["#0072B2", "#E69F00", "#56B4E9"]

# Generating the stacked areas
plt.stackplot(data.index, data['Soccer'], data['Basketball'], data['Swimming'], labels=['Soccer', 'Basketball', 'Swimming'], colors=colors)

# Aesthetics
plt.title('Monthly Sports Activity Data - 2021', fontsize=20)
plt.ylabel('Participation (in numbers)', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Annotating a specific data point
plt.text('December', 7200, 'Peak for Swimming', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()