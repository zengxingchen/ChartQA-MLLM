
import matplotlib.pyplot as plt

data_points = [
    5, 8, 12, 18, 22, 25, 18, 30, 34, 37,
    15, 20, 25, 28, 14, 21, 29, 33, 36, 41,
    9, 16, 24, 31, 3, 7, 13, 20, 35, 23,
    27, 11, 17, 26, 4, 19, 32, 38, 42, 44,
    45, 47, 2, 6, 10, 50, 55, 60, 65, 70, 75
]

plt.figure(figsize=(10, 6))
plt.hist(
    data_points,
    bins=12,
    orientation='vertical',
    color='#ff5733',
    edgecolor='#333333',
    alpha=0.8,
    rwidth=0.85
)

plt.title('Distribution of Study Hours in a Week')
plt.xlabel('Number of Study Hours')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

plt.show()