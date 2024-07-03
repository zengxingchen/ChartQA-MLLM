
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Brand': ['Hilton', 'Marriott', 'Hyatt', 'Accor', 'IHG', 'Wyndham', 'Choice', 'Radisson', 'Best Western', 'OYO', 'Meliá', 'Shangri-La', 'Rosewood', 'Four Seasons', 'Ritz-Carlton', 'St. Regis', 'Fairmont'],
    'UnitsSold': [60, 55, 40, 30, 28, 20, 15, 10, 8, 12, 18, 14, 9, 6, 5, 7, 11],
    'AverageSellingPrice': [200, 250, 180, 220, 230, 210, 150, 240, 190, 130, 170, 260, 280, 300, 340, 320, 290],
    'MarketSharePercentage': [12.0, 11.5, 8.0, 6.0, 5.5, 4.0, 3.0, 2.0, 1.8, 2.4, 3.2, 2.8, 1.5, 1.2, 1.0, 1.4, 2.2]
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
bubble_chart = sns.scatterplot(data=df, x='UnitsSold', y='AverageSellingPrice', size='MarketSharePercentage', sizes=(100, 1000), hue='Brand', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#FFC300', '#DAF7A6', '#900C3F', '#C70039', '#581845', '#C0C0C0', '#808080', '#800000', '#808000', '#00FF00', '#00FFFF', '#000080', '#FF00FF'])

plt.title('Top Hotel Chains by Room Sales', fontsize=20)
plt.xlabel('Rooms Sold (in thousands)', fontsize=14)
plt.ylabel('Average Room Price (in USD)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

plt.tight_layout()
plt.show()