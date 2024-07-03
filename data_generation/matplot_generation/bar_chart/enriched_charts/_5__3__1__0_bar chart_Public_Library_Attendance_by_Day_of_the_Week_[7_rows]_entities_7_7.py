
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
expenditure = [12.4, 14.2, 15.8, 17.9, 20.1, 21.7, 22.9, 23.5, 22.4, 19.7, 16.8, 14.9]
colors = ['#6A5ACD', '#7FFF00', '#FF4500', '#DA70D6', '#20B2AA', '#778899',
          '#4682B4', '#D2691E', '#FF1493', '#ADFF2F', '#32CD32', '#FF6347']

plt.figure(figsize=(12, 6))
bars = plt.bar(months, expenditure, color=colors, edgecolor='black', width=0.5)

plt.ylabel('Monthly Expenditure (Million $)')
plt.title('Monthly Expenditure on Outdoor Activities in 2023')
plt.ylim(10, max(expenditure) + 5)
plt.tight_layout()

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()