import matplotlib.pyplot as plt

months = [
    'Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021',
    'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 'Nov-2021', 'Dec-2021',
    'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022',
    'Jul-2022', 'Aug-2022', 'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'
]
usa = [
    110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330,
    350, 370, 390, 410, 430, 450, 470, 490, 510, 530, 550, 570
]
europe = [
    100, 115, 130, 140, 155, 170, 185, 200, 210, 225, 240, 255,
    265, 280, 295, 310, 320, 335, 350, 365, 375, 390, 405, 420
]
asia_pacific = [
    90, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195,
    205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305, 315
]

plt.figure(figsize=(16, 10))

plt.stackplot(months, usa, europe, asia_pacific,
              colors=['#FF6347', '#4682B4', '#9ACD32'],
              labels=['USA', 'Europe', 'Asia-Pacific'])

plt.legend(loc='upper left')

plt.title('Monthly Smartphone Sales by Region', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales (Thousands)')

for i, us in enumerate(usa):
    total_sales = us + europe[i] + asia_pacific[i]
    plt.text(months[i], total_sales, f'{total_sales}K', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()