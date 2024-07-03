
import matplotlib.pyplot as plt

cities = [
    "Paris", "London", "New York", "Rome", "Berlin", "Madrid", "Vienna",
    "Amsterdam", "Athens", "Florence", "Tokyo", "Moscow", "Chicago",
    "Los Angeles", "Barcelona", "San Francisco", "Toronto", "Sydney",
    "Seoul", "Mumbai", "Beijing", "Shanghai", "Hong Kong", "Singapore",
    "Dubai", "Bangkok", "Kuala Lumpur", "Jakarta", "Buenos Aires", "Mexico City"
]
number_of_bookstores = [
    95, 120, 85, 70, 90, 60, 80, 50, 65, 45, 110, 105, 75, 85, 55, 65,
    70, 60, 100, 80, 90, 95, 85, 70, 50, 65, 45, 60, 75, 80
]
visitors_per_bookstore = [
    2.0, 1.8, 2.3, 1.6, 1.9, 1.2, 1.7, 1.5, 1.4, 1.3, 1.8, 2.1, 2.0,
    1.9, 1.2, 2.2, 1.7, 2.0, 1.5, 1.8, 1.7, 2.1, 1.6, 1.8, 2.0, 1.9,
    1.4, 1.2, 1.5, 2.0
]

plt.figure(figsize=(16, 12))
plt.scatter(number_of_bookstores, visitors_per_bookstore, c=[
    '#FF5733', '#33FF57', '#3357FF', '#57FFF3', '#F3FF57', '#FF33FB',
    '#33FFF8', '#B833FF', '#FF5733', '#33FF57', '#3357FF', '#57FFF3',
    '#F3FF57', '#FF33FB', '#33FF57', '#FFAB33', '#33ABFF', '#5733FF',
    '#FF5733', '#33FF57', '#FF5733', '#33FF57', '#3357FF', '#57FFF3',
    '#FF33FB', '#33FFF8', '#B833FF', '#FF5733', '#33FF57', '#3357FF'
], s=100)

plt.title('Number of Bookstores vs. Average Visitors per Bookstore in Major Cities', fontsize=20)
plt.xlabel('Number of Bookstores', fontsize=15)
plt.ylabel('Average Visitors per Bookstore (thousands)', fontsize=15)

for i, city in enumerate(cities):
    plt.annotate(city, (number_of_bookstores[i], visitors_per_bookstore[i]),
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.show()