
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
transport = [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600]
accommodation = [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100]
food = [1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
activities = [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]

plt.figure(figsize=(14, 8))
plt.stackplot(months, transport, accommodation, food, activities, 
              colors=['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'])

plt.title('Monthly Travel Expenses', fontdict={'fontsize': 18}, loc='right')
plt.xlabel('Month')
plt.ylabel('Expenses ($)')
plt.legend(['Transport', 'Accommodation', 'Food', 'Activities'], loc='upper left')

peak_food_month = months[food.index(max(food))]
peak_food_value = max(food)
plt.text(peak_food_month, peak_food_value, 'Peak Food', ha='center', va='bottom')

plt.show()