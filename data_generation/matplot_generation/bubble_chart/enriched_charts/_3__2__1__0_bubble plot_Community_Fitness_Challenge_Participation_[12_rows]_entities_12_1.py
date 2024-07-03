
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

countries = [
    "United States", "China", "Japan", "Germany", "India", "United Kingdom", "France", 
    "Italy", "Brazil", "Canada", "South Korea", "Russia", "Australia", "Spain", 
    "Mexico", "Indonesia", "Netherlands", "Saudi Arabia", "Turkey", "Switzerland"
]
gdp = [
    21.43, 14.34, 5.08, 3.86, 2.87, 2.83, 2.71, 2.00, 1.84, 1.74, 1.63, 1.58, 1.39, 1.39, 
    1.27, 1.12, 0.91, 0.78, 0.76, 0.71
]
happiness_index = [
    7.0, 5.5, 5.9, 6.5, 4.5, 7.2, 6.9, 6.2, 6.8, 7.6, 5.8, 5.5, 7.5, 6.4, 6.3, 5.3, 7.4, 6.1, 
    5.1, 7.5
]
bubble_size = [
    150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 50, 40, 40, 30, 30, 20, 20, 20, 10
]
colors = [
    "#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#666666", 
    "#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#666666", 
    "#1b9e77", "#d95f02", "#7570b3", "#e7298a"
]

plt.figure(figsize=(18, 12))

for i in range(len(countries)):
    plt.scatter(gdp[i], happiness_index[i], s=bubble_size[i]*10, c=colors[i], alpha=0.6, edgecolors="w", linewidth=2)

plt.title('GDP vs Happiness Index of Major Countries', pad=20)
plt.xlabel('GDP in Trillion USD')
plt.ylabel('Happiness Index')
plt.grid(True)

legend_elements = [Patch(facecolor=colors[i], label=countries[i]) for i in range(len(countries))]
plt.legend(handles=legend_elements, title="Countries", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()