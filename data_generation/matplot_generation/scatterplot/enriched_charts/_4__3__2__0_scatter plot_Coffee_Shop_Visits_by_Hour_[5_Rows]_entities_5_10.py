
import matplotlib.pyplot as plt

cities = ["Bangkok", "London", "Paris", "Dubai", "New York", 
          "Singapore", "Kuala Lumpur", "Istanbul", "Tokyo", 
          "Barcelona", "Sydney", "Rome", "Los Angeles", 
          "Amsterdam", "Madrid", "Toronto", "Hong Kong", 
          "Vienna", "Seoul", "San Francisco"]
gym_membership_cost = [50, 85, 70, 100, 120, 90, 45, 55, 95, 
                       75, 110, 65, 115, 80, 72, 88, 105, 
                       67, 78, 125]
fitness_level_index = [75.2, 82.5, 78.3, 85.1, 87.4, 83.6, 72.4, 74.8, 84.0, 
                       80.2, 86.3, 77.5, 88.0, 81.7, 79.1, 82.8, 86.7, 79.9, 
                       81.4, 89.2]

plt.figure(figsize=(16, 12))
plt.scatter(gym_membership_cost, fitness_level_index, c=[
    '#FF5733','#33FF57','#3357FF','#57FFF3','#F3FF57',
    '#FF33FB','#33FFF8','#B833FF','#FF5733','#33FF57',
    '#3357FF','#57FFF3','#F3FF57','#FF33FB','#FF6F61',
    '#6B5B95','#88B04B','#F7CAC9','#92A8D1','#955251'], s=100)

plt.title('Correlation between Average Gym Membership Cost and Fitness Level Index in Major Cities', fontsize=18, y=1.05)
plt.xlabel('Average Gym Membership Cost (USD/month)', fontsize=14)
plt.ylabel('Fitness Level Index', fontsize=14)

for i, city in enumerate(cities):
    plt.annotate(city, (gym_membership_cost[i], fitness_level_index[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.show()