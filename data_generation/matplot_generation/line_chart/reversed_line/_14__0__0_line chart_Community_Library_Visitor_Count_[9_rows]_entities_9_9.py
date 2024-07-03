
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
visitors = [220, 210, 230, 240, 270, 290, 300, 310, 320, 280, 260, 250]

# Create a new figure with specific width and height
plt.figure(figsize=(16, 8))

# Plotting the line chart with a specific color scheme
plt.plot(months, visitors, marker='s', linestyle='-', color='#4682B4')  # SteelBlue color

# Assign annotations/labels to specific data points to provide additional information
for i, count in enumerate(visitors):
    plt.annotate(str(count), xy=(months[i], count), xytext=(5, -10), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Visitors to National Parks', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()