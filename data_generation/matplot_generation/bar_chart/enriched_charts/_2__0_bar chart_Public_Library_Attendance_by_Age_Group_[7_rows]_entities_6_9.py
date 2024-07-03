
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
steps = [3000, 3500, 5000, 7000, 8000, 10000, 12000, 11000, 9000, 7500, 5000, 4000]

colors = ['#FFB6C1', '#FF69B4', '#FF1493', '#C71585', '#DB7093', '#FF4500', '#FF6347', '#FF7F50', '#FF8C00', '#FFA500', '#FFD700', '#FFFF00']

plt.figure(figsize=(12, 6))
bar_width = 0.5
plt.bar(months, steps, color=colors, width=bar_width)

plt.title('Average Daily Steps in a Year')
plt.ylabel('Average Steps')
plt.xlabel('Month')

plt.ylim([0, max(steps) + 2000])

plt.tight_layout()
plt.show()