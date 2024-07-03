
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Company': ['Nike', 'Adidas', 'Puma', 'Under Armour', 'Asics', 'New Balance', 'Reebok', 'Skechers', 'Fila', 'Converse', 'Mizuno', 'Brooks', 'Salomon', 'Saucony'],
    'MarketShare': [34.5, 27.1, 12.5, 8.9, 6.7, 5.3, 4.2, 3.1, 2.4, 1.8, 1.2, 0.9, 0.7, 0.6],
    'SalesVolume': [350.2, 270.1, 120.3, 85.4, 65.7, 52.4, 41.6, 30.2, 22.9, 18.3, 12.4, 9.7, 7.1, 6.3],
    'Region': ['Americas', 'Europe', 'Europe', 'Americas', 'Asia', 'Americas', 'Europe', 'Americas', 'Asia', 'Americas', 'Asia', 'Americas', 'Europe', 'Americas']
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
bubble_chart = sns.scatterplot(data=df, x="Company", y="MarketShare", size="SalesVolume", hue="Region", 
                               palette=["#FF5733", "#33D7FF", "#33FF57", "#FF33FB"], sizes=(50, 2000), 
                               alpha=0.7, edgecolor="w", linewidth=1)

plt.title("Global Sports Equipment Market Share by Company in 2022")
plt.xlabel("Company Name")
plt.ylabel("Market Share (%)")
plt.xticks(rotation=45)
plt.legend(title="Region", loc="upper right", bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()