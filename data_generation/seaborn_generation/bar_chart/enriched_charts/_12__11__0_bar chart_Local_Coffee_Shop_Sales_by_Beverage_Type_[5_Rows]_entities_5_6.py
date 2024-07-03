
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Topic': [
        'Sustainable_Fashion', 'Eco_Friendly_Beauty_Products', 'Organic_Cosmetics',
        'Ethical_Fashion_Brands', 'Cruelty_Free_Cosmetics', 'Recycled_Materials_Fashion',
        'Fair_Trade_Beauty', 'Vegan_Beauty_Products', 'Second_Hand_Fashion',
        'Handmade_Jewelry', 'Upcycled_Fashion', 'Natural_Skincare', 'Zero_Waste_Fashion',
        'Slow_Fashion', 'Biodegradable_Beauty_Products', 'Plastic_Free_Beauty',
        'Sustainable_Fashion_Events', 'Eco_Conscious_Fashion_Shows', 'Green_Fashion_Initiatives',
        'Renewable_Fashion'
    ],
    'Count': [
        120000, 90000, 85000, 78000, 75000, 72000, 70000, 69000, 68000, 67000,
        66000, 65000, 64000, 63000, 62000, 61000, 60000, 59000, 58000, 57000
    ]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 12))

ax = sns.barplot(
    y="Topic",
    x="Count",
    data=df,
    palette=[
        '#4b0082', '#800080', '#9370db', '#ba55d3', '#dda0dd', '#ee82ee',
        '#dda0dd', '#ee82ee', '#da70d6', '#ff00ff', '#ff1493', '#c71585',
        '#db7093', '#e6e6fa', '#ffb6c1', '#ffc0cb', '#faebd7', '#f5f5dc',
        '#ffe4c4', '#8b0000'
    ],
    linewidth=0.8
)

ax.bar_label(ax.containers[0], fmt='%.0f', label_type='edge', padding=3)
ax.set(title='Popular Sustainable Fashion and Beauty Trends', xlabel='Count', ylabel='Trend')

plt.show()