
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [-2, -1, 5, 11, 17, 22, 25, 24, 19, 13, 6, 0]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart

# Plotting the line chart
ax.plot(months, temperatures, marker='o', linestyle='-', color='#1f77b4')  # Change color scheme using specific color codes
ax.set(xlabel='Month', ylabel='Average Temperature (°C)', title='Monthly Average Temperatures')  # Update topic, headline, and data type

# Annotation
for i, txt in enumerate(temperatures):
    ax.annotate(txt, (months[i], temperatures[i]), textcoords="offset points", xytext=(0,10), ha='center')  # Assign annotation/label in the chart

# Display the plot
plt.show()