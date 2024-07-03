
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
running_distance = [40, 50, 60, 75, 90, 110, 100, 85, 75, 65, 55, 50]
calories_burned = [350, 400, 450, 500, 600, 750, 700, 600, 550, 500, 450, 400]

month_numbers = [i+1 for i, _ in enumerate(months)]

plt.figure(figsize=(14, 7))
plt.scatter(month_numbers, running_distance, c=['#FF5733', '#33FF57', '#3357FF', '#FF33A6',
                                                '#FFC300', '#DAF7A6', '#C70039', '#581845',
                                                '#900C3F', '#FF5733', '#33FF57', '#FFC300'],
            s=calories_burned, alpha=0.7)

plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Running Distance (km)')
plt.title('Monthly Running Distance and Calories Burned', pad=20)
plt.xlim(0, 13)

plt.tight_layout()
plt.show()