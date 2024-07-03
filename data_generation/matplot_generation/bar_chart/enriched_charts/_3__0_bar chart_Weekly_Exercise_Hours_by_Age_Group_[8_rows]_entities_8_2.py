
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
product_a_calories = [350, 400, 380, 420, 450, 470, 430, 480, 500, 520, 490, 530]
product_b_calories = [300, 250, 320, 280, 340, 300, 360, 330, 380, 340, 370, 400]
product_c_calories = [200, 180, 240, 220, 260, 230, 270, 250, 290, 260, 280, 300]

fig, ax = plt.subplots(figsize=(12, 10))

bar_width = 0.3
bar_locations_a = range(len(product_a_calories))
bar_locations_b = [x + bar_width for x in bar_locations_a]
bar_locations_c = [x + bar_width for x in bar_locations_b]

bars1 = ax.bar(bar_locations_a, product_a_calories, bar_width, label='Product A', color='#FF7F50')
bars2 = ax.bar(bar_locations_b, product_b_calories, bar_width, label='Product B', color='#6A5ACD')
bars3 = ax.bar(bar_locations_c, product_c_calories, bar_width, label='Product C', color='#20B2AA')

ax.set_xticks([r + bar_width for r in range(len(product_a_calories))])
ax.set_xticklabels(months, rotation=45)

plt.ylabel('Calories Burned')
plt.title('Monthly Calories Burned: Sports & Fitness')
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()