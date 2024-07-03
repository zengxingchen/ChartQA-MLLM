
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_temperature_f = [32, 36, 45, 55, 65, 75, 85, 83, 70, 60, 50, 30]

# Modify color scheme with color codes, change figure size, change trend by slightly altering temperatures
plt.figure(figsize=(12, 8))
plt.plot(months, average_temperature_f, color='#ff5733', marker='o')  # Trend with color code

# Adding labels with annotations
for i, (month, temp) in enumerate(zip(months, average_temperature_f)):
    plt.annotate(f'{temp}°F', (month, temp), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Historical Monthly Temperatures in NYC', pad=20)
plt.xlabel('Month')
plt.ylabel('Temperature (°F)')

# Display chart
plt.show()