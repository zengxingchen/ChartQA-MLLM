
import matplotlib.pyplot as plt

# Data for scatterplot
cities = ["Bangkok", "London", "Paris", "Dubai", "New York", 
          "Singapore", "Kuala Lumpur", "Istanbul", "Tokyo", 
          "Barcelona", "Sydney", "Rome", "Los Angeles", "Amsterdam"]
books_read = [8, 15, 12, 10, 18, 9, 7, 11, 16, 13, 14, 10, 17, 12]
exercise_hours = [3.5, 5.0, 4.2, 2.7, 6.3, 3.1, 2.4, 3.8, 5.5, 4.0, 4.8, 3.6, 5.7, 4.3]

# Create scatterplot
plt.figure(figsize=(12, 7))
plt.scatter(books_read, exercise_hours, c=[
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2',
    '#FF4500', '#1E90FF', '#ADFF2F', '#FF6347', '#4682B4',
    '#32CD32', '#FFD700', '#8A2BE2', '#FF4500'], s=100)

# Customize plot
plt.title('Correlation between Books Read per Month and Exercise Hours per Week', fontsize=16)
plt.xlabel('Books Read per Month', fontsize=12)
plt.ylabel('Exercise Hours per Week', fontsize=12)

# Annotate data points
for i, city in enumerate(cities):
    plt.annotate(city, (books_read[i], exercise_hours[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()