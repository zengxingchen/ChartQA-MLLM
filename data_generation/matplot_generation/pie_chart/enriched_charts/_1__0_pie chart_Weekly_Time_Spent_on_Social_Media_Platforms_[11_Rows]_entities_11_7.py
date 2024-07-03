
import matplotlib.pyplot as plt

# Data
disorders = ['Anxiety Disorders', 'Depressive Disorders', 'Bipolar Disorder', 'Schizophrenia', 
             'Obsessive-Compulsive Disorder', 'Post-Traumatic Stress Disorder', 'Eating Disorders', 'Other']
percentages = [31, 27, 4, 1, 2, 8, 9, 18]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ffccff']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(percentages, labels=disorders, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Distribution of Mental Health Disorders in 2022", pad=20)

# Display the chart
plt.show()