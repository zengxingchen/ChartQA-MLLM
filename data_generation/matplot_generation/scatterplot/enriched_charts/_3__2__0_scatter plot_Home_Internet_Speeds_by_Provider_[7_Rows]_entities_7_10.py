
import matplotlib.pyplot as plt

city = ["New York", "Los Angeles", "Paris", "London", "Tokyo", "Beijing", "Sydney", "Cape Town", "Moscow", "Rio de Janeiro", "Berlin", "Seoul", "Madrid", "Toronto", "Chicago", "Dubai", "Mexico City", "Buenos Aires", "Mumbai", "Rome"]
films_watched = [45, 52, 50, 55, 60, 57, 48, 49, 43, 50, 55, 60, 53, 50, 45, 48, 55, 49, 58, 52]
leisure_hours = [10.5, 11.0, 12.0, 12.5, 13.0, 13.5, 14.0, 10.0, 11.5, 10.8, 12.3, 11.1, 12.6, 13.3, 14.2, 10.6, 11.8, 13.1, 14.5, 12.2]
colors = ['#ff0000', '#00ff00', '#0000ff', '#ff00ff', '#00ffff', '#ffff00', '#ff9900', '#9933ff', '#6699ff', '#99cc00', '#ff3399', '#ccff33', '#cc33ff', '#ffcc00', '#00ccff', '#33cc33', '#cc6633', '#ff6699', '#339999', '#ff99cc']

plt.figure(figsize=(18, 12))

for i in range(len(city)):
    plt.scatter(films_watched[i], leisure_hours[i], color=colors[i], label=city[i])

plt.title('Correlation between Number of Films Watched and Leisure Hours in Different Cities', pad=20)
plt.xlabel('Number of Films Watched (per year)')
plt.ylabel('Leisure Hours (per week)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()