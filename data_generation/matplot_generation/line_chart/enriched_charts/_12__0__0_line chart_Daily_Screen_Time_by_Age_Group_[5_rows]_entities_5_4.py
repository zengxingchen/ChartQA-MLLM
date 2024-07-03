
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
views = [120, 150, 180, 210, 250, 300, 350, 320, 280, 260, 230, 200]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(16, 8))  # Change width and height of the chart

# Plotting the line chart
ax.plot(months, views, marker='o', linestyle='-', color='#1f77b4')  # Change color scheme using specific color codes
ax.set(xlabel='Month', ylabel='Views (in thousands)', title='Monthly Video Views in 2023')  # Update topic, headline, and data type

# Annotation
for i, txt in enumerate(views):
    ax.annotate(txt, (months[i], views[i]), textcoords="offset points", xytext=(0,10), ha='center')  # Assign annotation/label in the chart

# Display the plot
plt.show()