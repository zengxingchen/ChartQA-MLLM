
import matplotlib.pyplot as plt

temperatures = [
    22, 23, 22, 21, 20, 19, 24, 25, 23, 26, 28, 30, 27, 26, 29, 21, 22, 20, 19, 18,
    17, 16, 23, 24, 21, 19, 25, 26, 28, 29, 23, 22, 24, 25, 26, 21, 20, 19, 23, 25,
    27, 28, 30, 31, 29, 28, 27, 26, 24, 23, 22, 31, 32, 30, 28, 27, 26, 24, 25, 23,
    22, 21, 20, 19, 18, 17, 16, 18, 17, 19, 20, 22, 23, 24, 26, 25, 24, 23, 22, 21,
    20, 19, 18, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34
]

colors = '#ff6347'
bin_width = 1
plt.figure(figsize=(10, 8))
plt.hist(temperatures, bins=range(int(min(temperatures)), int(max(temperatures)) + bin_width, bin_width), color=colors, orientation='horizontal')
plt.xlabel('Frequency')
plt.ylabel('Temperature (°C)')
plt.title('Frequency Distribution of Daily Temperatures Over Two Months', pad=20)
plt.grid(True)
plt.show()