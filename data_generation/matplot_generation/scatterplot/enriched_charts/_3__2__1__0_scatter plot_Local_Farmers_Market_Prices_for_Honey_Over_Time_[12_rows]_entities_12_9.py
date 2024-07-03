
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
stars_observed = [150, 160, 155, 165, 158, 162, 170, 160, 155, 175, 168, 158, 162, 170, 180, 155, 175, 165, 170, 160, 165, 172, 180, 175, 160, 155, 170, 150, 175, 182, 170]
viewing_time = [20, 22, 21, 23, 20, 22, 24, 21, 20, 25, 23, 22, 21, 24, 26, 20, 24, 22, 23, 21, 23, 24, 26, 25, 22, 20, 23, 19, 25, 26, 23]

plt.figure(figsize=(14, 10))
plt.scatter(stars_observed, viewing_time, color='#3366FF')
plt.xlabel('Stars Observed')
plt.ylabel('Viewing Time (minutes)')
plt.title('Stars Observed vs. Viewing Time in a Month', pad=20)
plt.show()