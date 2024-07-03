
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
number_of_events = [2, 3, 4, 6, 5, 8, 9, 7, 6, 4, 3, 2]

# Create a new figure with specific width and height
plt.figure(figsize=(12, 6))

# Plotting the line chart with a specific color scheme
plt.plot(months, number_of_events, marker='o', linestyle='-', color='#1f77b4')  # Blue color

# Assign annotations/labels to specific data points to provide additional information
for i, events in enumerate(number_of_events):
    plt.annotate(str(events), xy=(months[i], events), xytext=(5, 5), textcoords='offset points')

# Modify the chart title and labels
plt.title('Monthly Number of Events in Local Community', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Events')

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()