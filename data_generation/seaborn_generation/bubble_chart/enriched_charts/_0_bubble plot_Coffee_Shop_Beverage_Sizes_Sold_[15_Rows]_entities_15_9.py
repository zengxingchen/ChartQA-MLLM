
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Assuming the CSV data is loaded into a DataFrame
data = {
    'Company': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO', 'Vivo', 'Lenovo', 'LG', 'Sony', 'Google', 'Nokia', 'Motorola', 'OnePlus', 'HTC'],
    'MarketShare': [31.2, 22.1, 10.5, 8.2, 5.7, 4.9, 3.3, 2.9, 1.2, 1.0, 0.9, 0.7, 0.6, 0.4],
    'SalesVolume': [320.8, 228.3, 108.7, 84.5, 58.9, 50.6, 34.1, 29.9, 12.4, 10.3, 9.2, 7.2, 6.2, 4.1],
    'Region': ['Asia', 'Americas', 'Asia', 'Asia', 'Asia', 'Asia', 'Americas', 'Americas', 'Europe', 'Americas', 'Europe', 'Americas', 'Asia', 'Asia']
}
df = pd.DataFrame(data)

# Create a scatter plot with varying bubble sizes
plt.figure(figsize=(14, 8))
bubble_chart = sns.scatterplot(data=df, x="Company", y="MarketShare", size="SalesVolume", hue="Region", 
                               palette=["#FF5733", "#33D7FF", "#33FF57", "#FF33FB"], sizes=(20, 2000), 
                               alpha=0.7, edgecolor="w", linewidth=1)

plt.title("Global Smartphone Market Share by Company in 2022")
plt.xlabel("Company Name")
plt.ylabel("Market Share (%)")
plt.xticks(rotation=45)
plt.legend(title="Region", loc="upper left", bbox_to_anchor=(1, 1))

# Show the plot
plt.tight_layout()
plt.show()