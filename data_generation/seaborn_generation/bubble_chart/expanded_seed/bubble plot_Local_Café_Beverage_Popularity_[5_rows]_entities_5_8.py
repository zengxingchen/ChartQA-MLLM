
import seaborn as sns
import matplotlib.pyplot as plt

# Provided table data
data = [
    {'Beverage': 'Coffee', 'Price (USD)': 3.0, 'Sales (cups/day)': 150, 'Average Rating (out of 5)': 4.3},
    {'Beverage': 'Tea', 'Price (USD)': 2.5, 'Sales (cups/day)': 90, 'Average Rating (out of 5)': 4.1},
    {'Beverage': 'Smoothie', 'Price (USD)': 4.5, 'Sales (cups/day)': 60, 'Average Rating (out of 5)': 4.7},
    {'Beverage': 'Espresso', 'Price (USD)': 3.5, 'Sales (cups/day)': 70, 'Average Rating (out of 5)': 4.5},
    {'Beverage': 'Water', 'Price (USD)': 1.0, 'Sales (cups/day)': 200, 'Average Rating (out of 5)': 3.9}
]

# Convert the data to a suitable format for Seaborn
import pandas as pd
df = pd.DataFrame(data)

# Set the size context of the plot
sns.set_context("talk")

# Create a bubble chart
plt.figure(figsize=(10, 6))  # set the size of the figure
bubble = sns.scatterplot(data=df, x='Price (USD)', y='Sales (cups/day)', 
                         size='Average Rating (out of 5)', hue='Beverage', sizes=(100, 1000),
                         legend="full", palette="bright")

# Customize the axes and title
plt.title('Beverage Sales, Prices, and Ratings')
plt.xlabel('Price (USD)')
plt.ylabel('Sales (cups/day)')

# Modify the legend
h,l = bubble.get_legend_handles_labels()
plt.legend(h[1:], l[1:], title="Beverages")

# Show the plot
plt.show()