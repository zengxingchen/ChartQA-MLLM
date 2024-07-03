
import matplotlib.pyplot as plt

# Define the data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
new_patents_filed = [150, 170, 180, 190, 210, 230, 300, 250, 220, 210, 190, 180]

# Create the line chart
plt.figure(figsize=(12, 6))  # Changed width and height of the chart
plt.plot(months, new_patents_filed, color='#1f77b4', marker='o')  # Changed color scheme and added markers

# Customize the trend of the data by simulating a spike in July
new_patents_filed[6] = 300
plt.plot(months, new_patents_filed, linestyle='--', color='#ff7f0e')  # Overlaying the modified trend line

# Assign annotation to the chart
for i, patents in enumerate(new_patents_filed):
    plt.annotate(f"{patents}", (months[i], new_patents_filed[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Monthly New Patents Filed in 2023')
plt.xlabel('Month')
plt.ylabel('New Patents Filed')
plt.grid(True)

# Display the plot
plt.show()