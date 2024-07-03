
import matplotlib.pyplot as plt

# Data
day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
sugar_consumed = [45, 60, 55, 70, 65, 75, 68, 50, 80, 55, 72, 65, 60, 75, 55, 70, 50, 65, 60, 80, 68, 55, 75, 70, 50, 72, 65, 60, 75, 55, 70]
blood_sugar_level = [95, 105, 100, 110, 107, 115, 109, 97, 118, 100, 112, 107, 105, 115, 100, 110, 97, 107, 105, 118, 109, 100, 115, 110, 97, 112, 107, 105, 115, 100, 110]

plt.figure(figsize=(14, 10))
plt.scatter(sugar_consumed, blood_sugar_level, color='#3498DB')
plt.xlabel('Daily Sugar Consumed (grams)')
plt.ylabel('Blood Sugar Level (mg/dL)')
plt.title('Correlation between Daily Sugar Consumption and Blood Sugar Levels', fontsize=16, pad=25)
plt.show()