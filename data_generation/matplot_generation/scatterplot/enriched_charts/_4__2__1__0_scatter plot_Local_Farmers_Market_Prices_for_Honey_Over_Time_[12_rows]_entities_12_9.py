
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
calories_consumed = [2100, 2200, 2000, 2300, 2150, 2050, 2250, 2400, 2150, 2100, 2350, 2200, 2250, 2400, 2300, 2100, 2200, 2150, 2300, 2250, 2150, 2100, 2350, 2200, 2250, 2100, 2400, 2350, 2200, 2100, 2300]
sleep_hours = [7, 6.5, 8, 7.5, 7, 8, 6.5, 7, 6, 8, 7, 6.5, 7, 8, 6.5, 7, 8, 6.5, 7, 8, 6, 7.5, 6.5, 7, 8, 6, 7, 7.5, 6.5, 8, 7]

plt.figure(figsize=(14, 10))
plt.scatter(calories_consumed, sleep_hours, color='#1f77b4')
plt.xlabel('Calories Consumed')
plt.ylabel('Sleep Hours')
plt.title('Calories Consumed vs. Sleep Hours in a Month')
plt.show()