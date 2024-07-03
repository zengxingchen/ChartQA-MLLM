import matplotlib.pyplot as plt

categories = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
electricity_spending = [85, 90, 88, 92, 94, 95, 100, 98, 93, 89, 87, 91]
water_spending = [45, 50, 47, 49, 52, 53, 55, 54, 51, 48, 46, 50]
internet_spending = [30, 35, 32, 33, 34, 36, 38, 37, 35, 33, 31, 34]

fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.25
bar_locations_electricity = range(len(electricity_spending))
bar_locations_water = [x + bar_width for x in bar_locations_electricity]
bar_locations_internet = [x + bar_width for x in bar_locations_water]

bars1 = ax.bar(bar_locations_electricity, electricity_spending, bar_width, label="Electricity", color='#0073e6')
bars2 = ax.bar(bar_locations_water, water_spending, bar_width, label="Water", color='#33cc33')
bars3 = ax.bar(bar_locations_internet, internet_spending, bar_width, label="Internet", color='#ff9933')

ax.set_xticks([r + bar_width for r in range(len(electricity_spending))])
ax.set_xticklabels(categories, rotation=45)

plt.ylabel('Spending ($)')
plt.title("Monthly Household Spending on Utilities", pad=20)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()