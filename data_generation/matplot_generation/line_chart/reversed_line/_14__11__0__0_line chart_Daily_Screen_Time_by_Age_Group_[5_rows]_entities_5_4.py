
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [15, 12, 18, 22, 30, 28, 38, 35, 42, 45, 40, 50]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(14, 7))

# Plotting the line chart
ax.plot(months, revenue, marker='o', linestyle='-', color='#ff6347')
ax.set(xlabel='Month', ylabel='Revenue (in $1000s)', title='Monthly Revenue for Entertainment & Leisure 2023')
ax.invert_yaxis()

# Annotation
for i, txt in enumerate(revenue):
    ax.annotate(txt, (months[i], revenue[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Display the plot
plt.show()