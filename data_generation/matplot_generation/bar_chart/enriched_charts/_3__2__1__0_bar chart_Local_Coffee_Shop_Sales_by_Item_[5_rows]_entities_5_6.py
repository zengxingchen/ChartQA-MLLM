
import matplotlib.pyplot as plt

months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
temperatures = [
    5, 7, 10, 13, 18, 22,
    25, 24, 20, 15, 10, 6
]

plt.figure(figsize=(10, 14))

bar_width = 0.5
plt.bar(months, temperatures, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF',
    '#FF8333', '#33FFF2', '#F2FF33', '#FF3333', '#33A8FF',
    '#5733FF', '#33FF83'
], width=bar_width)

plt.ylabel('Temperature (°C)', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.title('Monthly Average Temperatures', fontsize=16)

plt.xticks(months, fontsize=10)

plt.show()