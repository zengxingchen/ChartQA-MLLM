
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
food_consumption = [150, 170, 160, 180, 200, 220, 210, 230, 240, 220, 200, 180]

# Create a new figure with specific width and height
plt.figure(figsize=(10, 8))

# Plotting the line chart with a specific color scheme
plt.plot(months, food_consumption, marker='o', linestyle='-', color='#FF5733')  # Orange color

# Assign annotations/labels to specific data points to provide additional information
for i, value in enumerate(food_consumption):
    plt.annotate(str(value), xy=(months[i], value), xytext=(5, -10), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Food Consumption', pad=20)
plt.xlabel('Month')
plt.ylabel('Food Consumption (Kg)')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()