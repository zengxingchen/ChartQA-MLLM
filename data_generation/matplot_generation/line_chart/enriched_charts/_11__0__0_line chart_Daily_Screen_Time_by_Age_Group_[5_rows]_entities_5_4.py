
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [12, 18, 25, 20, 28, 35, 45, 42, 38, 30, 22, 15]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(16, 8))  # Change width and height of the chart

# Plotting the line chart
ax.plot(months, revenue, marker='o', linestyle='-', color='#1f77b4')  # Change color scheme using specific color codes
ax.set(xlabel='Month', ylabel='Revenue (in $1000s)', title='Monthly Revenue for Art & Design 2023')  # Update topic, headline, and data type

# Annotation
for i, txt in enumerate(revenue):
    ax.annotate(txt, (months[i], revenue[i]), textcoords="offset points", xytext=(0,10), ha='center')  # Assign annotation/label in the chart

# Display the plot
plt.show()