
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_temperature_f = [32, 35, 42, 53, 62, 71, 76, 75, 68, 57, 47, 38]

# Changes to data to enrich visualization (slightly warmer July and colder December for example)
average_temperature_f[6] += 1  # July
average_temperature_f[-1] -= 2  # December

# Modify color scheme with color codes, change figure size, change trend by inversing the temperature
plt.figure(figsize=(10, 6))
plt.plot(months, [max(average_temperature_f) + min(average_temperature_f) - temp for temp in average_temperature_f], 
         color='#1f77b4', marker='o')  # Inverse trend with color code

# Adding labels with annotations
for i, (month, temp) in enumerate(zip(months, average_temperature_f)):
    inverse_temp = max(average_temperature_f) + min(average_temperature_f) - temp
    plt.annotate(f'{temp}°F', (month, inverse_temp), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('NYC Historical Average Monthly Temperatures - Inverted Trend')
plt.xlabel('Month')
plt.ylabel('Temperature (°F)')

# Display chart
plt.show()