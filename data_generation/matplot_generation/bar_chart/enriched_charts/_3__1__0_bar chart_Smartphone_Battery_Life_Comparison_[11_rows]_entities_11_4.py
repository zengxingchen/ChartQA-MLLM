
import matplotlib.pyplot as plt

cities = [
    "Paris", "Bangkok", "London", "Dubai", "Singapore", 
    "Kuala Lumpur", "Istanbul", "New York", "Tokyo", 
    "Seoul", "Hong Kong", "Barcelona", "Rome", 
    "Osaka", "Los Angeles", "Moscow"
]
tourists = [
    29000000, 25000000, 19000000, 16000000, 15000000, 
    13000000, 12500000, 12000000, 11000000, 10500000, 
    10000000, 9000000, 8500000, 8000000, 7800000, 7500000
]

colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#ffbb78', '#98df8a', '#c49c94', '#f7b6d2', '#c7c7c7',
    '#dbdb8d'
]

plt.figure(figsize=(10, 8))
plt.barh(cities, tourists, color=colors, height=0.6)

plt.title('Number of Tourists in Top Cities', fontsize=16, pad=20)
plt.xlabel('Number of Tourists', fontsize=14)
plt.ylabel('City', fontsize=14)

plt.show()