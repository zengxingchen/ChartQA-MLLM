
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Fruit': 'Apples', 'Monday': 45, 'Tuesday': 30, 'Wednesday': 60, 'Thursday': 40, 'Friday': 55, 'Saturday': 85},
    {'Fruit': 'Oranges', 'Monday': 40, 'Tuesday': 35, 'Wednesday': 55, 'Thursday': 25, 'Friday': 50, 'Saturday': 90},
    {'Fruit': 'Bananas', 'Monday': 50, 'Tuesday': 45, 'Wednesday': 65, 'Thursday': 30, 'Friday': 60, 'Saturday': 100},
    {'Fruit': 'Strawberries', 'Monday': 20, 'Tuesday': 25, 'Wednesday': 30, 'Thursday': 35, 'Friday': 45, 'Saturday': 70},
    {'Fruit': 'Grapes', 'Monday': 15, 'Tuesday': 20, 'Wednesday': 25, 'Thursday': 10, 'Friday': 30, 'Saturday': 55},
    {'Fruit': 'Watermelons', 'Monday': 30, 'Tuesday': 22, 'Wednesday': 35, 'Thursday': 28, 'Friday': 40, 'Saturday': 80},
    {'Fruit': 'Blueberries', 'Monday': 10, 'Tuesday': 12, 'Wednesday': 15, 'Thursday': 18, 'Friday': 25, 'Saturday': 45},
    {'Fruit': 'Peaches', 'Monday': 25, 'Tuesday': 18, 'Wednesday': 30, 'Thursday': 22, 'Friday': 35, 'Saturday': 60}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format
df_long = df.melt(id_vars='Fruit', var_name='Day', value_name='Sales')

# Seaborn bar chart
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))
bar_plot = sns.barplot(x='Day', y='Sales', hue='Fruit', data=df_long, palette='viridis')

# Add some customization
plt.title('Fruit Sales by Day', fontsize=20)
plt.xlabel('Day of the Week', fontsize=15)
plt.ylabel('Number of Fruits Sold', fontsize=15)
plt.xticks(rotation=45)
plt.legend(title='Fruit', bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.) 

# Show the plot
plt.tight_layout()
plt.show()