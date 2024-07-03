
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2019', '2019', '2019', '2019', '2019',
             '2020', '2020', '2020', '2020', '2020',
             '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022'],
    "Category": ['Fruits', 'Vegetables', 'Dairy Products', 'Meat & Poultry', 'Beverages',
                 'Fruits', 'Vegetables', 'Dairy Products', 'Meat & Poultry', 'Beverages',
                 'Fruits', 'Vegetables', 'Dairy Products', 'Meat & Poultry', 'Beverages',
                 'Fruits', 'Vegetables', 'Dairy Products', 'Meat & Poultry', 'Beverages'],
    "Revenue": [120.0, 85.3, 60.2, 110.7, 90.8,
                150.4, 100.1, 70.3, 115.9, 102.4,
                180.5, 120.6, 80.7, 130.3, 140.8,
                200.9, 130.8, 90.4, 140.7, 160.6]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(16, 10))
colors = ['#E74C3C', '#2ECC71', '#3498DB', '#9B59B6', '#F1C40F', '#E67E22', '#1ABC9C', '#F39C12', '#8E44AD', '#2C3E50']

# Treemap plot
squarify.plot(sizes=df["Revenue"], label=df["Category"], color=colors, alpha=0.8)
plt.title("Revenue in Food & Nutrition Industry (2019-2022)", fontsize=20, color='#333333', y=1.05)
plt.axis('off')
plt.show()