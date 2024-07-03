
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
             "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
             "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
             "Indianapolis", "Seattle", "Denver", "Boston", "El Paso",
             "Detroit", "Nashville", "Memphis", "Portland", "Las Vegas", 
             "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson"],
    "UnemploymentRate": [4.2, 5.0, 6.3, 4.5, 4.0, 
                         5.8, 4.6, 3.5, 4.1, 3.2, 
                         3.4, 5.0, 4.3, 4.8, 4.5, 
                         5.2, 3.6, 4.0, 3.3, 5.5, 
                         7.1, 3.7, 6.0, 4.3, 6.8, 
                         4.8, 5.7, 6.2, 5.9, 4.9],
    "PovertyRate": [15.5, 18.3, 17.2, 19.8, 16.7, 
                    22.4, 17.0, 14.8, 15.6, 11.9, 
                    13.2, 17.5, 16.0, 18.1, 16.5, 
                    19.0, 11.5, 12.3, 10.9, 20.3, 
                    24.7, 13.7, 21.5, 12.9, 20.1, 
                    17.3, 21.2, 23.5, 19.6, 18.8]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))

scatter_plot = sns.scatterplot(x="UnemploymentRate", y="PovertyRate", data=df, s=100,
                               palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#33FFF6"],
                               hue="City", legend=False)

scatter_plot.set_title("Unemployment Rate vs. Poverty Rate by City", pad=20)
scatter_plot.set_xlabel("Unemployment Rate (%)")
scatter_plot.set_ylabel("Poverty Rate (%)")

plt.show()