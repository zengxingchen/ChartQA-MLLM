
import matplotlib.pyplot as plt

# Data
city = ["New York", "Los Angeles", "Paris", "London", "Tokyo", "Beijing", "Sydney", "Cape Town", "Moscow", "Rio de Janeiro"]
temperature = [15.2, 18.5, 12.4, 11.7, 16.3, 13.9, 17.9, 16.7, 7.5, 23.4]
tourists = [8330, 7480, 8460, 7530, 9270, 8560, 4880, 2350, 4150, 2870]
colors = ['#FF6363', '#FFD700', '#1E90FF', '#32CD32', '#9400D3', '#FF8C00', '#20B2AA', '#FFA500', '#FF4500', '#8A2BE2']

plt.figure(figsize=(14, 8))  # Width, height in inches

# Scatter plot
for i in range(len(city)):
    plt.scatter(temperature[i], tourists[i], color=colors[i], label=city[i])

# Customizing the plot
plt.title('Relationship between Average Temperature and Tourist Numbers in Cities')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Average Number of Tourists (in thousands)')
plt.legend()

plt.show()