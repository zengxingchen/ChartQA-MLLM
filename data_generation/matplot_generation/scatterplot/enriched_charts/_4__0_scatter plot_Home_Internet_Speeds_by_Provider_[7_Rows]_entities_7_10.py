
import matplotlib.pyplot as plt

# Data
city = ["New York", "Los Angeles", "Paris", "London", "Tokyo", "Beijing", "Sydney", "Cape Town", "Moscow", "Rio de Janeiro", "Berlin", "Toronto", "Mumbai", "Singapore", "Dubai"]
album_sales = [500, 600, 450, 470, 520, 480, 550, 430, 390, 570, 460, 490, 510, 530, 520]
musicians = [30, 25, 28, 22, 26, 24, 20, 18, 23, 21, 27, 29, 19, 31, 20]
colors = ['#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#9400D3', '#FF8C00', '#20B2AA', '#FF6363', '#8A2BE2', '#FFA500', '#FF1493', '#0000FF', '#00FF00', '#FF00FF', '#00CED1']

plt.figure(figsize=(16, 10))  # Width, height in inches

# Scatter plot
for i in range(len(city)):
    plt.scatter(album_sales[i], musicians[i], color=colors[i], label=city[i])

# Customizing the plot
plt.title('Album Sales vs. Number of Musicians in Cities', pad=20)
plt.xlabel('Album Sales (in thousands)')
plt.ylabel('Number of Musicians')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()