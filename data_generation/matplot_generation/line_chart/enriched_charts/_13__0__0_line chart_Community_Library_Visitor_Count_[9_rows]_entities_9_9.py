
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
steps = [5000, 4500, 5500, 6000, 6500, 6200, 7000, 6800, 7500, 7200, 6900, 7400]

# Create a new figure with specific width and height
plt.figure(figsize=(16, 8))

# Plotting the line chart with a specific color scheme
plt.plot(months, steps, marker='o', linestyle='-', color='#4682B4')  # SteelBlue color

# Assign annotations/labels to specific data points to provide additional information
for i, step in enumerate(steps):
    plt.annotate(str(step), xy=(months[i], step), xytext=(5, -15), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Step Count', pad=20)
plt.xlabel('Month')
plt.ylabel('Steps')

# Show the plot
plt.show()