
import matplotlib.pyplot as plt

# Data for the chart
topics = ['Primary Education', 'Secondary Education', 'Higher Education', 'Vocational Training', 'Special Education', 'Adult Education', 'Online Learning']
percentages = [15, 20, 25, 10, 5, 15, 10]
colors = ['#ff6666', '#ffcc66', '#99cc99', '#66b3ff', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Create a pie chart
plt.figure(figsize=(12, 8))  # Set the width and height of the chart
plt.pie(percentages, labels=topics, autopct='%1.1f%%', colors=colors, startangle=90)

plt.title('Education Types Distribution in 2023', y=1.05)  # Change the headline to match the topic and position it to avoid overlap
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()