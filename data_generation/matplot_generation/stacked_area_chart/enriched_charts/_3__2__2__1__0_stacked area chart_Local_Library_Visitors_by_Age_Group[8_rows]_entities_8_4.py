
import matplotlib.pyplot as plt

months = ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021', 
          'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 'Nov-2021', 'Dec-2021',
          'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022',
          'Jul-2022', 'Aug-2022', 'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022']

calories = [2100, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950, 3050, 3150,
            3250, 3350, 3450, 3550, 3650, 3750, 3850, 3950, 4050, 4150, 4250, 4350]

beverages = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520,
             540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760]

proteins = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260,
            270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380]

plt.figure(figsize=(18, 9))

plt.stackplot(months, calories, beverages, proteins,
              colors=['#e6194b', '#3cb44b', '#ffe119'],
              labels=['Calories', 'Beverages', 'Proteins'])

plt.legend(loc='upper left')
plt.title('Monthly Food Consumption', pad=20)
plt.xlabel('Month')
plt.ylabel('Quantity (in units)')

for i, calorie in enumerate(calories):
    total = calorie + beverages[i] + proteins[i]
    plt.text(months[i], total, f'{total}', ha='center', va='bottom')

plt.tight_layout()
plt.show()