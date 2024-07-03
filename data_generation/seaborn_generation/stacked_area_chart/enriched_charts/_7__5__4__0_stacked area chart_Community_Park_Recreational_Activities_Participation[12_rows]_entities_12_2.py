
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Carbohydrates': [2200, 2100, 2300, 2400, 2500, 2600, 
                      2700, 2800, 2900, 3000, 3100, 3200],
    'Proteins': [1200, 1150, 1250, 1300, 1350, 1400,
                 1450, 1500, 1550, 1600, 1650, 1700],
    'Fats': [900, 850, 950, 1000, 1050, 1100,
             1150, 1200, 1250, 1300, 1350, 1400]
})

# Transform data for stacked area plot
data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

# Stacked area plot
plt.figure(figsize=(16, 10))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#87CEEB", "#FFA07A", "#20B2AA"]

# Generating the stacked areas
plt.stackplot(data.index, data['Carbohydrates'], data['Proteins'], data['Fats'], labels=['Carbohydrates', 'Proteins', 'Fats'], colors=colors)

# Aesthetics
plt.title('Monthly Nutrient Intake - 2021', fontsize=20, pad=20)
plt.ylabel('Nutrient Intake (in grams)', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Annotating a specific data point
plt.text('December', 3200, 'Peak for Carbohydrates', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()