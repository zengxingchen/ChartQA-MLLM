
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_temperature_f = [35, 38, 50, 60, 70, 80, 90, 88, 75, 65, 55, 40]

# Modify color scheme with color codes, change figure size, change trend by slightly altering temperatures
plt.figure(figsize=(14, 10))
plt.plot(months, average_temperature_f, color='#1f77b4', marker='o')  # Trend with color code

# Adding labels with annotations
for i, (month, temp) in enumerate(zip(months, average_temperature_f)):
    plt.annotate(f'{temp}°F', (month, temp), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Average Temperatures in NYC', pad=20, fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)

# Display chart
plt.show()