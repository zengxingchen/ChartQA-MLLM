
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with diversified data
df = pd.DataFrame({
    'category': ['Food', 'Food', 'Food', 'Food', 
                 'Nutrition', 'Nutrition', 'Nutrition', 'Nutrition', 
                 'Cuisine', 'Cuisine', 'Cuisine', 'Cuisine', 
                 'Diet', 'Diet', 'Diet', 'Diet', 
                 'Beverages', 'Beverages', 'Beverages', 'Beverages', 
                 'Supplements', 'Supplements', 'Supplements', 'Supplements'],
    'sub_category': ['Fruits', 'Vegetables', 'Grains', 'Dairy', 
                     'Protein', 'Carbohydrates', 'Vitamins', 'Minerals', 
                     'Asian', 'European', 'American', 'African', 
                     'Keto', 'Vegan', 'Paleo', 'Low-Carb', 
                     'Juices', 'Tea', 'Coffee', 'Smoothies', 
                     'Protein Shakes', 'Multivitamins', 'Herbal', 'Fish Oil'],
    'value': [1200, 800, 1500, 900, 1100, 1000, 1300, 1400, 
              700, 600, 800, 900, 1000, 1100, 1200, 1300, 
              1400, 900, 1100, 1000, 700, 800, 900, 600]
})

# Create a new color list
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#00FA9A', '#FF69B4', '#CD5C5C', '#4682B4', '#D2691E', 
          '#8FBC8F', '#6495ED', '#DC143C', '#00CED1', '#FF4500', '#DA70D6', '#EEE8AA', '#98FB98', 
          '#AFEEEE', '#DB7093', '#D3D3D3', '#B0E0E6', '#ADD8E6', '#F08080', '#F0E68C', '#FFDAB9']

# Plot
plt.figure(figsize=(30, 15))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.8)
plt.title('Distribution of Key Areas in Food & Nutrition', fontsize=30)
plt.axis('off')
plt.show()