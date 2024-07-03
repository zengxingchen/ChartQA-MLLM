
import matplotlib.pyplot as plt

countries = ["France", "Spain", "United States", "China", "Italy", "Turkey", "Mexico",
             "Germany", "Thailand", "United Kingdom", "Japan", "Austria", "Malaysia",
             "Greece", "Russia", "Canada", "Australia", "Hong Kong", "Singapore",
             "Indonesia", "Brazil", "India", "Netherlands", "Egypt", "South Africa",
             "Argentina", "Vietnam"]
travelers_per_year = [90, 82, 79, 63, 62, 52, 45, 39, 39, 37, 32, 31, 26, 24, 22, 22,
                      21, 20, 19, 16, 14, 11, 10, 9, 8, 7, 7]  # in millions
tourism_revenue = [70, 60, 240, 130, 55, 40, 35, 45, 50, 36, 39, 19, 20, 18, 17, 30,
                   35, 27, 20, 15, 25, 28, 21, 13, 10, 12, 14]  # in billions USD
satisfaction_rating = [85, 82, 78, 75, 80, 74, 77, 83, 76, 81, 84, 88, 73, 86, 70, 80,
                       79, 85, 87, 72, 69, 67, 81, 65, 68, 66, 71]  # in satisfaction rating

fig, ax = plt.subplots(figsize=(18, 10))

colors = ["#3498db", "#2ecc71", "#e74c3c", "#9b59b6", "#f1c40f", "#e67e22", "#1abc9c",
          "#34495e", "#f39c12", "#d35400", "#7f8c8d", "#2980b9", "#27ae60", "#8e44ad",
          "#c0392b", "#16a085", "#bdc3c7", "#2c3e50", "#f06292", "#4caf50", "#ba68c8",
          "#ffa726", "#d32f2f", "#303f9f", "#009688", "#8d6e63", "#cddc39"]

for i, country in enumerate(countries):
    ax.scatter(travelers_per_year[i], tourism_revenue[i], s=satisfaction_rating[i]*10,
               c=colors[i], alpha=0.6, edgecolors="w", label=country)

ax.set_title('Tourism Performance by Country', fontsize=18, pad=20)
ax.set_xlabel('Annual Travelers (in millions)', fontsize=14)
ax.set_ylabel('Tourism Revenue (in billions USD)', fontsize=14)

ax.grid(True)

ax.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

plt.tight_layout()
plt.show()