
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
average_running_distance = [5, 6, 8, 10, 12, 15, 18, 17, 14, 10, 7, 5]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF7',
          '#FFA833', '#8033FF', '#33FF80', '#FF3380', '#FF8033',
          '#FF3333', '#33A1FF']

plt.figure(figsize=(14, 8))
plt.barh(months, average_running_distance, color=colors, edgecolor='black', height=0.5)

plt.xlabel('Average Running Distance (miles)', fontsize=12)
plt.ylabel('Month', fontsize=12)
plt.title('Monthly Average Running Distance in 2021', fontsize=16, pad=20)
plt.xlim(4, 20)

plt.tight_layout()
plt.show()