
import matplotlib.pyplot as plt

countries = ["Japan", "Switzerland", "Singapore", "Australia", "Spain",
             "Italy", "Iceland", "Israel", "France", "Norway",
             "Sweden", "Canada", "New Zealand", "United Kingdom", "Germany",
             "Finland", "Ireland", "Austria", "Netherlands", "South Korea"]
life_expectancy = [84.2, 83.4, 83.1, 82.8, 82.4,
                   82.3, 82.1, 82.0, 81.9, 81.8,
                   81.7, 81.5, 81.4, 81.2, 81.1,
                   81.0, 80.9, 80.8, 80.7, 80.5]
healthcare_spending = [4950, 9350, 4400, 5000, 3540,
                       3460, 6470, 2740, 4950, 7510,
                       5700, 4960, 4110, 4260, 5560,
                       4650, 5450, 5360, 5600, 2650]

sizes = [spend / 10 for spend in healthcare_spending]

colors = ['#4CAF50' if life > 82 else '#FFC107' if life > 81 else '#F44336' for life in life_expectancy]

fig, ax = plt.subplots(figsize=(12, 10))
bubble = ax.scatter(life_expectancy, countries, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

ax.set_title('Life Expectancy and Healthcare Spending in Various Countries', fontsize=16)
ax.set_xlabel('Life Expectancy (Years)', fontsize=14)
ax.set_ylabel('Countries', fontsize=14)

ax.grid(True)

for spend in sorted(set(healthcare_spending), reverse=True):
    ax.scatter([], [], c='k', alpha=0.3, s=spend/10, label=str(spend) + ' USD')
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Healthcare Spending (USD)')

plt.tight_layout()
plt.show()