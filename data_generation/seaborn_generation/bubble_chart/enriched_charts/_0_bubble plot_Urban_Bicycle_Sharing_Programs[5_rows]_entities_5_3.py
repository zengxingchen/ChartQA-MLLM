
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Manufacturer': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO',
                     'Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO',
                     'Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO'],
    'Year': [2020, 2020, 2020, 2020, 2020,
             2021, 2021, 2021, 2021, 2021,
             2022, 2022, 2022, 2022, 2022],
    'Shipments': [300, 200, 150, 120, 100,
                  320, 215, 120, 135, 110,
                  330, 220, 90, 145, 115],
    'MarketShare': [30, 20, 15, 12, 10,
                    35, 23, 11, 14, 12,
                    31, 21, 8, 14, 11]
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(14, 7))
bubble_chart = sns.scatterplot(data=df, x="Year", y="Shipments",
                               hue="Manufacturer", size="MarketShare",
                               palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
                               sizes=(20, 2000), alpha=0.7)

# Adjust the legend and plot titles
plt.title('Smartphone Shipments by Manufacturer', fontsize=16)
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Manufacturer')
bubble_chart.set_xlabel('Year', fontsize=12)
bubble_chart.set_ylabel('Shipments (in millions)', fontsize=12)

plt.tight_layout()
plt.show()