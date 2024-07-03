
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Topic": ['Food & Nutrition'] * 13,
    "Category": ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Sweets', 'Beverages', 
                 'Snacks', 'Seafood', 'Nuts', 'Oils', 'Spices', 'Legumes'],
    "Percentage": [30.5, 25.3, 15.8, 10.4, 8.7, 5.4, 3.9, 4.8, 6.2, 4.1, 1.9, 2.1, 5.7]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(16, 10))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c2f0c2','#f0c2c2','#d9d9d9','#b3b3cc','#ffccff','#ccffcc','#f0b3b3']

# Treemap plot
squarify.plot(sizes=df["Percentage"], label=df["Category"], color=colors, alpha=0.8)
plt.title("Food & Nutrition Category Market Share", fontsize=20, color='#555555', pad=20)
plt.axis('off')
plt.show()