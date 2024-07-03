
import matplotlib.pyplot as plt

months = ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021', 
          'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 'Nov-2021', 'Dec-2021',
          'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022',
          'Jul-2022', 'Aug-2022', 'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022']

views = [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100,
         3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300]

likes = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220,
         230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340]

shares = [50, 60, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150,
          160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270]

plt.figure(figsize=(16, 8))

plt.stackplot(months, views, likes, shares,
              colors=['#ffcc99', '#66b3ff', '#99ff99'],
              labels=['Views', 'Likes', 'Shares'])

plt.legend(loc='upper right')
plt.title('Monthly Social Media Engagement', pad=20)
plt.xlabel('Month')
plt.ylabel('Count')

for i, view in enumerate(views):
    total = view + likes[i] + shares[i]
    plt.text(months[i], total, f'{total}', ha='center', va='bottom')

plt.tight_layout()
plt.show()