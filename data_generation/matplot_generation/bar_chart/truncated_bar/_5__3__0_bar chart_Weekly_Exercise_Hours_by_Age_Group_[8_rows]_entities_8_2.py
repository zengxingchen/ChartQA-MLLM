
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
product_a_calories = [350, 400, 380, 420, 450, 470, 430, 480, 500, 520, 490, 530]
product_b_calories = [300, 250, 320, 280, 340, 300, 360, 330, 380, 340, 370, 400]
product_c_calories = [200, 180, 240, 220, 260, 230, 270, 250, 290, 260, 280, 300]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.25
bar_height = 0.25
bar_locations_a = range(len(product_a_calories))
bar_locations_b = [x + bar_width for x in bar_locations_a]
bar_locations_c = [x + bar_width for x in bar_locations_b]

bars1 = ax.barh(bar_locations_a, product_a_calories, bar_height, label='Product A', color='#3498DB')
bars2 = ax.barh(bar_locations_b, product_b_calories, bar_height, label='Product B', color='#2ECC71')
bars3 = ax.barh(bar_locations_c, product_c_calories, bar_height, label='Product C', color='#E74C3C')

ax.set_yticks([r + bar_width for r in range(len(product_a_calories))])
ax.set_yticklabels(months)

ax.set_xlim(150, 600)
ax.set_xlabel('Calories Consumed')
ax.set_title('Monthly Calories Consumed: Food & Nutrition')
ax.legend(loc='lower right')

plt.tight_layout()
plt.show()