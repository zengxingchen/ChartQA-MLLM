
import matplotlib.pyplot as plt

city = ["New York", "Los Angeles", "Paris", "London", "Tokyo", "Beijing", "Sydney", "Cape Town", "Moscow", "Rio de Janeiro", "Berlin", "Seoul", "Madrid", "Toronto", "Chicago", "Dubai", "Mexico City", "Buenos Aires", "Mumbai", "Rome"]
books_read = [35, 42, 38, 45, 50, 47, 41, 36, 33, 39, 44, 49, 37, 40, 35, 38, 43, 36, 48, 37]
study_hours = [14.2, 15.8, 16.5, 17.1, 18.3, 19.6, 16.0, 14.7, 13.9, 15.2, 17.4, 18.0, 15.5, 16.3, 14.1, 16.8, 17.6, 14.9, 19.2, 15.4]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff9896', '#98df8a', '#c5b0d5', '#c49c94', '#f7b6d2', '#dbdb8d', '#9edae5', '#1f77b4', '#ff7f0e', '#2ca02c']

plt.figure(figsize=(16, 10))

for i in range(len(city)):
    plt.scatter(books_read[i], study_hours[i], color=colors[i], label=city[i])

plt.title('Correlation between Number of Books Read and Study Hours in Different Cities', pad=20)
plt.xlabel('Number of Books Read (per year)')
plt.ylabel('Study Hours (per week)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()