
import matplotlib.pyplot as plt

cities = ["Bangkok", "London", "Paris", "Dubai", "New York", 
          "Singapore", "Kuala Lumpur", "Istanbul", "Tokyo", 
          "Barcelona", "Sydney", "Rome", "Los Angeles", 
          "Amsterdam", "Madrid", "Toronto", "Hong Kong", 
          "Vienna", "Seoul", "San Francisco"]
average_rent = [850, 2200, 1850, 2000, 3000, 2500, 700, 600, 2300, 
                1800, 2700, 1600, 2800, 2100, 1700, 1900, 3200, 1500, 
                1800, 3500]
employment_rate = [94.0, 95.5, 93.2, 96.7, 92.1, 97.0, 92.9, 91.8, 96.2, 
                   94.5, 95.8, 91.5, 93.0, 97.5, 94.2, 95.3, 98.1, 96.4, 
                   94.9, 93.4]

plt.figure(figsize=(14, 10))
plt.scatter(average_rent, employment_rate, c=[
    '#FF5733','#33FF57','#3357FF','#57FFF3','#F3FF57',
    '#FF33FB','#33FFF8','#B833FF','#FF5733','#33FF57',
    '#3357FF','#57FFF3','#F3FF57','#FF33FB','#FF6F61',
    '#6B5B95','#88B04B','#F7CAC9','#92A8D1','#955251'], s=100)

plt.title('Correlation between Average Rent and Employment Rate in Major Cities', fontsize=18)
plt.xlabel('Average Rent (USD/month)', fontsize=14)
plt.ylabel('Employment Rate (%)', fontsize=14)

for i, city in enumerate(cities):
    plt.annotate(city, (average_rent[i], employment_rate[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.show()