
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
rainfall = [12, 15, 10, 17, 13, 11, 18, 14, 16, 15, 19, 17, 13, 14, 20, 12, 18, 16, 17, 13, 15, 14, 18, 19, 16, 15, 13, 12, 17, 18, 16]
plant_growth = [20, 22, 18, 24, 21, 19, 25, 22, 23, 22, 26, 24, 20, 21, 27, 19, 24, 23, 24, 20, 22, 21, 25, 26, 23, 22, 20, 19, 24, 25, 23]

plt.figure(figsize=(14, 10))
plt.scatter(rainfall, plant_growth, color='#4CAF50')
plt.xlabel('Daily Rainfall (mm)')
plt.ylabel('Plant Growth (cm)')
plt.title('Effect of Rainfall on Plant Growth')
plt.show()