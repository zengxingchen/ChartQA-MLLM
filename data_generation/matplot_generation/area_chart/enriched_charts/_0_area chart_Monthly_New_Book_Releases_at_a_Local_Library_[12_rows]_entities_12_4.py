
import matplotlib.pyplot as plt

# Data for the area chart
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]

# Create the area chart
plt.figure(figsize=(10, 6))  # Modify the width and height of the chart
plt.fill_between(months, temperatures, color='#76B900')  # Use a specific color code

# Adding a title and labels
plt.title('Average Monthly Temperatures in Metropolis City', fontsize=14)  # Change the headline and topic
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Annotate the highest temperature
highest_temp_idx = temperatures.index(max(temperatures))
plt.annotate('Highest', xy=(months[highest_temp_idx], temperatures[highest_temp_idx]), 
             xytext=(months[highest_temp_idx], temperatures[highest_temp_idx]+2),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))  # Specific color code for annotation

# Customize ticks and grid
plt.xticks(rotation=45)
plt.yticks(range(0, max(temperatures)+5, 5))
plt.grid(True, linestyle='--', alpha=0.7)

# Display the chart
plt.tight_layout()
plt.show()