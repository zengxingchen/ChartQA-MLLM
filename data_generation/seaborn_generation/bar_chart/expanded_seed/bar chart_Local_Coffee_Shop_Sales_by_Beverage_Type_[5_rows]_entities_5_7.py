
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Your initial data in wide-form
data = [
    {'Beverage': 'Espresso', 'Monday': 75, 'Tuesday': 80, 'Wednesday': 65, 'Thursday': 70, 'Friday': 90},
    {'Beverage': 'Latte', 'Monday': 120, 'Tuesday': 110, 'Wednesday': 130, 'Thursday': 140, 'Friday': 160},
    {'Beverage': 'Cappuccino', 'Monday': 90, 'Tuesday': 85, 'Wednesday': 70, 'Thursday': 95, 'Friday': 100},
    {'Beverage': 'Iced Coffee', 'Monday': 60, 'Tuesday': 75, 'Wednesday': 80, 'Thursday': 85, 'Friday': 95},
    {'Beverage': 'Tea', 'Monday': 50, 'Tuesday': 45, 'Wednesday': 55, 'Thursday': 60, 'Friday': 70}
]

# Convert wide-form data into long-form
df = pd.DataFrame(data)
df_long = pd.melt(df, id_vars=['Beverage'], var_name='Day', value_name='Sales')

# Create a bar chart with diversified visual encoding
plt.figure(figsize=(10, 8))
barplot = sns.barplot(x='Day', y='Sales', hue='Beverage', data=df_long, palette='pastel', edgecolor='0.2')

# Additional visual customization (e.g., adding value labels on top of the bars)
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.1f'), 
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha = 'center', va = 'center', 
                     xytext = (0, 9), 
                     textcoords = 'offset points')

plt.title('Weekly Beverage Sales')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Beverages Sold')
plt.legend(title='Beverage', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()