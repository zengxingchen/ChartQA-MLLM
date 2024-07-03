
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
temperatures = [5, 6, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]

# Modify the plot size
plt.figure(figsize=(12, 8))

# Create a horizontal histogram
plt.barh(months, temperatures, color="#3498db", edgecolor="#2980b9", height=0.5)  # Adjusted band height and color

# Customize the display
plt.xlabel('Average Temperature (°C)', fontsize=12)
plt.ylabel('Month', fontsize=12)
plt.title('Average Monthly Temperatures in a City', fontsize=14)

# Show grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the histogram
plt.show()