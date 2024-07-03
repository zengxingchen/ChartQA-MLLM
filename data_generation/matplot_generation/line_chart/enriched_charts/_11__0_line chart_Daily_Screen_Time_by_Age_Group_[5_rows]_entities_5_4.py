
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [-1, 0, 4, 10, 15, 20, 24, 23, 18, 12, 5, 1]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the line chart
ax.plot(months, temperatures, marker='o', linestyle='-', color='#ff6347')

# Update topic, headline, and data type
ax.set(xlabel='Month', ylabel='Average Temperature (°C)', title='Monthly Temperature Trend')

# Annotation
for i, txt in enumerate(temperatures):
    ax.annotate(txt, (months[i], temperatures[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Display the plot
plt.show()