
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weight_kg = [90, 88, 85, 83, 80, 78, 75, 73, 70, 68, 65, 63]

# Create a new figure with specific width and height
plt.figure(figsize=(12, 6))

# Plotting the line chart with a specific color scheme
plt.plot(months, weight_kg, marker='o', linestyle='-', color='#d62728')  # Red color

# Assign annotations/labels to specific data points to provide additional information
for i, weight in enumerate(weight_kg):
    plt.annotate(str(weight), xy=(months[i], weight), xytext=(5, 2), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Weight Loss Progress', pad=20)
plt.xlabel('Month')
plt.ylabel('Weight (kg)')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()