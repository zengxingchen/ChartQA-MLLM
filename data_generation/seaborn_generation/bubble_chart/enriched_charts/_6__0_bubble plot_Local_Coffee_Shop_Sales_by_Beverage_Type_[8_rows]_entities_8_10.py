
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
    "AverageTouristVisits": [12, 10, 8, 6, 5, 7, 6, 6, 7, 5, 4, 4, 3, 3, 4, 9, 3, 8, 6, 11, 7, 2, 5, 3, 2, 5, 10, 3, 2, 4, 3, 2, 2, 2, 3],
    "NumberOfAttractions": [150, 130, 120, 90, 70, 110, 85, 95, 100, 65, 60, 50, 55, 40, 60, 120, 45, 110, 80, 140, 105, 30, 85, 50, 35, 75, 120, 55, 40, 65, 50, 30, 25, 35, 45],
    "PopulationSize": [8419000, 3980000, 2706000, 2323000, 1680000, 1584000, 1532000, 1343000, 1429000, 1035000, 995000, 911500, 918000, 906000, 880000,
                       883000, 876000, 753000, 727000, 705000, 692000, 688000, 692000, 677000, 649000, 654000, 651000, 651000, 620000, 621000, 595000,
                       561000, 542000, 531000, 513000]
}

df = pd.DataFrame(data)

# Plotting the bubble chart
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df, x="AverageTouristVisits", y="NumberOfAttractions", size="PopulationSize",
                               sizes=(100, 2000), alpha=0.6, palette=["#2E8B57", "#6A5ACD", "#FF6347"])

# Enhancing the chart
plt.title("Tourist Visits, Attractions, and Population Size of Various Cities", pad=20)
plt.xlabel("Average Annual Tourist Visits (millions)")
plt.ylabel("Number of Tourist Attractions")
plt.legend(title='Population Size (in millions)', labelspacing=1, loc="lower right")

# Display
plt.show()