
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)

# Create a data frame with fake data
df = pd.DataFrame({
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Fashion', 'Fashion', 'Fashion', 'Home', 'Home', 'Home', 'Books', 'Books', 'Books', 'Books', 'Sports', 'Sports', 'Sports', 'Sports', 'Food', 'Food', 'Food', 'Food'],
    'sub_category': ['Smartphones', 'TVs', 'Smart Watches', 'Laptops', 'Clothing', 'Shoes', 'Accessories', 'Kitchen', 'Furniture', 'Decor', 'Fiction', 'Non-Fiction', 'Children', 'Educational', 'Cycling', 'Running', 'Gym Equipment', 'Swimwear', 'Beverages', 'Snacks', 'Health Foods', 'Confectionery'],
    'value': [1200, 800, 400, 600, 900, 700, 500, 400, 600, 300, 800, 600, 400, 200, 500, 800, 700, 300, 900, 700, 400, 500]
})

# Create a color list
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

# Plot
plt.figure(figsize=(20, 10))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.7)
plt.title('Market Segmentation of Consumer Goods', fontsize=23)
plt.axis('off')
plt.show()