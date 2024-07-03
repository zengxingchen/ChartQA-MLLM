
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing the dataset into a DataFrame
data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
             "Philadelphia", "San Antonio", "Dallas", "San Diego", "San Jose",
             "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
             "San Francisco", "Indianapolis", "Seattle", "Denver", 
             "Washington D.C.", "Boston", "El Paso", "Nashville", "Detroit",
             "Oklahoma City", "Portland", "Las Vegas", "Memphis", "Louisville",
             "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento"],
    "AverageSunshineHours": [6, 8, 5, 6, 9, 6, 8, 7, 7, 7, 7, 7, 7, 4, 7, 6, 5, 4, 7, 6, 5, 8, 6, 4, 6, 4, 9, 6, 5, 5, 4, 8, 8, 8, 7],
    "AverageTemperature": [10, 18, 10, 20, 23, 12, 21, 18, 18, 16, 20, 20, 19, 11, 16, 14, 12, 11, 10, 15, 11, 19, 15, 9, 15, 12, 21, 16, 14, 12, 10, 16, 19, 19, 18],
    "PopulationSize": [8419000, 3980000, 2706000, 2323000, 1680000, 1584000, 1532000, 1343000, 1429000, 1035000, 995000, 911500, 918000, 906000, 880000,
                       883000, 876000, 753000, 727000, 705000, 692000, 688000, 692000, 677000, 649000, 654000, 651000, 651000, 620000, 621000, 595000,
                       561000, 542000, 531000, 513000]
}

df = pd.DataFrame(data)

# Plotting the bubble chart
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, x="AverageSunshineHours", y="AverageTemperature", size="PopulationSize",
                               sizes=(100, 2000), alpha=0.6, palette=["#FFD700", "#FF8C00", "#FF4500"])

# Enhancing the chart
plt.title("Sunshine Hours, Temperature, and Population Size of Global Cities")
plt.xlabel("Average Hours of Sunshine per day")
plt.ylabel("Average Temperature (°C)")
plt.legend(title='Population Size (in millions)', labelspacing=1, loc="upper right")

# Display
plt.show()