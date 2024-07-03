
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Company': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO', 'Vivo', 'Lenovo', 'LG', 'Sony', 'Google', 'Nokia', 'Motorola', 'OnePlus', 'HTC', 'Realme', 'Asus'],
    'MarketShare': [31.2, 22.1, 10.5, 8.2, 5.7, 4.9, 3.3, 2.9, 1.2, 1.0, 0.9, 0.7, 0.6, 0.4, 1.1, 1.3],
    'SalesVolume': [320.8, 228.3, 108.7, 84.5, 58.9, 50.6, 34.1, 29.9, 12.4, 10.3, 9.2, 7.2, 6.2, 4.1, 12.0, 13.0],
    'Region': ['Asia', 'Americas', 'Asia', 'Asia', 'Asia', 'Asia', 'Americas', 'Americas', 'Europe', 'Americas', 'Europe', 'Americas', 'Asia', 'Asia', 'Asia', 'Asia']
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
bubble_chart = sns.scatterplot(data=df, x="Company", y="MarketShare", size="SalesVolume", hue="Region", 
                               palette=["#E74C3C", "#3498DB", "#2ECC71", "#9B59B6"], sizes=(50, 2000), 
                               alpha=0.7, edgecolor="k", linewidth=1)

plt.title("Top Smartphone Companies by Market Share in 2022", fontsize=18, pad=20)
plt.xlabel("Company Name", fontsize=14)
plt.ylabel("Market Share (%)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Region", loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()