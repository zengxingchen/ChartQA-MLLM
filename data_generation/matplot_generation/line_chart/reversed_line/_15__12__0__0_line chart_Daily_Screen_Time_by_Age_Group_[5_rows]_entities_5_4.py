
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
views = [200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 30, 10]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(12, 6))  # Change width and height of the chart

# Plotting the line chart
ax.plot(months, views, marker='o', linestyle='-', color='#ff5733')  # Change color scheme using specific color codes
ax.set(xlabel='Month', ylabel='Views (in hundreds)', title='Monthly Video Views in 2023 - Entertainment & Leisure')  # Update topic, headline, and data type
ax.invert_yaxis()  # Invert y-axis

# Annotation
for i, txt in enumerate(views):
    ax.annotate(txt, (months[i], views[i]), textcoords="offset points", xytext=(0,10), ha='center')  # Assign annotation/label in the chart

# Display the plot
plt.show()