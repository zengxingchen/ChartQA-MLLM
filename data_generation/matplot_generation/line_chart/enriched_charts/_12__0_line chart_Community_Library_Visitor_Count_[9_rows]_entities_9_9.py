
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
average_rainfall = [78, 64, 92, 110, 123, 138, 145, 130, 112, 85, 95, 70]

# Create a new figure with specific width and height
plt.figure(figsize=(14, 7))

# Plotting the line chart with a specific color scheme
plt.plot(months, average_rainfall, marker='o', linestyle='-', color='#ff7f0e')  # Orange color

# Assign annotations/labels to specific data points to provide additional information
for i, rainfall in enumerate(average_rainfall):
    plt.annotate(str(rainfall), xy=(months[i], rainfall), xytext=(5, 5), textcoords='offset points')

# Modify the chart title and labels
plt.title('Average Monthly Rainfall in Coastal City', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')

# Show the plot
plt.show()