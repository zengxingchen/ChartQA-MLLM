
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2019', '2019', '2019', '2019', '2019',
             '2020', '2020', '2020', '2020', '2020',
             '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022'],
    "Category": ['Fitness Equipment', 'Fitness Apparel', 'Fitness Supplements', 'Gyms', 'Online Fitness Classes',
                 'Fitness Equipment', 'Fitness Apparel', 'Fitness Supplements', 'Gyms', 'Online Fitness Classes',
                 'Fitness Equipment', 'Fitness Apparel', 'Fitness Supplements', 'Gyms', 'Online Fitness Classes',
                 'Fitness Equipment', 'Fitness Apparel', 'Fitness Supplements', 'Gyms', 'Online Fitness Classes'],
    "Revenue": [150.0, 85.3, 45.2, 105.7, 75.8,
                185.4, 95.1, 55.3, 110.9, 102.4,
                210.5, 105.6, 65.7, 120.3, 125.8,
                230.9, 115.8, 75.4, 130.7, 140.6]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(18, 12))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5', '#FFC300', '#DAF7A6', '#FF69B4', '#8A2BE2', '#5F9EA0']

# Treemap plot
squarify.plot(sizes=df["Revenue"], label=df["Category"], color=colors, alpha=0.8)
plt.title("Revenue in Fitness Industry (2019-2022)", fontsize=20, color='#333333', y=1.02)
plt.axis('off')
plt.show()