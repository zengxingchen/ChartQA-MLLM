
import matplotlib.pyplot as plt

# Data
days = list(range(1, 366))
temperatures = [24 - 0.05 * day for day in days]  # Simulating a temperature trend

# Plotting
plt.figure(figsize=(10, 5))  # Change width and height

plt.plot(days, temperatures, color='#17becf')  # Using a specific color code

plt.title('Yearly Temperature Trend')  # Change the topic and headline
plt.xlabel('Day of the Year')
plt.ylabel('Average Temperature (°C)')

# Annotation
plt.annotate('Mid-year Dip', xy=(182, temperatures[181]), xytext=(100, temperatures[100] + 5),
             arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

plt.tight_layout()
plt.show()