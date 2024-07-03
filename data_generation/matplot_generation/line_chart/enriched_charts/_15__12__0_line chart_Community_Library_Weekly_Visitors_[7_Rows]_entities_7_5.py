
import matplotlib.pyplot as plt

# Define the data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
rainfall = [50, 55, 60, 58, 62, 65, 70, 80, 75, 78, 80, 85]

# Create the line chart
plt.figure(figsize=(10, 5))  # Changed width and height of the chart
plt.plot(months, rainfall, color='#2E86C1', marker='o')  # Changed color scheme and added markers

# Customize the trend of the data by simulating a sudden increase in August
rainfall[7] = 90
plt.plot(months, rainfall, linestyle='--', color='#28B463')  # Overlaying the modified trend line

# Assign annotation to the chart
for i, rain in enumerate(rainfall):
    plt.annotate(f"{rain}mm", (months[i], rainfall[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Axes and title
plt.title('Monthly Average Rainfall in City X (Sudden Increase in August)', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')
plt.gca().invert_yaxis()  # Invert y-axis
plt.grid(True)

# Display the plot
plt.show()