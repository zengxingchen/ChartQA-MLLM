
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Country": ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam", "South Korea", "Turkey", "France", "United Kingdom", "Italy", "Spain"],
    "Year": [2023] * 21,
    "Population": [1427647786, 1393409038, 331002651, 273523615, 212559417, 225199937, 206139589, 169575884, 145912025, 128932753, 125836021, 114963588, 109581078, 104258327, 97338579, 51780579, 85157650, 65426179, 67886011, 60367477, 47351567],
    "Average Rainfall (mm)": [600, 1100, 715, 2700, 1761, 494, 1150, 2031, 460, 738, 1700, 850, 2310, 51, 1825, 1340, 593, 867, 1154, 832, 636],
    "Agricultural Land (%)": [56.1, 60.4, 44.5, 31.0, 32.9, 47.1, 77.7, 59.7, 13.2, 54.9, 12.5, 34.5, 41.7, 3.6, 39.3, 18.2, 35.6, 52.7, 71.8, 47.0, 54.1]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 9))
bubble_chart = sns.scatterplot(data=df, x="Average Rainfall (mm)", y="Agricultural Land (%)",
                               size="Population", sizes=(100, 1500), alpha=0.7,
                               hue="Population", palette=["#3366cc", "#dc3912", "#ff9900", "#109618", "#990099", "#0099c6", "#dd4477", "#66aa00", "#b82e2e", "#316395", "#994499", "#22aa99", "#aaaa11", "#6633cc", "#e67300", "#8b0707", "#651067", "#329262", "#5574a6", "#3b3eac", "#b77322"])

bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Population')

plt.title('Rainfall and Agricultural Land Distribution (2023)')
plt.xlabel('Average Rainfall (mm)')
plt.ylabel('Agricultural Land (%)')

plt.show()