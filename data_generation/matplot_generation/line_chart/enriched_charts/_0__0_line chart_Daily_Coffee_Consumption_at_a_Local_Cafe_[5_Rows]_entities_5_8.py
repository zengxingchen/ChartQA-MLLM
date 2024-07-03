
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
temp_city_a = [20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5]
temp_city_b = [22.5, 22.0, 21.5, 21.0, 20.5, 20.0, 19.5, 19.0, 18.5, 18.0, 17.5, 17.0, 16.5, 16.0, 15.5, 15.0, 14.5, 14.0, 13.5, 13.0, 12.5, 12.0, 11.5, 11.0, 10.5, 10.0, 9.5, 9.0, 8.5, 8.0, 7.5]

plt.figure(figsize=(12, 7))
plt.plot(days, temp_city_a, color='#FF4500', label='City A')  # OrangeRed
plt.plot(days, temp_city_b, color='#1E90FF', label='City B')  # DodgerBlue

plt.title('Daily High Temperatures in January')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°C)')

plt.annotate('City A Peak', xy=(31, temp_city_a[-1]), xytext=(25, temp_city_a[-5]),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.annotate('City B Low', xy=(31, temp_city_b[-1]), xytext=(25, temp_city_b[-5]),
             arrowprops=dict(facecolor='#1E90FF', shrink=0.05))

plt.grid(True)
plt.legend()
plt.show()