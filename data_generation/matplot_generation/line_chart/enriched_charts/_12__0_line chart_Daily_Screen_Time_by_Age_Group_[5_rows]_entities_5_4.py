
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calorie_intake = [2000, 1900, 2100, 2200, 2300, 2400, 2500, 2400, 2300, 2200, 2100, 2000]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(14, 9))  # Change width and height of the chart

# Plotting the line chart
ax.plot(months, calorie_intake, marker='s', linestyle='-', color='#ff7f0e')  # Change color scheme using specific color codes
ax.set(xlabel='Month', ylabel='Average Calorie Intake (kcal)', title='Monthly Average Calorie Intake')  # Update topic, headline, and data type

# Annotation
for i, txt in enumerate(calorie_intake):
    ax.annotate(txt, (months[i], calorie_intake[i]), textcoords="offset points", xytext=(0,10), ha='center')  # Assign annotation/label in the chart

# Display the plot
plt.show()