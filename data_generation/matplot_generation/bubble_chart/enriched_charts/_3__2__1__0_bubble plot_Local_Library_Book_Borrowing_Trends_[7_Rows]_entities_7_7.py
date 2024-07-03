
import matplotlib.pyplot as plt

cities = [
    "Paris", "London", "Rome", "New York", "Tokyo",
    "Dubai", "Barcelona", "Singapore", "Bangkok", "Istanbul",
    "Hong Kong", "Sydney", "Los Angeles", "Amsterdam", "Berlin",
    "Las Vegas", "Miami", "Vienna", "Madrid", "San Francisco",
    "Toronto", "Chicago", "Boston", "Moscow", "Seoul"
]

book_sales = [
    4.2, 5.8, 3.1, 6.7, 7.5,
    4.0, 3.8, 6.2, 2.5, 3.4,
    5.0, 4.5, 5.2, 2.8, 3.7,
    2.9, 3.3, 3.6, 3.2, 4.8,
    4.1, 4.3, 3.9, 4.4, 5.9
]

population_millions = [
    2.14, 8.98, 2.87, 8.4, 9.27,
    3.3, 1.62, 5.7, 10.5, 15.03,
    7.4, 5.23, 3.99, 0.87, 3.65,
    0.65, 0.47, 1.9, 3.22, 0.88,
    2.93, 2.71, 0.69, 12.54, 9.76
]

education_quality_index = [
    85, 88, 82, 90, 92,
    80, 84, 89, 78, 75,
    87, 86, 83, 81, 84,
    79, 80, 85, 82, 88,
    84, 83, 86, 76, 88
]

sizes = [index * 10 for index in education_quality_index]

colors = [
    '#FF6347' if sales < 3.5 else '#FFD700' if sales < 5.0 else '#32CD32'
    for sales in book_sales
]

fig, ax = plt.subplots(figsize=(16, 9))
bubble = ax.scatter(book_sales, cities, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

ax.set_title('Book Sales vs. Education Quality in Major Cities', fontsize=18, pad=20)
ax.set_xlabel('Book Sales (millions)', fontsize=14)
ax.set_ylabel('Cities', fontsize=14)

ax.grid(True)

for index in sorted(set(education_quality_index), reverse=True):
    ax.scatter([], [], c='k', alpha=0.3, s=index * 10, label=str(index))
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Education Quality Index', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()