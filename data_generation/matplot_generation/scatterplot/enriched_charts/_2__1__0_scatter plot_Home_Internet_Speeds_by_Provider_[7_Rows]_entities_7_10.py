
import matplotlib.pyplot as plt

city = ["New York", "Los Angeles", "Paris", "London", "Tokyo", "Beijing", "Sydney", "Cape Town", "Moscow", "Rio de Janeiro", "Berlin", "Toronto", "Dubai", "Mumbai", "Mexico City", "Hong Kong", "Buenos Aires", "Cairo", "Bangkok", "Lagos", "Singapore", "Seoul", "Sao Paulo", "Istanbul", "Vienna", "Stockholm", "Zurich", "Buenos Aires", "Copenhagen", "Bangkok"]
average_income = [65000, 62000, 58000, 61000, 72000, 50000, 67000, 45000, 48000, 37000, 59000, 63000, 80000, 25000, 30000, 71000, 34000, 27000, 28000, 20000, 75000, 69000, 42000, 38000, 64000, 68000, 90000, 32000, 76000, 29000]
education_expenditure = [12000, 11000, 15000, 13000, 14000, 10000, 12500, 9000, 9500, 8000, 13500, 12000, 16000, 6000, 7000, 15000, 7500, 5000, 6500, 4000, 15500, 14500, 8500, 8200, 12800, 13800, 17000, 7200, 16000, 6400]
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#AEC7E8', '#FFBB78', '#98DF8A', '#FF9896', '#C5B0D5', '#C49C94', '#F7B6D2', '#C7C7C7', '#DBDB8D', '#9EDAE5', '#6B6ECF', '#7B4173', '#FF4500', '#6A5ACD', '#7FFF00', '#FFD700', '#8A2BE2', '#B22222', '#FF1493', '#228B22']

plt.figure(figsize=(18, 12))

for i in range(len(city)):
    plt.scatter(average_income[i], education_expenditure[i], color=colors[i], label=city[i])

plt.title('Average Income vs Education Expenditure in Major Cities', pad=20)
plt.xlabel('Average Income (USD)')
plt.ylabel('Education Expenditure (USD)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()