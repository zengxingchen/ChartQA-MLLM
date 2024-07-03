
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [5, 7, 10, 15, 20, 25, 30, 28, 22, 17, 10, 6]

# Create a new figure with specific width and height
plt.figure(figsize=(16, 8))

# Plotting the line chart with a specific color scheme
plt.plot(months, temperature, marker='o', linestyle='-', color='#4682B4')  # Steel Blue color

# Assign annotations/labels to specific data points to provide additional information
for i, temp in enumerate(temperature):
    plt.annotate(str(temp), xy=(months[i], temp), xytext=(5, 2), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Average Temperature', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

# Show the plot
plt.show()