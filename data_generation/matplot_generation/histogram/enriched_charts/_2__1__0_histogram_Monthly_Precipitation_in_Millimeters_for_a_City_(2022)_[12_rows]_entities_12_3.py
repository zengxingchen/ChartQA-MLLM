
import matplotlib.pyplot as plt

travelers = [
    34, 56, 65, 72, 85, 90, 23, 45, 53, 67, 71, 84, 28, 49, 59, 62, 73, 81, 34, 46, 58, 69, 75, 89, 27, 50, 63, 77, 92, 24, 47, 55, 66, 78, 83, 30, 44, 54, 68, 74, 80, 37, 52, 60, 70, 79, 87, 33, 51, 64, 76, 88, 35, 48, 61, 82, 91, 36, 43, 57, 85, 40, 55, 72, 86, 39, 56, 73, 87, 41, 53, 74, 89, 38, 52, 75, 90
]

plt.figure(figsize=(14, 8))

plt.hist(travelers, bins=range(20, 100, 5), alpha=0.75, orientation='horizontal', color='#FF4500')

plt.title('Travelers Distribution by Destination')
plt.xlabel('Number of Travelers')
plt.ylabel('Age')

plt.tight_layout()

plt.show()