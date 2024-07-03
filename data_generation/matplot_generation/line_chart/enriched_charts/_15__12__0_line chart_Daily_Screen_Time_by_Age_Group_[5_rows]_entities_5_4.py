
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
study_hours = [2, 2.5, 3, 3.5, 4, 4.5, 4, 3.5, 3, 2.5, 2, 1.5]

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(16, 8))

# Plotting the line chart
ax.plot(months, study_hours, marker='o', linestyle='-', color='#1f77b4')
ax.set(xlabel='Month', ylabel='Average Study Hours per Day', title='Monthly Average Study Hours in 2023')
ax.invert_yaxis()

# Annotation
for i, txt in enumerate(study_hours):
    ax.annotate(txt, (months[i], study_hours[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Display the plot
plt.show()