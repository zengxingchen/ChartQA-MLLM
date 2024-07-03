
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
steps = [12000, 11500, 13000, 14000, 16000, 15000, 15500, 17000, 16500, 17500, 16000, 18000]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the line chart
ax.plot(months, steps, marker='s', linestyle='--', color='#4682B4')

# Update topic, headline, and data type
ax.set(xlabel='Month', ylabel='Average Steps', title='Monthly Steps Count')

# Annotation
for i, txt in enumerate(steps):
    ax.annotate(txt, (months[i], steps[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Display the plot
plt.show()