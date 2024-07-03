
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [5, 10, 8, 15, 12, 18, 20, 25, 22, 28, 30, 35]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart

# Plotting the line chart
ax.plot(months, revenue, marker='s', linestyle='--', color='#ff5733')  # Change color scheme using specific color codes
ax.set(xlabel='Month', ylabel='Revenue (in thousands of $)', title='Monthly Revenue Analysis')  # Update topic, headline, and data type

# Annotation
for i, txt in enumerate(revenue):
    ax.annotate(txt, (months[i], revenue[i]), textcoords="offset points", xytext=(0,10), ha='center')  # Assign annotation/label in the chart

# Invert Y-axis
ax.invert_yaxis()

# Display the plot
plt.show()