
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenues = [25, 30, 45, 40, 50, 55, 70, 65, 60, 75, 80, 85]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting the line chart
ax.plot(months, revenues, marker='o', linestyle='-', color='#ff7f0e')
ax.set(xlabel='Month', ylabel='Revenue (in thousands $)', title='Monthly Revenue Trends')

# Annotation
for i, txt in enumerate(revenues):
    ax.annotate(txt, (months[i], revenues[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Display the plot
plt.show()