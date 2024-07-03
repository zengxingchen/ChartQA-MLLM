
import matplotlib.pyplot as plt

cities = ["Bangkok", "London", "Paris", "Dubai", "New York", 
          "Singapore", "Kuala Lumpur", "Istanbul", "Tokyo", 
          "Barcelona", "Sydney", "Rome", "Los Angeles", 
          "Amsterdam", "Madrid", "Toronto", "Hong Kong", 
          "Vienna", "Seoul", "San Francisco", "Shanghai",
          "Mumbai", "Berlin", "Cape Town", "Moscow",
          "Mexico City", "Buenos Aires", "Rio de Janeiro",
          "Cairo", "Jakarta"]
gdp_growth = [3.5, 1.8, 2.0, 3.2, 1.5, 3.6, 4.0, 2.8, 1.7, 
              2.5, 3.3, 1.9, 1.6, 2.7, 2.2, 2.9, 3.4, 2.1, 
              2.6, 1.4, 4.2, 3.8, 1.8, 2.4, 2.3, 3.1, 3.0, 
              2.7, 3.5, 4.1]
unemployment_rate = [1.2, 4.5, 3.9, 2.3, 5.2, 2.1, 1.8, 3.4, 3.0, 
                     4.0, 2.6, 3.8, 5.3, 3.1, 4.2, 2.4, 1.9, 3.3, 
                     2.7, 5.5, 2.0, 1.6, 3.7, 3.5, 4.1, 3.2, 3.6, 
                     3.8, 4.0, 2.2]

plt.figure(figsize=(14, 10))
plt.scatter(gdp_growth, unemployment_rate, c=[
    '#FF0000','#00FF00','#0000FF','#FFFF00','#FF00FF',
    '#00FFFF','#800000','#008000','#000080','#808000',
    '#800080','#008080','#808080','#C0C0C0','#FFA500',
    '#A52A2A','#8A2BE2','#5F9EA0','#7FFF00','#D2691E',
    '#FF7F50','#6495ED','#DC143C','#00FFFF','#00008B',
    '#008B8B','#B8860B','#A9A9A9','#006400','#8B0000'], s=120)

plt.title('Economic Indicators: Annual GDP Growth vs Unemployment Rate in Major Cities', fontsize=18)
plt.xlabel('Annual GDP Growth Rate (%)', fontsize=14)
plt.ylabel('Unemployment Rate (%)', fontsize=14)

for i, city in enumerate(cities):
    plt.annotate(city, (gdp_growth[i], unemployment_rate[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.show()