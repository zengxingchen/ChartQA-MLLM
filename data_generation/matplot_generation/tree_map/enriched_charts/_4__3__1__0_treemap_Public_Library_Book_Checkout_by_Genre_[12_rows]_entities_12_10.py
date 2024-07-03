
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Category': ['Food & Nutrition'] * 18,
    'Subcategory': ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Seafood', 'Sweets', 'Beverages', 
                    'Nuts & Seeds', 'Spices & Herbs', 'Snacks', 'Bakery', 'Condiments', 'Supplements', 
                    'Fast Food', 'Organic Food', 'Gourmet Food', 'Street Food'],
    'Popularity (in million)': [2800, 2400, 2000, 1600, 1500, 1400, 1200, 1100, 1000, 900, 850, 800, 
                                750, 700, 650, 600, 550, 500]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 14))
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF3333', '#33FF9F', 
          '#FFC733', '#A833FF', '#FF3385', '#33FFC7', '#FF9633', '#5733FF', 
          '#FF5733', '#33D7FF', '#FF3385', '#C7FF33', '#FF33D7', '#33FFB2']

squarify.plot(sizes=df['Popularity (in million)'], label=df['Subcategory'], color=colors, alpha=0.8)
plt.title('Popularity of Food & Nutrition Subcategories', fontsize=20)
plt.axis('off')

plt.show()