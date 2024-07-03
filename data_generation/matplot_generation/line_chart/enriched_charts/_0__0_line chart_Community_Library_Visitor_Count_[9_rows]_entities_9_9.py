
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
streaming_hours = [120, 150, 130, 160, 200, 220, 180, 210, 190, 170, 160, 180]

# Create a new figure with specific width and height
plt.figure(figsize=(14, 7))

# Plotting the line chart with a specific color scheme
plt.plot(months, streaming_hours, marker='o', linestyle='-', color='#FF6347')  # Tomato color

# Assign annotations/labels to specific data points to provide additional information
for i, hours in enumerate(streaming_hours):
    plt.annotate(str(hours), xy=(months[i], hours), xytext=(5, 2), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Streaming Hours')
plt.xlabel('Month')
plt.ylabel('Streaming Hours')

# Show the plot
plt.show()