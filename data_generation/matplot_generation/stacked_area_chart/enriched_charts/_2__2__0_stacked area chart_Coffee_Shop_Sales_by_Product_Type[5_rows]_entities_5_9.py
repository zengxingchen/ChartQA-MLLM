
import matplotlib.pyplot as plt

# Table data of monthly activities
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
reading_books = [5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200]
watching_sports = [8000, 8300, 8500, 8700, 8900, 9100, 9300, 9500, 9700, 9900, 10100, 10300]
exercising = [3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200]

# Stacked area chart
plt.figure(figsize=(16, 10))
plt.stackplot(months, reading_books, watching_sports, exercising, 
              labels=['Reading Books', 'Watching Sports', 'Exercising'],
              colors=['#8A2BE2', '#5F9EA0', '#FF4500'])

# Customizing the plot with titles, labels and annotations
plt.title('Monthly Health and Fitness Activities in 2024', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Time Spent (Minutes)', fontsize=14)
plt.legend(loc='upper left')
plt.xticks(rotation=45, fontsize=12)

# Annotation example
peak_exercising = max(exercising)
peak_month = months[exercising.index(peak_exercising)]
plt.annotate(f'Peak Exercising\n{peak_exercising} mins',
             xy=(peak_month, peak_exercising),
             xytext=(peak_month, peak_exercising + 2000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()