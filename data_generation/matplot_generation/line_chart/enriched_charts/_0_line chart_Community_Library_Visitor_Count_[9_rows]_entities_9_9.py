
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_temperature = [2, 3, 6, 10, 15, 20, 25, 24, 19, 13, 7, 3]

# Create a new figure with specific width and height
plt.figure(figsize=(12, 6))

# Plotting the line chart with a specific color scheme
plt.plot(months, average_temperature, marker='o', linestyle='-', color='#1f77b4')  # Blue color

# Assign annotations/labels to specific data points to provide additional information
for i, temp in enumerate(average_temperature):
    plt.annotate(str(temp), xy=(months[i], temp), xytext=(5, 2), textcoords='offset points')

# Modify the chart title and labels
plt.title('Average Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('Average Temperature (Celsius)')

# Show the plot
plt.show()