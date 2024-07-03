
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Given data
data = [
    {'Category': 'Beverages', 'Item': 'Coffee', 'Sales': 12000},
    {'Category': 'Beverages', 'Item': 'Tea', 'Sales': 3500},
    {'Category': 'Food', 'Item': 'Pastries', 'Sales': 5000},
    {'Category': 'Food', 'Item': 'Sandwiches', 'Sales': 6200},
    {'Category': 'Merchandise', 'Item': 'Mugs', 'Sales': 1500}
]

# Preparing data for the treemap
categories = [item['Category'] for item in data]
items = [item['Item'] for item in data]
sales = [item['Sales'] for item in data]
colors = sns.color_palette('pastel', len(data))

# Here, we're styling with Seaborn
sns.set(style="whitegrid")

plt.figure(figsize=(12, 8))
ax = plt.gca()

# Creating a treemap
squarify.plot(sizes=sales, label=items, color=colors, alpha=0.8, ax=ax)

# Adding titles and labels
plt.title("Sales Treemap")
plt.axis('off')

# Use Seaborn's context manager to apply higher-level stylings temporarily
with sns.axes_style("white"):
    sns.despine(left=True, bottom=True, right=True)

plt.show()