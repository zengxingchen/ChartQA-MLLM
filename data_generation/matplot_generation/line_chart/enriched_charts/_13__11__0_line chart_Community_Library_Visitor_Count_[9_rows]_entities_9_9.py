
import matplotlib.pyplot as plt

# Data for plotting
categories = ['Meditation', 'Running', 'Swimming', 'Yoga', 'Cycling', 'Dancing', 'Hiking', 'Weightlifting', 'Pilates', 'CrossFit', 'Tennis', 'Basketball']
percentage = [60, 55, 70, 50, 65, 75, 80, 45, 55, 50, 65, 70]

# Create a new figure with specific width and height
plt.figure(figsize=(16, 9))

# Plotting the line chart with a specific color scheme
plt.plot(categories, percentage, marker='o', linestyle='-', color='#4287f5')  # Blue color

# Assign annotations/labels to specific data points to provide additional information
for i, perc in enumerate(percentage):
    plt.annotate(str(perc), xy=(categories[i], perc), xytext=(5, 2), textcoords='offset points')

# Modify the chart title and labels
plt.title('Popularity of Various Physical Activities', pad=20)
plt.xlabel('Activity')
plt.ylabel('Participation Percentage (%)')

# Show the plot
plt.show()