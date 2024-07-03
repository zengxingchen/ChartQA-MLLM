
import matplotlib.pyplot as plt

seasons = ['Winter', 'Spring', 'Summer', 'Autumn', 'Early Winter', 'Late Winter', 'Early Spring', 'Late Spring', 'Early Summer', 'Late Summer', 'Early Autumn', 'Late Autumn']
average_temperature = [5, 15, 30, 20, 10, 7, 12, 18, 28, 32, 22, 18]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A8', '#33FFA8', '#FFA833', '#A833FF', '#33A8FF', '#FF33FF', '#FF33A8', '#A8FF33']

plt.figure(figsize=(12, 6))
bar_width = 0.6
plt.bar(seasons, average_temperature, color=colors, width=bar_width)

plt.title('Average Seasonal Temperatures Throughout the Year', pad=20)
plt.ylabel('Average Temperature (°C)')
plt.xlabel('Season')

plt.ylim([0, max(average_temperature) + 5])

plt.tight_layout()
plt.show()