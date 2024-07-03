
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2019', '2019', '2019', '2019', '2019',
             '2020', '2020', '2020', '2020', '2020',
             '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022'],
    "Category": ['Fitness Apps', 'Sports Equipment', 'Online Training Programs', 'Nutrition Supplements', 'Outdoor Gear',
                 'Fitness Apps', 'Sports Equipment', 'Online Training Programs', 'Nutrition Supplements', 'Outdoor Gear',
                 'Fitness Apps', 'Sports Equipment', 'Online Training Programs', 'Nutrition Supplements', 'Outdoor Gear',
                 'Fitness Apps', 'Sports Equipment', 'Online Training Programs', 'Nutrition Supplements', 'Outdoor Gear'],
    "Investment": [200.5, 180.3, 130.2, 110.7, 90.8,
                   230.4, 200.9, 140.7, 120.1, 100.4,
                   260.5, 220.6, 150.2, 130.3, 110.9,
                   290.7, 240.8, 160.3, 140.2, 120.5]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(24, 16))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF2',
          '#FFBD33', '#8D33FF', '#FF5733', '#33FF57', '#3357FF']

# Treemap plot
squarify.plot(sizes=df["Investment"], label=df["Category"], color=colors, alpha=0.8)
plt.title("Investment in Sports & Fitness Technology (2019-2022)", fontsize=28, color='#333333', y=1.05)
plt.axis('off')
plt.show()