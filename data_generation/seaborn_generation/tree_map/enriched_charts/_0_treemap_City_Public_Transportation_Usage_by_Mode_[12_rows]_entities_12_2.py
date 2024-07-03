
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Seaborn for improved visuals
import seaborn as sns
sns.set(style="whitegrid")

# Read the data
data = '''
category,sub_category,value
Electronics,Smartphones,300
Electronics,Laptops,200
Electronics,Tablets,150
Home Appliances,Washers,90
Home Appliances,Refrigerators,95
Home Appliances,Dishwashers,60
Fashion,Shirts,180
Fashion,Shoes,140
Fashion,Accessories,110
Books,Fiction,70
Books,Non-Fiction,80
Books,Educational,60
Toys & Games,Puzzles,50
Toys & Games,Board Games,80
Toys & Games,Video Games,200
'''
# Simulate reading a CSV file
from io import StringIO
df = pd.read_csv(StringIO(data))

# Prepare data
sizes = df['value'].values.tolist()
label_texts = df['sub_category'].map(str) + " (" + df['value'].astype(str) + ")"

# Color list
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357',
    '#57FFD5', '#D557FF', '#FFD557', '#FF57D5', '#D5FF57',
    '#5733FF', '#F733FF', '#FF3374', '#74FF33', '#3374FF'
]

# Create a figure and a set of subplots
fig, ax = plt.subplots(1, figsize=(12, 8))

# Squarify: plot a treemap of the data
squarify.plot(sizes=sizes, label=label_texts, color=colors, alpha=.7, ax=ax)

# Remove the axes
plt.axis('off')

# Set the title of the plot
plt.title('Market Share by Product Category', fontsize=18)

# Show
plt.show()