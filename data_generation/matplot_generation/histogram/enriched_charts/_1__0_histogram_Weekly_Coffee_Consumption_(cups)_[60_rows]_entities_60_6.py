import matplotlib.pyplot as plt

data_points = [
    30, 45, 25, 60, 70, 55, 35, 85, 95, 40,
    50, 65, 75, 85, 90, 100, 110, 20, 10, 80,
    35, 50, 65, 85, 105, 120, 130, 30, 45, 55,
    70, 40, 25, 65, 75, 85, 55, 35, 50, 95,
    70, 80, 55, 45, 60, 75, 90
]

plt.figure(figsize=(10, 6))
plt.hist(
    data_points,
    bins=12,
    orientation='vertical',
    color='#ff5733',
    edgecolor='#000000',
    alpha=0.8,
    rwidth=0.85
)

plt.title('Distribution of Workout Duration in Minutes')
plt.xlabel('Number of Minutes')
plt.ylabel('Frequency')
plt.grid(axis='x', alpha=0.75)

plt.show()