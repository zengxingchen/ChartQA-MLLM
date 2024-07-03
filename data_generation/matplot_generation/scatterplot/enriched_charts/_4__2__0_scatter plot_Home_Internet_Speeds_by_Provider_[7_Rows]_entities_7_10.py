
import matplotlib.pyplot as plt

city = ["New York", "Los Angeles", "Paris", "London", "Tokyo", "Beijing", "Sydney", "Cape Town", "Moscow", "Rio de Janeiro", "Berlin", "Seoul", "Madrid", "Toronto", "Chicago", "Dubai", "Mexico City", "Buenos Aires", "Mumbai", "Rome"]
happiness_index = [7.2, 7.8, 6.9, 7.5, 7.0, 6.8, 8.0, 6.7, 6.4, 7.6, 7.1, 6.6, 7.3, 7.4, 7.0, 8.1, 6.9, 7.2, 6.5, 7.3]
sleep_hours = [6.5, 6.9, 6.4, 7.0, 6.6, 6.3, 7.1, 6.1, 6.0, 7.2, 6.7, 6.2, 6.8, 6.9, 6.6, 7.3, 6.4, 6.7, 6.1, 6.8]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1']

plt.figure(figsize=(14, 8))

for i in range(len(city)):
    plt.scatter(happiness_index[i], sleep_hours[i], color=colors[i], label=city[i])

plt.title('Correlation between Happiness Index and Average Sleep Hours in Different Cities', pad=20)
plt.xlabel('Happiness Index')
plt.ylabel('Average Sleep Hours (per night)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()