
import matplotlib.pyplot as plt

# Define the data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
revenue = [1200, 1300, 1400, 1550, 1700, 1800, 1750, 1900, 1950, 2100, 2200, 2400]

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(months, revenue, color='#1E90FF', marker='s')  # Changed color scheme and added markers

# Customize the trend of the data by simulating a sudden revenue drop in July
revenue[6] = 1600
plt.plot(months, revenue, linestyle='--', color='green')  # Overlaying the modified trend line

# Assign annotation to the chart
for i, rev in enumerate(revenue):
    plt.annotate(f"${rev}", (months[i], revenue[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Monthly Sales Revenue in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(True)

# Display the plot
plt.show()