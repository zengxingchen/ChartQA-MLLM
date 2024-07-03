
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grapes', 'Pineapple', 'Mango', 'Blueberry', 'Watermelon', 'Peach', 'Papaya', 'Kiwi', 'Guava', 'Lemon', 'Avocado'],
    'VitaminC': [14, 12, 70, 59, 4, 47, 36, 10, 10, 6, 60, 92, 228, 77, 20],
    'Weight': [182, 120, 130, 18, 5, 905, 200, 2, 9200, 150, 500, 76, 100, 65, 150],
    'Price': [1.2, 0.5, 0.8, 0.1, 2.5, 3, 1.5, 6, 0.3, 1.3, 1.8, 1.1, 2.2, 0.7, 2],
    'Popularity': [75, 85, 90, 92, 80, 70, 88, 95, 65, 78, 82, 87, 83, 79, 84]
})

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(
    data=data,
    x='VitaminC',
    y='Price',
    size='Weight',
    hue='Popularity',
    palette=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76eec6', '#ffbbff', '#808000', '#FF6347', '#6e8b3d', '#c6e2ff', '#2e8b57', '#ffdab9'],
    sizes=(100, 2000),
    alpha=0.7
)

plt.legend(title='Popularity Rating', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Comparison of Fruits by Vitamin C Content, Price, and Weight', fontsize=20, pad=20)
plt.xlabel('Vitamin C (mg)', fontsize=14)
plt.ylabel('Price in USD', fontsize=14)

plt.show()