
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
temp_city_a = [5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5]
temp_city_b = [15.5, 15.0, 14.5, 14.0, 13.5, 13.0, 12.5, 12.0, 11.5, 11.0, 10.5, 10.0, 9.5, 9.0, 8.5, 8.0, 7.5, 7.0, 6.5, 6.0, 5.5, 5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5]

plt.figure(figsize=(14, 8))
plt.plot(days, temp_city_a, color='#008080', label='City A')  # Teal
plt.plot(days, temp_city_b, color='#800080', label='City B')  # Purple

plt.title('Average Daily Temperatures in January')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°C)')

plt.annotate('City A Peak', xy=(31, temp_city_a[-1]), xytext=(25, temp_city_a[-5]),
             arrowprops=dict(facecolor='#008080', shrink=0.05))

plt.annotate('City B Low', xy=(31, temp_city_b[-1]), xytext=(25, temp_city_b[-5]),
             arrowprops=dict(facecolor='#800080', shrink=0.05))

plt.grid(True)
plt.legend()
plt.show()