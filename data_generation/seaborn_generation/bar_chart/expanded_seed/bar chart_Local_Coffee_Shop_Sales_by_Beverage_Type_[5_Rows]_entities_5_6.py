
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Here is the provided data as a list of dictionaries
data = [
    {'Beverage Type': 'Espresso', 'Mon': 75, 'Tue': 60, 'Wed': 90, 'Thu': 55, 'Fri': 85},
    {'Beverage Type': 'Cappuccino', 'Mon': 50, 'Tue': 45, 'Wed': 60, 'Thu': 40, 'Fri': 75},
    {'Beverage Type': 'Latte', 'Mon': 85, 'Tue': 70, 'Wed': 95, 'Thu': 80, 'Fri': 100},
    {'Beverage Type': 'American', 'Mon': 40, 'Tue': 35, 'Wed': 50, 'Thu': 30, 'Fri': 60},
    {'Beverage Type': 'Tea', 'Mon': 30, 'Tue': 25, 'Wed': 35, 'Thu': 20, 'Fri': 40}
]

# Convert into a pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame so that days are along one axis and numbers along another
df_melted = df.melt(id_vars='Beverage Type', var_name='Day', value_name='Sales')

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# Create the bar plot using seaborn
sns.barplot(x='Day', y='Sales', hue='Beverage Type', data=df_melted, palette='viridis')

# Add some additional visual style
sns.despine()
plt.title('Weekly Beverage Sales by Type')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Beverages Sold')
plt.legend(title='Beverage Type')

# Show the plot
plt.show()