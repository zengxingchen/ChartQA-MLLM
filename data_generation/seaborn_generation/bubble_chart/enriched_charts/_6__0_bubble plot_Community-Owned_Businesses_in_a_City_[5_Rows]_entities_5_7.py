
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset
data = {
    "Country": ["USA", "China", "Japan", "Germany", "India", 
                "UK", "France", "Italy", "Brazil", "Canada",
                "Russia", "South Korea", "Australia", "Spain", "Mexico"],
    "GDP": [21427700, 14140163, 5081770, 3845630, 2875142, 
            2825208, 2715518, 2005004, 1839758, 1647000,
            1575267, 1655608, 1388272, 1328549, 1228908],
    "InternetUsers": [312000000, 854000000, 118000000, 79900000, 687000000, 
                      62700000, 58700000, 54300000, 149000000, 37000000,
                      117000000, 51000000, 22000000, 42000000, 85000000],
    "Population": [331000000, 1439323776, 126476461, 83783942, 1380004385, 
                   67886011, 65273511, 60461826, 212559417, 37742154,
                   145934462, 51269185, 25499884, 46754778, 128932753]
}

df = pd.DataFrame(data)

# Define the seaborn style
sns.set_context("talk")
sns.set_style("whitegrid")

# Plotting
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(
    data=df, 
    x="InternetUsers", 
    y="GDP", 
    hue="Country", 
    size="Population",
    sizes=(100, 2500),
    palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FF8D33",
             "#33FF8D", "#8D33FF", "#A6FF33", "#5733FF", "#33A6FF",
             "#FF3333", "#33FF33", "#33A6A6", "#A633FF", "#FFA633"]
).set_title('Country Statistics: GDP, Internet Users, and Population', pad=20)

# Modify axes labels
plt.xlabel("Internet Users")
plt.ylabel("GDP (in millions USD)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.tight_layout()
plt.show()