
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
             "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
             "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte"],
    "Population": [8419000, 3990000, 2706000, 2306000, 1662000, 
                   1584000, 1532000, 1426000, 1343000, 1029000,
                   993000, 911000, 890000, 892000, 885000],
    "InternetPenetrationRate": [85, 80, 75, 78, 82, 
                                83, 76, 84, 81, 88,
                                79, 77, 73, 74, 82],
    "AverageDownloadSpeed": [75, 70, 65, 60, 68,
                             66, 62, 74, 67, 80,
                             69, 63, 61, 64, 72]
}

df = pd.DataFrame(data)

sns.set_context("talk")
sns.set_style("whitegrid")

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(
    data=df, 
    x="InternetPenetrationRate", 
    y="AverageDownloadSpeed", 
    hue="City", 
    size="Population",
    sizes=(100, 2000),
    palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF",
             "#FF8F33", "#33FF8F", "#8F33FF", "#FF3333", "#33FFA1",
             "#A1FF33", "#FF33FF", "#33FFF5", "#F5FF33", "#33FFBD"]
).set_title('City Internet Statistics: Penetration Rate and Download Speed', pad=20)

plt.xlabel("Internet Penetration Rate (%)")
plt.ylabel("Average Download Speed (Mbps)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.tight_layout()
plt.show()