
import matplotlib.pyplot as plt

categories = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
mens_spending = [120, 130, 140, 125, 135, 145, 150, 155, 160, 165, 170, 175]
womens_spending = [150, 145, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
childrens_spending = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.3
bar_locations_men = range(len(mens_spending))
bar_locations_women = [x + bar_height for x in bar_locations_men]
bar_locations_children = [x + bar_height for x in bar_locations_women]

bars1 = ax.barh(bar_locations_men, mens_spending, bar_height, label="Men's Spending", color='#FF5733')
bars2 = ax.barh(bar_locations_women, womens_spending, bar_height, label="Women's Spending", color='#33FF57')
bars3 = ax.barh(bar_locations_children, childrens_spending, bar_height, label="Children's Spending", color='#3357FF')

ax.set_yticks([r + bar_height for r in range(len(mens_spending))])
ax.set_yticklabels(categories)

plt.xlabel('Spending ($)')
plt.title("Monthly Spending on Fashion for Men, Women, and Children")
ax.legend(loc='lower right')

plt.tight_layout()
plt.show()