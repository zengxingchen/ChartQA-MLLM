
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2021', '2021', '2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022',
             '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023'],
    "Category": ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Seafood', 'Sweets', 'Beverages', 'Snacks',
                 'Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Seafood', 'Sweets', 'Beverages', 'Snacks',
                 'Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Seafood', 'Sweets', 'Beverages', 'Snacks'],
    "Value": [12.5, 18.2, 15.4, 10.1, 9.3, 7.2, 5.6, 8.9, 6.4,
              13.0, 19.0, 16.0, 10.5, 9.7, 7.5, 6.0, 9.2, 6.7,
              13.5, 20.0, 17.0, 11.0, 10.0, 8.0, 6.5, 9.5, 7.0]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(18, 12))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#ff9ff3']

# Treemap plot
squarify.plot(sizes=df["Value"], label=df["Category"], color=colors, alpha=0.8)
plt.title("Food & Nutrition Consumption (2021-2023)", fontsize=22, color='#555555', pad=20, loc='left')
plt.axis('off')
plt.show()