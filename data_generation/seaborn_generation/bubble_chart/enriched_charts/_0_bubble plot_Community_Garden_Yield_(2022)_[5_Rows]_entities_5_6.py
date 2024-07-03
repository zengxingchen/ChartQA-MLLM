
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the given data
data = {
    'Brand': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'OnePlus', 'Google', 'Sony', 'Nokia', 'Lenovo', 'LG', 'Motorola', 'Realme', 'Asus', 'TCL', 'ZTE'],
    'UnitsSold': [70, 50, 38, 28, 25, 23, 5, 3, 2, 4, 6, 7, 8, 10, 3.5, 4.5, 1.8],
    'AverageSellingPrice': [250, 750, 300, 150, 200, 180, 500, 650, 550, 100, 230, 280, 220, 120, 350, 90, 110],
    'MarketSharePercentage': [20.0, 15.0, 10.9, 8.1, 7.3, 6.7, 1.4, 0.9, 0.6, 1.2, 1.7, 2.0, 2.3, 2.9, 1.0, 1.3, 0.5]
}
df = pd.DataFrame(data)

# Plot the bubble chart
plt.figure(figsize=(14, 8))
bubble_chart = sns.scatterplot(data=df, x='UnitsSold', y='AverageSellingPrice', size='MarketSharePercentage', sizes=(20, 500), hue='Brand', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#FFC300', '#DAF7A6', '#900C3F', '#C70039', '#581845', '#C0C0C0', '#808080', '#800000', '#808000', '#00FF00', '#00FFFF', '#000080', '#FF00FF'])

# Customizing the plot
plt.title('Global Smartphone Sales by Brand (Q1)', fontsize=20)
plt.xlabel('Units Sold (in millions)', fontsize=14)
plt.ylabel('Average Selling Price (in USD)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.tight_layout()
plt.show()