
import matplotlib.pyplot as plt
import numpy as np

years = ['2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028']
fast_food = np.array([55, 52, 50, 48, 45, 42, 40, 38, 35, 32])
home_cooked = np.array([30, 32, 33, 35, 38, 40, 42, 44, 46, 48])
takeaway = np.array([10, 12, 14, 15, 15, 16, 16, 16, 17, 18])
others = np.array([5, 4, 3, 2, 2, 2, 2, 2, 2, 2])

totals = fast_food + home_cooked + takeaway + others
fast_food_percentage = fast_food / totals * 100
home_cooked_percentage = home_cooked / totals * 100
takeaway_percentage = takeaway / totals * 100
others_percentage = others / totals * 100

colors_fast_food = '#ff6347'
colors_home_cooked = '#4682b4'
colors_takeaway = '#32cd32'
colors_others = '#ffd700'

bar_width = 0.55

bar1 = plt.bar(years, fast_food_percentage, color=colors_fast_food, edgecolor='white', width=bar_width)
bar2 = plt.bar(years, home_cooked_percentage, bottom=fast_food_percentage, color=colors_home_cooked, edgecolor='white', width=bar_width)
bar3 = plt.bar(years, takeaway_percentage, bottom=fast_food_percentage+home_cooked_percentage, color=colors_takeaway, edgecolor='white', width=bar_width)
bar4 = plt.bar(years, others_percentage, bottom=fast_food_percentage+home_cooked_percentage+takeaway_percentage, color=colors_others, edgecolor='white', width=bar_width)

plt.xticks(years)
plt.xlabel('Year')
plt.title('Trends in Meal Preferences')
plt.yticks(np.arange(0, 101, 10))
plt.ylabel('Percentage (%)')
plt.gcf().set_size_inches(14, 10)
plt.gca().set_aspect(0.05)

plt.legend((bar1[0], bar2[0], bar3[0], bar4[0]), ('Fast Food', 'Home Cooked', 'Takeaway', 'Others'), loc='upper left', bbox_to_anchor=(1,1))

plt.show()