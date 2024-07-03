
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Company': ['Nike', 'Adidas', 'Puma', 'Under Armour', 'Asics', 'New Balance', 'Reebok', 'Skechers', 'Fila', 'Converse', 'Mizuno', 'Brooks', 'Salomon', 'Saucony', 'Hoka One One', 'On Running', 'Altra', 'La Sportiva'],
    'MarketShare': [34.5, 27.1, 12.5, 8.9, 6.7, 5.3, 4.2, 3.1, 2.4, 1.8, 1.2, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
    'SalesVolume': [350.2, 270.1, 120.3, 85.4, 65.7, 52.4, 41.6, 30.2, 22.9, 18.3, 12.4, 9.7, 7.1, 6.3, 5.8, 4.9, 4.2, 3.5],
    'Region': ['Americas', 'Europe', 'Europe', 'Americas', 'Asia', 'Americas', 'Europe', 'Americas', 'Asia', 'Americas', 'Asia', 'Americas', 'Europe', 'Americas', 'Europe', 'Americas', 'Europe', 'Europe']
}
df = pd.DataFrame(data)

plt.figure(figsize=(18, 12))
bubble_chart = sns.scatterplot(data=df, x="Company", y="MarketShare", size="SalesVolume", hue="Region", 
                               palette=["#FF5733", "#33D7FF", "#33FF57", "#FF33FB"], sizes=(50, 2000), 
                               alpha=0.7, edgecolor="w", linewidth=1)

plt.title("Market Share of Sports Footwear Companies in 2023", fontsize=16)
plt.xlabel("Company Name", fontsize=14)
plt.ylabel("Market Share (%)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Region", loc="upper left", bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()