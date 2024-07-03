
import matplotlib.pyplot as plt

# Data for scatterplot
cities = ["Bangkok", "London", "Paris", "Dubai", "New York", 
          "Singapore", "Kuala Lumpur", "Istanbul", "Tokyo", 
          "Barcelona", "Sydney", "Rome", "Los Angeles", "Amsterdam"]
temperatures = [28.6, 11.3, 12.3, 35.0, 13.5, 27.0, 28.0, 14.7, 16.0, 16.4, 17.6, 15.5, 18.0, 10.2]
tourists = [22.7, 19.2, 18.0, 16.7, 13.5, 14.5, 13.4, 13.4, 13.4, 9.5, 10.5, 10.3, 9.0, 8.1]

# Create scatterplot
plt.figure(figsize=(10, 6)) # Changed width and height
plt.scatter(temperatures, tourists, c=[
    '#FF5733','#33FF57','#3357FF','#57FFF3','#F3FF57',
    '#FF33FB','#33FFF8','#B833FF','#FF5733','#33FF57',
    '#3357FF','#57FFF3','#F3FF57','#FF33FB'], s=100)

# Customize plot
plt.title('Correlation between Average Annual Temperature and Tourist Numbers in Major Cities', fontsize=16)
plt.xlabel('Average Annual Temperature (°C)', fontsize=12)
plt.ylabel('Average Annual Tourists (millions)', fontsize=12)

# Annotate data points
for i, city in enumerate(cities):
    plt.annotate(city, (temperatures[i], tourists[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()