
import matplotlib.pyplot as plt

# Define the data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
new_patents_filed = [160, 180, 200, 220, 240, 260, 320, 280, 260, 250, 230, 210]

# Create the line chart
plt.figure(figsize=(14, 7))  # Changed width and height of the chart
plt.plot(months, new_patents_filed, color='#2ca02c', marker='D')  # Changed color scheme and added markers

# Assign annotation to the chart
for i, patents in enumerate(new_patents_filed):
    plt.annotate(f"{patents}", (months[i], new_patents_filed[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Monthly New Patents Filed in 2023', fontsize=16)
plt.xlabel('Month')
plt.ylabel('New Patents Filed')
plt.grid(True)

# Display the plot
plt.show()