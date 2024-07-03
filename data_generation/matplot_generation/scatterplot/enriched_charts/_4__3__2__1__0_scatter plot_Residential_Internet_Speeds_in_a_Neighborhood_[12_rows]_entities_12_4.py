
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
temperature = [5, 6, 10, 12, 15, 20, 25, 24, 20, 15, 10, 6]
humidity = [60, 62, 58, 55, 50, 45, 40, 42, 48, 52, 58, 60]

month_numbers = [i+1 for i, _ in enumerate(months)]

plt.figure(figsize=(18, 10))
plt.scatter(month_numbers, temperature, c=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', 
                                           '#A133FF', '#FF8333', '#33FFF5', '#FF5733', 
                                           '#33FFA1', '#5733FF', '#A1FF33', '#FF3357'],
            s=[h*2 for h in humidity], alpha=0.8)

plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature and Humidity', pad=30)
plt.xlim(0, 13)

plt.tight_layout()
plt.show()