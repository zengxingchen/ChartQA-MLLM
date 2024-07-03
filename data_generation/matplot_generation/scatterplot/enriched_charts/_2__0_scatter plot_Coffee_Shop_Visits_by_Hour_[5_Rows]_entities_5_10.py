
import matplotlib.pyplot as plt

cities = ["Bangkok", "London", "Paris", "Dubai", "New York", 
          "Singapore", "Kuala Lumpur", "Istanbul", "Tokyo", 
          "Barcelona", "Sydney", "Rome", "Los Angeles", 
          "Amsterdam", "Madrid", "Toronto", "Hong Kong", 
          "Vienna", "Seoul", "San Francisco"]
physical_activity = [5.6, 4.0, 3.5, 6.2, 5.0, 4.8, 5.2, 3.9, 4.5, 
                     3.7, 6.0, 4.1, 5.7, 3.8, 4.4, 4.2, 4.6, 4.3, 
                     3.9, 5.5]
happiness_score = [7.2, 7.8, 7.6, 7.0, 7.4, 7.3, 7.1, 7.2, 7.5, 
                   7.6, 7.8, 7.3, 7.5, 7.7, 7.4, 7.6, 7.1, 7.8, 
                   7.3, 7.5]

plt.figure(figsize=(12, 8))
plt.scatter(physical_activity, happiness_score, c=[
    '#FF5733','#33FF57','#3357FF','#57FFF3','#F3FF57',
    '#FF33FB','#33FFF8','#B833FF','#FF5733','#33FF57',
    '#3357FF','#57FFF3','#F3FF57','#FF33FB','#FF6F61',
    '#6B5B95','#88B04B','#F7CAC9','#92A8D1','#955251'], s=100)

plt.title('Correlation between Physical Activity Level and Happiness Score in Major Cities', fontsize=16)
plt.xlabel('Physical Activity Level (hours/week)', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)

for i, city in enumerate(cities):
    plt.annotate(city, (physical_activity[i], happiness_score[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.show()