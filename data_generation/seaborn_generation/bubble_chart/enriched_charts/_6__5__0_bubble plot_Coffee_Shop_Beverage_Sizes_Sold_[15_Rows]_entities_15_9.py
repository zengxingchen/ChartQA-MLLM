
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Type': ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass', 'Wave', 'Tidal'],
    'MarketShare': [27.3, 25.1, 19.6, 12.4, 10.7, 2.5, 2.0],
    'SalesVolume': [340.2, 315.4, 265.3, 165.8, 145.6, 30.2, 25.3],
    'Region': ['Asia', 'Europe', 'Americas', 'Asia', 'Europe', 'Asia', 'Europe']
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
bubble_chart = sns.scatterplot(data=df, x="Type", y="MarketShare", size="SalesVolume", hue="Region", 
                               palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A8"], sizes=(100, 2000), 
                               alpha=0.7, edgecolor="k", linewidth=1)

plt.title("Market Share of Renewable Energy Sources in 2022", fontsize=18, pad=20)
plt.xlabel("Energy Type", fontsize=14)
plt.ylabel("Market Share (%)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Region", loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()