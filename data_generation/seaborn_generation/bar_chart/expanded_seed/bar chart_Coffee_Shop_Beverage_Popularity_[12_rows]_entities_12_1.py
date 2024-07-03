
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [
    {'Beverage': 'Espresso', 'Number of Cups Sold (per day)': 90},
    {'Beverage': 'Americano', 'Number of Cups Sold (per day)': 120},
    {'Beverage': 'Cappuccino', 'Number of Cups Sold (per day)': 140},
    {'Beverage': 'Latte', 'Number of Cups Sold (per day)': 160},
    {'Beverage': 'Mocha', 'Number of Cups Sold (per day)': 100},
    {'Beverage': 'Flat White', 'Number of Cups Sold (per day)': 70},
    {'Beverage': 'Iced Coffee', 'Number of Cups Sold (per day)': 150},
    {'Beverage': 'Cold Brew', 'Number of Cups Sold (per day)': 110},
    {'Beverage': 'Hot Chocolate', 'Number of Cups Sold (per day)': 40},
    {'Beverage': 'Tea', 'Number of Cups Sold (per day)': 50},
    {'Beverage': 'Fruit Smoothies', 'Number of Cups Sold (per day)': 60},
    {'Beverage': 'Herbal Tea', 'Number of Cups Sold (per day)': 30}
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 8))
barplot = sns.barplot(
    x='Beverage', 
    y='Number of Cups Sold (per day)', 
    data=df,
    palette='viridis', # Using a different color palette for diversification
    edgecolor='black' # Adding an outline to the bars for more definition
)

# Add labels and title
plt.xlabel('Beverage', fontsize=12)
plt.ylabel('Number of Cups Sold (per day)', fontsize=12)
plt.title('Daily Beverage Sales', fontsize=16)
plt.xticks(rotation=45) # Rotate the x labels to make them readable

# Annotating each bar with the number of cups sold
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.1f'), 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     ha='center', va='center', 
                     xytext=(0, 9), 
                     textcoords='offset points')

# Show the plot
plt.tight_layout() # Adjust the plot to ensure everything fits without overlapping
plt.show()