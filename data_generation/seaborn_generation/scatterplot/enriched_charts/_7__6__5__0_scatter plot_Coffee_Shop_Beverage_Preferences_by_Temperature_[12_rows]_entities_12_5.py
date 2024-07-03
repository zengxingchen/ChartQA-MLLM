
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
    "DailyFruitIntake": [2.5, 3.0, 1.8, 2.2, 2.7, 
                         2.9, 1.5, 3.3, 2.0, 2.8, 
                         3.1, 1.6, 2.4, 2.6, 1.7, 
                         1.9, 3.2, 2.1, 3.4, 1.4, 
                         1.3, 1.5, 1.2, 2.3, 2.6, 
                         2.0, 1.9, 2.7, 2.2, 2.4],
    "VitaminCLevel": [45, 50, 35, 42, 48, 
                      47, 30, 52, 40, 49, 
                      51, 33, 43, 46, 34, 
                      38, 50, 41, 53, 28, 
                      25, 32, 22, 44, 45, 
                      36, 37, 48, 42, 43]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))

scatter_plot = sns.scatterplot(x="DailyFruitIntake", y="VitaminCLevel", data=df, s=100,
                               palette=["#ff7f50", "#ff4500", "#32cd32", "#4682b4", "#daa520", 
                                        "#ff6347", "#20b2aa", "#adff2f", "#7b68ee", "#00ced1",
                                        "#ffb6c1", "#1e90ff", "#f0e68c", "#ff69b4", "#2e8b57",
                                        "#dc143c", "#00fa9a", "#8b008b", "#8fbc8f", "#ffd700",
                                        "#7fff00", "#00ff00", "#ff00ff", "#ff6347", "#ffa07a",
                                        "#20b2aa", "#778899", "#ff69b4", "#4682b4", "#daa520"],
                               hue="City", legend=False)

scatter_plot.set_title("Daily Fruit Intake and Vitamin C Levels by City", fontsize=18, pad=20)
scatter_plot.set_xlabel("Daily Fruit Intake (servings)", fontsize=14)
scatter_plot.set_ylabel("Vitamin C Level (mg/dL)", fontsize=14)

plt.show()