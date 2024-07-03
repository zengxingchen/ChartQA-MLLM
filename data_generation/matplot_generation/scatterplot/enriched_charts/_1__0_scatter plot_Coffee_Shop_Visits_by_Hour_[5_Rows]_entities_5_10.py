
import matplotlib.pyplot as plt

# Data for scatterplot
cities = ["Paris", "London", "New York", "Rome", "Berlin", "Madrid", 
          "Vienna", "Amsterdam", "Athens", "Florence", "Tokyo", 
          "Moscow", "Chicago", "Los Angeles", "Barcelona"]
number_of_museums = [134, 192, 83, 82, 175, 58, 112, 44, 67, 53, 100, 160, 59, 95, 36]
visitors_per_museum = [1.2, 0.9, 1.5, 0.7, 0.8, 0.6, 1.0, 0.8, 0.5, 0.4, 0.9, 0.7, 1.1, 0.8, 0.6]

# Create scatterplot
plt.figure(figsize=(12, 8))
plt.scatter(number_of_museums, visitors_per_museum, c=[
    '#FF5733','#33FF57','#3357FF','#57FFF3','#F3FF57',
    '#FF33FB','#33FFF8','#B833FF','#FF5733','#33FF57',
    '#3357FF','#57FFF3','#F3FF57','#FF33FB','#33FF57'], s=100)

# Customize plot
plt.title('Relationship Between Number of Museums and Average Visitors per Museum in Major Cities', fontsize=16)
plt.xlabel('Number of Museums', fontsize=12)
plt.ylabel('Average Visitors per Museum (millions)', fontsize=12)

# Annotate data points
for i, city in enumerate(cities):
    plt.annotate(city, (number_of_museums[i], visitors_per_museum[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()