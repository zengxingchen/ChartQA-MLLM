
import matplotlib.pyplot as plt

# Define the data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
temperatures = [32.1, 34.7, 42.4, 53.0, 63.1, 72.5, 79.3, 78.1, 70.1, 57.9, 47.3, 36.5]

# Create the line chart
plt.figure(figsize=(10, 5)) # Changed width and height of the chart
plt.plot(months, temperatures, color='#FF5733', marker='o') # Changed color scheme and added markers

# Customize the trend of the data by simulating a sudden temperature drop in July
temperatures[6] = 68
plt.plot(months, temperatures, linestyle='--', color='blue') # Overlaying the modified trend line

# Assign annotation to the chart
for i, temp in enumerate(temperatures):
    plt.annotate(f"{temp}°F", (months[i], temperatures[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Average Monthly Temperatures in NYC (Modifying July Temp)')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°F)')
plt.grid(True)

# Display the plot
plt.show()