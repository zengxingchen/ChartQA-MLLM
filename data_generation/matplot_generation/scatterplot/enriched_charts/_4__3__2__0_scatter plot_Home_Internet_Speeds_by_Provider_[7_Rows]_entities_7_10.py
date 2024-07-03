
import matplotlib.pyplot as plt

city = ["New York", "Los Angeles", "Paris", "London", "Tokyo", "Beijing", "Sydney", "Cape Town", "Moscow", "Rio de Janeiro", "Berlin", "Seoul", "Madrid", "Toronto", "Chicago", "Dubai", "Mexico City", "Buenos Aires", "Mumbai", "Rome"]
hours_of_exercise = [3.5, 4.0, 3.8, 4.2, 4.5, 4.1, 3.9, 3.7, 4.3, 4.0, 3.6, 4.4, 3.9, 4.0, 4.2, 3.8, 4.1, 3.6, 4.3, 3.7]
calories_burned = [350, 400, 370, 410, 450, 420, 390, 365, 430, 400, 360, 440, 395, 405, 415, 375, 425, 355, 435, 370]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

plt.figure(figsize=(14, 10))

for i in range(len(city)):
    plt.scatter(hours_of_exercise[i], calories_burned[i], color=colors[i], label=city[i])

plt.title('Correlation between Hours of Exercise and Calories Burned in Different Cities', pad=20)
plt.xlabel('Hours of Exercise (per week)')
plt.ylabel('Calories Burned (per session)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()