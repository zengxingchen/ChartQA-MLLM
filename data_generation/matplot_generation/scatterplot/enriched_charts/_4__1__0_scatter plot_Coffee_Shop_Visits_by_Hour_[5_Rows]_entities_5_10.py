
import matplotlib.pyplot as plt

# Data for scatterplot
cities = ["Paris", "London", "New York", "Rome", "Berlin", "Madrid", 
          "Vienna", "Amsterdam", "Athens", "Florence", "Tokyo", 
          "Moscow", "Chicago", "Los Angeles", "Barcelona", "Sydney",
          "Dubai", "Hong Kong", "Toronto", "San Francisco", "Beijing",
          "Singapore", "Melbourne", "Bangkok"]
number_of_restaurants = [200, 250, 300, 180, 220, 170, 160, 140, 130, 150, 280, 
                         240, 210, 260, 190, 200, 230, 270, 190, 180, 250, 220, 
                         200, 240]
average_revenue_per_restaurant = [2.5, 3.0, 2.8, 2.2, 2.7, 2.1, 2.4, 2.3, 2.0, 2.2, 
                                  3.1, 2.6, 2.4, 3.0, 2.5, 2.7, 2.8, 3.1, 2.6, 2.9, 
                                  2.7, 2.8, 2.5, 2.6]

# Create scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(number_of_restaurants, average_revenue_per_restaurant, c=[
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2',
    '#FF1493', '#00CED1', '#9400D3', '#FFA07A', '#20B2AA',
    '#FF4500', '#2E8B57', '#4169E1', '#DAA520', '#4B0082',
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2',
    '#FF1493', '#00CED1', '#9400D3', '#FFA07A'], s=100)

# Customize plot
plt.title('Relationship Between Number of Restaurants and Average Revenue per Restaurant in Major Cities', fontsize=18)
plt.xlabel('Number of Restaurants', fontsize=14)
plt.ylabel('Average Revenue per Restaurant (millions)', fontsize=14)

# Annotate data points
for i, city in enumerate(cities):
    plt.annotate(city, (number_of_restaurants[i], average_revenue_per_restaurant[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()