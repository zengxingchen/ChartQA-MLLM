
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
    "AverageExerciseHours": [5.2, 4.3, 6.5, 3.1, 5.0, 
                             4.8, 5.1, 6.0, 4.5, 6.2, 
                             5.7, 3.9, 4.8, 5.3, 4.4, 
                             3.5, 6.1, 5.8, 6.3, 4.0, 
                             3.2, 4.6, 3.5, 6.4, 4.7, 
                             4.2, 3.9, 4.5, 5.0, 4.3],
    "RestingHeartRate": [60, 62, 58, 65, 61, 
                         64, 59, 57, 63, 56, 
                         60, 66, 62, 61, 63, 
                         65, 58, 59, 57, 66, 
                         67, 64, 66, 57, 63, 
                         65, 66, 62, 61, 64]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))

scatter_plot = sns.scatterplot(x="AverageExerciseHours", y="RestingHeartRate", data=df, s=100,
                               palette=["#ff6347", "#ffa07a", "#20b2aa", "#778899", "#ff69b4", 
                                        "#4682b4", "#daa520", "#adff2f", "#7b68ee", "#32cd32",
                                        "#00ced1", "#ffb6c1", "#1e90ff", "#f0e68c", "#ff4500",
                                        "#2e8b57", "#dc143c", "#00fa9a", "#8b008b", "#8fbc8f",
                                        "#ffd700", "#7fff00", "#00ff00", "#ff00ff", "#ff6347",
                                        "#ffa07a", "#20b2aa", "#778899", "#ff69b4", "#4682b4"],
                               hue="City", legend=False)

scatter_plot.set_title("Average Exercise Hours per Week and Resting Heart Rate by City", fontsize=15, pad=20)
scatter_plot.set_xlabel("Average Exercise Hours per Week", fontsize=12)
scatter_plot.set_ylabel("Resting Heart Rate (BPM)", fontsize=12)

plt.show()