
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
box_office_revenue = [150, 140, 135, 130, 125, 120, 115, 110, 100, 90, 85, 80]

# Create a new figure with specific width and height
plt.figure(figsize=(10, 8))

# Plotting the line chart with a specific color scheme
plt.plot(months, box_office_revenue, marker='s', linestyle='-', color='#FF5733')  # Orange color

# Assign annotations/labels to specific data points to provide additional information
for i, revenue in enumerate(box_office_revenue):
    plt.annotate(str(revenue), xy=(months[i], revenue), xytext=(5, -10), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Box Office Revenue', pad=20)
plt.xlabel('Month')
plt.ylabel('Revenue (Million USD)')

# Show the plot
plt.show()