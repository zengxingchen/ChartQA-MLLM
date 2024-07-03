
import matplotlib.pyplot as plt

data_points = [
    35, 55, 40, 65, 75, 85, 95, 45, 50, 60,
    70, 80, 90, 100, 110, 120, 30, 40, 25, 50,
    65, 75, 85, 55, 35, 95, 105, 115, 125, 130,
    20, 25, 35, 45, 55, 60, 70, 80, 90, 40,
    30, 50, 60, 70, 85, 95, 105, 115, 20, 10,
    35, 50, 45, 55, 65, 75, 85, 95, 40, 50,
    60, 70, 80, 100, 110, 120, 30, 40, 50, 60,
    70, 80, 90, 100, 20, 25, 35, 45, 55, 65,
    75, 85, 90, 105, 115, 125, 130, 20, 30, 40,
    50, 60, 70, 80, 90, 100, 110, 120, 25, 35
]

plt.figure(figsize=(12, 8))
plt.hist(
    data_points,
    bins=15,
    orientation='horizontal',
    color='#3498db',
    edgecolor='#1f618d',
    alpha=0.85,
    rwidth=0.75
)

plt.title('Distribution of Page Count in Books')
plt.xlabel('Frequency')
plt.ylabel('Number of Pages')
plt.grid(axis='y', alpha=0.75)

plt.show()