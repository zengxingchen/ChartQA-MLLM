
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Shop Location': 'Central Perk', 'Month': 'January', 'Total Customers': 1240, 'Sales Volume (cups)': 3760, 'Top Selling Beverage': 'Espresso', 'Average Price Per Cup ($)': 4.0},
    {'Shop Location': 'Bean There', 'Month': 'January', 'Total Customers': 930, 'Sales Volume (cups)': 2730, 'Top Selling Beverage': 'Americano', 'Average Price Per Cup ($)': 3.5},
    {'Shop Location': 'Latte Da', 'Month': 'January', 'Total Customers': 1120, 'Sales Volume (cups)': 3300, 'Top Selling Beverage': 'Cappuccino', 'Average Price Per Cup ($)': 4.2},
    {'Shop Location': 'The Grind', 'Month': 'January', 'Total Customers': 780, 'Sales Volume (cups)': 2150, 'Top Selling Beverage': 'Latte', 'Average Price Per Cup ($)': 4.5},
    {'Shop Location': 'Central Perk', 'Month': 'February', 'Total Customers': 1100, 'Sales Volume (cups)': 3460, 'Top Selling Beverage': 'Espresso', 'Average Price Per Cup ($)': 4.0},
    {'Shop Location': 'Bean There', 'Month': 'February', 'Total Customers': 870, 'Sales Volume (cups)': 2540, 'Top Selling Beverage': 'Americano', 'Average Price Per Cup ($)': 3.5},
    {'Shop Location': 'Latte Da', 'Month': 'February', 'Total Customers': 1050, 'Sales Volume (cups)': 3140, 'Top Selling Beverage': 'Cappuccino', 'Average Price Per Cup ($)': 4.2},
    {'Shop Location': 'The Grind', 'Month': 'February', 'Total Customers': 740, 'Sales Volume (cups)': 2020, 'Top Selling Beverage': 'Latte', 'Average Price Per Cup ($)': 4.5}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Create bubble chart
plt.figure(figsize=(10, 8))
bubble_chart = sns.scatterplot(
    data=df,
    x='Total Customers',
    y='Average Price Per Cup ($)',
    size='Sales Volume (cups)',
    hue='Shop Location',
    style='Month',
    sizes=(20, 500),
    alpha=0.7,  # setting transparency level
    edgecolor="w",  # setting edge color for the bubbles
    linewidth=1  # setting edge width for the bubbles
)

# Adjust legend
bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.15, 1), borderaxespad=0)
plt.title('Coffee Shop Sales Data (Bubble Chart)')
plt.xlabel('Total Customers')
plt.ylabel('Average Price Per Cup ($)')
plt.grid(True)  # Optional grid
sns.move_legend(bubble_chart, "lower center", bbox_to_anchor=(.5, 1), ncol=3, title=None, frameon=False)

plt.show()