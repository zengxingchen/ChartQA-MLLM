
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the data
data = {
    'Category': [
        'Fruits', 'Vegetables', 'Dairy Products', 'Meat', 
        'Seafood', 'Grains', 'Beverages', 'Snacks', 
        'Condiments', 'Bakery', 'Frozen Foods', 'Organic Foods', 
        'Canned Foods', 'Spices'
    ],
    'Value': [
        1200, 900, 850, 780, 670, 950, 1300, 750, 600, 880, 1100, 760, 1200, 890
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', 
    '#FDB462', '#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD', 
    '#CCEBC5', '#FFED6F', '#D53E4F', '#3288BD'
]

# Define size of the figure
plt.figure(figsize=(20, 12))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Value'], label=df['Category'], color=colors, alpha=0.8)

plt.title('Key Categories in Food & Nutrition by Market Value (in Millions)', fontsize=24)
plt.axis('off')
plt.show()