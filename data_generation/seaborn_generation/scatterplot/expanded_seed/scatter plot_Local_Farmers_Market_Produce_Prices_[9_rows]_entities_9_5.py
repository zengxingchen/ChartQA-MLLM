
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Produce': 'Tomatoes', 'Price per lb ($)': 2.99, 'Month': 'July'},
    {'Produce': 'Zucchini', 'Price per lb ($)': 1.49, 'Month': 'July'},
    {'Produce': 'Apples', 'Price per lb ($)': 1.99, 'Month': 'October'},
    {'Produce': 'Pumpkins', 'Price per lb ($)': 0.59, 'Month': 'October'},
    {'Produce': 'Strawberries', 'Price per lb ($)': 3.89, 'Month': 'May'},
    {'Produce': 'Peaches', 'Price per lb ($)': 2.49, 'Month': 'June'},
    {'Produce': 'Green Beans', 'Price per lb ($)': 2.29, 'Month': 'July'},
    {'Produce': 'Corn', 'Price per lb ($)': 0.25, 'Month': 'August'},
    {'Produce': 'Sweet Potatoes', 'Price per lb ($)': 1.39, 'Month': 'November'}
]

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(data)

# Create a scatterplot with varied visual encodings using Seaborn
plt.figure(figsize=(10, 8))
scatter = sns.scatterplot(
    x="Month",
    y="Price per lb ($)",
    hue="Month",        # Color points by month
    size="Price per lb ($)",    # Size points by price
    style="Produce",    # Different markers for each produce
    sizes=(20, 200),    # Range of point sizes
    data=df
)

# Improve readability by rotating the x-axis labels
plt.xticks(rotation=45)

# Adding title and labels for clarity
plt.title('Produce Prices by Month')
plt.xlabel('Month')
plt.ylabel('Price per lb ($)')

# Show the legend outside the plot to avoid overlap
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()