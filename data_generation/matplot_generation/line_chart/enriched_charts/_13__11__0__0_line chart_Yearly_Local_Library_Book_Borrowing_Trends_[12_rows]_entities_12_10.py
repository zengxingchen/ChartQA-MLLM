
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
water_consumption = [1.2, 1.5, 1.8, 2.0, 2.5, 2.8, 3.0, 2.9, 2.6, 2.3, 2.0, 1.5]

# Creating the line chart
plt.figure(figsize=(12, 6))

plt.plot(months, water_consumption, color="#1E90FF", marker='o')

# Annotating the highest and lowest water consumption
plt.annotate('Highest\n3.0 liters', xy=("July", 3.0), xytext=("July", 3.1),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n1.2 liters', xy=("January", 1.2), xytext=("January", 1.1),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')

# Title and labels
plt.title("Average Daily Water Consumption per Month", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Average Daily Water Consumption (liters)", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.7, color='grey')

# Show the plot
plt.show()