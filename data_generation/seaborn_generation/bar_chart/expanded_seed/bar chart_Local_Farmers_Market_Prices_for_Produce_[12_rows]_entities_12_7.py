
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [{'Produce': 'Apples (per lb)', 'Price Last Month': 1.2, 'Price This Month': 1.3, 'Price Change (%)': 8.3},
        {'Produce': 'Bananas (per lb)', 'Price Last Month': 0.6, 'Price This Month': 0.55, 'Price Change (%)': -8.3},
        {'Produce': 'Tomatoes (per lb)', 'Price Last Month': 2.0, 'Price This Month': 1.8, 'Price Change (%)': -10.0},
        {'Produce': 'Carrots (per lb)', 'Price Last Month': 0.9, 'Price This Month': 0.95, 'Price Change (%)': 5.6},
        {'Produce': 'Lettuce (per head)', 'Price Last Month': 1.0, 'Price This Month': 1.1, 'Price Change (%)': 10.0},
        {'Produce': 'Oranges (per lb)', 'Price Last Month': 1.1, 'Price This Month': 1.2, 'Price Change (%)': 9.1},
        {'Produce': 'Strawberries (per lb)', 'Price Last Month': 2.5, 'Price This Month': 2.4, 'Price Change (%)': -4.0},
        {'Produce': 'Blueberries (per lb)', 'Price Last Month': 3.0, 'Price This Month': 2.8, 'Price Change (%)': -6.7},
        {'Produce': 'Cucumbers (each)', 'Price Last Month': 0.75, 'Price This Month': 0.8, 'Price Change (%)': 6.7},
        {'Produce': 'Peppers (per lb)', 'Price Last Month': 2.2, 'Price This Month': 2.1, 'Price Change (%)': -4.5},
        {'Produce': 'Onions (per lb)', 'Price Last Month': 0.7, 'Price This Month': 0.65, 'Price Change (%)': -7.1},
        {'Produce': 'Potatoes (per lb)', 'Price Last Month': 0.5, 'Price This Month': 0.45, 'Price Change (%)': -10.0}]

# Convert data to DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Creating a bar chart
plt.figure(figsize=(10, 8))
barplot = sns.barplot(x='Produce', y='Price Change (%)', data=df, palette='vlag')

# Add labels to the bars
for index, row in df.iterrows():
    barplot.text(index, row['Price Change (%)'], round(row['Price Change (%)'], 2), color='black', ha="center", va='bottom' if row['Price Change (%)'] > 0 else 'top')

# Enhance the plot with customizations
barplot.set_xticklabels(barplot.get_xticklabels(), rotation=45, horizontalalignment='right')
sns.despine(bottom=True, left=True)
plt.title('Produce Price Change From Last Month to This Month')
plt.xlabel('Type of Produce')
plt.ylabel('Price Change (%)')
plt.tight_layout()

# Display the plot
plt.show()