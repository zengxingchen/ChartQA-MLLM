
import matplotlib.pyplot as plt

rainfall = [
    7, 12, 15, 14, 19, 22, 24, 26, 25, 28, 30, 34, 32, 29, 21, 23, 20, 18,
    15, 12, 9, 13, 17, 19, 22, 24, 26, 27, 29, 28, 30, 31, 25, 23, 21, 20,
    18, 16, 14, 12, 10, 8, 5, 7, 10, 13, 16, 18, 20, 22, 24, 25, 28, 30, 27,
    25, 23, 21, 19, 18, 15, 12, 10, 8, 6, 4
]

plt.figure(figsize=(10, 6))

plt.hist(rainfall, bins=12, color='#e74c3c', edgecolor='#2c3e50', linewidth=1.0)

plt.title('Monthly Rainfall Distribution')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Number of Days')

plt.grid(axis='y', color='grey', linestyle='--', linewidth=0.5)

plt.show()