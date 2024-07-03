
import matplotlib.pyplot as plt

months = [
    'Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021',
    'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 'Nov-2021', 'Dec-2021',
    'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022',
    'Jul-2022', 'Aug-2022', 'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'
]
north_america = [
    120, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235,
    245, 255, 265, 275, 285, 295, 305, 315, 325, 335, 345, 355
]
europe = [
    95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205,
    215, 225, 235, 245, 255, 265, 275, 285, 295, 305, 315, 325
]
asia_pacific = [
    70, 80, 95, 100, 110, 120, 130, 140, 150, 160, 170, 180,
    190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300
]

plt.figure(figsize=(14, 9))

plt.stackplot(months, north_america, europe, asia_pacific,
              colors=['#FF5733', '#33FF57', '#3357FF'],
              labels=['North America', 'Europe', 'Asia-Pacific'])

plt.legend(loc='upper left')

plt.title('Monthly Concert Ticket Sales by Region', pad=20)
plt.xlabel('Month')
plt.ylabel('Ticket Sales (Thousands)')

for i, na in enumerate(north_america):
    total_sales = na + europe[i] + asia_pacific[i]
    plt.text(months[i], total_sales, f'{total_sales}K', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()