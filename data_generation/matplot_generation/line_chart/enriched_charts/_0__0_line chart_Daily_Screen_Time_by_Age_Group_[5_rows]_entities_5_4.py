
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [5, 8, 15, 22, 35, 45, 55, 60, 50, 40, 30, 15]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(14, 10))  # Change width and height of the chart

# Plotting the line chart
ax.plot(months, revenue, marker='o', linestyle='-', color='#ff7f0e')  # Change color scheme using specific color codes
ax.set(xlabel='Month', ylabel='Revenue (in $1000s)', title='Monthly Revenue for 2023')  # Update topic, headline, and data type

# Annotation
for i, txt in enumerate(revenue):
    ax.annotate(txt, (months[i], revenue[i]), textcoords="offset points", xytext=(0,10), ha='center')  # Assign annotation/label in the chart

# Display the plot
plt.show()