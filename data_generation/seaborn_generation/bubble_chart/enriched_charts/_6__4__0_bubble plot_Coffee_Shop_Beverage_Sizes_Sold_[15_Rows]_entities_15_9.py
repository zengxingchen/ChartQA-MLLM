
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Company': ['Apple', 'Samsung', 'Huawei', 'Google', 'Xiaomi', 'Microsoft', 'Sony', 'Dell', 'Lenovo', 'HP', 'LG', 'Asus', 'Acer', 'Nokia'],
    'MarketShare': [42.5, 28.3, 15.2, 8.9, 5.4, 3.7, 2.9, 2.2, 1.8, 1.5, 1.2, 0.9, 0.7, 0.5],
    'SalesVolume': [450.2, 310.7, 170.3, 98.4, 65.1, 48.9, 38.6, 27.4, 22.7, 18.3, 14.6, 11.2, 9.8, 7.3],
    'Region': ['Americas', 'Asia', 'Europe', 'Americas', 'Asia', 'Americas', 'Europe', 'Americas', 'Asia', 'Americas', 'Asia', 'Asia', 'Europe', 'Europe']
}
df = pd.DataFrame(data)

plt.figure(figsize=(18, 12))
bubble_chart = sns.scatterplot(data=df, x="Company", y="MarketShare", size="SalesVolume", hue="Region", 
                               palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"], sizes=(100, 3000), 
                               alpha=0.8, edgecolor="k", linewidth=1)

plt.title("Market Share of Tech Companies by Region in 2022", fontsize=16)
plt.xlabel("Company Name", fontsize=14)
plt.ylabel("Market Share (%)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Region", loc="upper left", bbox_to_anchor=(1, 1), fontsize=12)

plt.tight_layout()
plt.show()