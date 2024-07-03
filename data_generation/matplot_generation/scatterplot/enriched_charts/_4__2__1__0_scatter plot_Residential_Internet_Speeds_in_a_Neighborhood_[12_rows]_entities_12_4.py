
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
meditation_duration = [5, 7, 8, 10, 12, 15, 13, 11, 10, 9, 8, 7]
stress_levels = [70, 65, 60, 55, 50, 45, 48, 52, 55, 58, 62, 65]

month_numbers = [i+1 for i, _ in enumerate(months)]

plt.figure(figsize=(16, 8))
plt.scatter(month_numbers, meditation_duration, c=['#FF5733', '#33FF57', '#3357FF', '#FF33A6',
                                                   '#FFC300', '#DAF7A6', '#C70039', '#581845',
                                                   '#900C3F', '#FF5733', '#33FF57', '#FFC300'],
            s=stress_levels, alpha=0.7)

plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Meditation Duration (hours)')
plt.title('Monthly Meditation Duration and Stress Levels', pad=20)
plt.xlim(0, 13)

plt.tight_layout()
plt.show()