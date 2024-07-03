
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
hours_reading = [10, 12, 15, 14, 18, 20, 22, 21, 19, 17, 16, 13]

plt.figure(figsize=(16, 8))
plt.fill_between(months, hours_reading, color='#1E90FF')
plt.title('Monthly Reading Hours Throughout the Year', fontsize=18, loc='center')
plt.xlabel('Month')
plt.ylabel('Hours of Reading')
plt.grid(True)
for i, txt in enumerate(hours_reading):
    plt.annotate(txt, (months[i], hours_reading[i]), textcoords="offset points", xytext=(0, 5), ha='center')
plt.show()