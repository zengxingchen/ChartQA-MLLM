
import matplotlib.pyplot as plt

# Data for scatterplot
cities = ["Paris", "London", "New York", "Rome", "Berlin", "Madrid", 
          "Vienna", "Amsterdam", "Athens", "Florence", "Tokyo", 
          "Moscow", "Chicago", "Los Angeles", "Barcelona", 
          "Sydney", "Toronto", "San Francisco", "Melbourne", "Beijing"]
number_of_concert_venues = [134, 192, 150, 82, 175, 58, 112, 44, 67, 53, 100, 
                            160, 59, 95, 36, 78, 65, 90, 80, 140]
average_visitors_per_venue = [0.8, 1.2, 1.0, 0.7, 1.1, 0.6, 0.9, 0.7, 0.5, 0.4, 
                              0.9, 1.0, 0.8, 0.9, 0.6, 0.8, 0.7, 1.0, 0.9, 1.1]

# Create scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(number_of_concert_venues, average_visitors_per_venue, c=[
    '#FF5733', '#33FF57', '#3357FF', '#57FFF3', '#F3FF57',
    '#FF33FB', '#33FFF8', '#B833FF', '#FF5733', '#33FF57',
    '#3357FF', '#57FFF3', '#F3FF57', '#FF33FB', '#33FF57',
    '#FF9F33', '#33FF9F', '#9F33FF', '#FF339F', '#339FFF'], s=120)

# Customize plot
plt.title('Relationship Between Number of Concert Venues and Average Annual Visitors per Venue in Major Cities', fontsize=18, pad=20)
plt.xlabel('Number of Concert Venues', fontsize=14)
plt.ylabel('Average Annual Visitors per Venue (millions)', fontsize=14)

# Annotate data points
for i, city in enumerate(cities):
    plt.annotate(city, (number_of_concert_venues[i], average_visitors_per_venue[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()