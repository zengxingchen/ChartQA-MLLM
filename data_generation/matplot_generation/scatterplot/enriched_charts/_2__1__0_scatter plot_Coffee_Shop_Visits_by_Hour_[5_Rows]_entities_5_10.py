
import matplotlib.pyplot as plt

# Data for scatterplot
cities = ["Paris", "London", "New York", "Rome", "Berlin", "Madrid", 
          "Vienna", "Amsterdam", "Athens", "Florence", "Tokyo", 
          "Moscow", "Chicago", "Los Angeles", "Barcelona",
          "San Francisco", "Toronto", "Sydney", "Seoul", "Mumbai"]
number_of_bookstores = [95, 120, 85, 70, 90, 60, 80, 50, 65, 45, 110, 105, 75, 85, 55, 65, 70, 60, 100, 80]
visitors_per_bookstore = [2.0, 1.8, 2.3, 1.6, 1.9, 1.2, 1.7, 1.5, 1.4, 1.3, 1.8, 2.1, 2.0, 1.9, 1.2, 2.2, 1.7, 2.0, 1.5, 1.8]

# Create scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(number_of_bookstores, visitors_per_bookstore, c=[
    '#FF5733','#33FF57','#3357FF','#57FFF3','#F3FF57',
    '#FF33FB','#33FFF8','#B833FF','#FF5733','#33FF57',
    '#3357FF','#57FFF3','#F3FF57','#FF33FB','#33FF57',
    '#FFAB33','#33ABFF','#5733FF','#FF5733','#33FF57'], s=100)

# Customize plot
plt.title('Number of Bookstores vs. Average Visitors per Bookstore in Major Cities', fontsize=16)
plt.xlabel('Number of Bookstores', fontsize=12)
plt.ylabel('Average Visitors per Bookstore (thousands)', fontsize=12)

# Annotate data points
for i, city in enumerate(cities):
    plt.annotate(city, (number_of_bookstores[i], visitors_per_bookstore[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()