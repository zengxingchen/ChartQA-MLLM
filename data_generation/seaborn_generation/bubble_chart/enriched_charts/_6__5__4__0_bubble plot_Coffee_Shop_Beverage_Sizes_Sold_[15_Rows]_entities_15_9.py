
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Company': ['FreshFarms', 'GreenOrchard', 'TropicalTaste', 'FruitDelight', 'HealthyHarvest', 'SunshineFruits', 'NatureBounty', 'BerryGood', 'OrganicOasis', 'FreshStart', 'PureFruits', 'SweetHarvest', 'GoldenFruits', 'TastyOrchard', 'HealthyChoice', 'VitalFruits', 'GreenHarvest', 'NaturalFarms'],
    'MarketShare': [20.1, 17.3, 15.2, 13.8, 11.5, 8.4, 6.7, 5.3, 3.9, 2.8, 2.0, 1.5, 1.1, 0.9, 0.6, 0.4, 0.2, 0.1],
    'SalesVolume': [200.5, 170.3, 150.1, 135.6, 115.7, 85.4, 67.2, 52.5, 39.1, 28.4, 20.5, 15.6, 11.2, 9.5, 6.7, 4.8, 2.3, 1.5],
    'Region': ['Americas', 'Europe', 'Asia', 'Americas', 'Europe', 'Asia', 'Americas', 'Europe', 'Asia', 'Americas', 'Europe', 'Asia', 'Americas', 'Europe', 'Asia', 'Americas', 'Europe', 'Asia']
}
df = pd.DataFrame(data)

plt.figure(figsize=(20, 14))
bubble_chart = sns.scatterplot(data=df, x="Company", y="MarketShare", size="SalesVolume", hue="Region", 
                               palette=["#FF5733", "#33D7FF", "#33FF57", "#FF33FB"], sizes=(50, 2000), 
                               alpha=0.7, edgecolor="w", linewidth=1)

plt.title("Market Share of Fruit Companies in 2023", fontsize=20, pad=20)
plt.xlabel("Company Name", fontsize=16)
plt.ylabel("Market Share (%)", fontsize=16)
plt.xticks(rotation=45)
plt.legend(title="Region", loc="upper left", bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()