
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [120, 90, 80, 70, 60, 50, 40, 45, 55, 65, 85, 100]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the line chart
ax.plot(months, rainfall, marker='o', linestyle='-', color='#1f77b4')

# Update topic, headline, and data type
ax.set(xlabel='Month', ylabel='Average Rainfall (mm)', title='Monthly Rainfall Trend')

# Annotation
for i, txt in enumerate(rainfall):
    ax.annotate(txt, (months[i], rainfall[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Invert y-axis
ax.invert_yaxis()

# Display the plot
plt.show()