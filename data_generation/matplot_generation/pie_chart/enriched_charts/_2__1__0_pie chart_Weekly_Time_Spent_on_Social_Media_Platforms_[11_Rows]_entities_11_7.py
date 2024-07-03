
import matplotlib.pyplot as plt

# Data
activities = ['Walking', 'Running', 'Cycling', 'Swimming', 'Yoga', 'Weightlifting', 'Hiking', 'Other']
percentages = [25, 15, 10, 8, 12, 10, 10, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ffccff']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(12, 9))
ax.pie(percentages, labels=activities, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Distribution of Physical Activities in 2022", pad=20)

# Display the chart
plt.show()