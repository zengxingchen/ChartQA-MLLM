
import matplotlib.pyplot as plt

# Data for the chart
topics = ['Renewable Energy', 'Fossil Fuels', 'Nuclear Power', 'Hydropower', 'Wind Energy', 'Solar Energy', 'Geothermal']
percentages = [22, 18, 12, 14, 20, 10, 4]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Create a pie chart
plt.figure(figsize=(10, 7))  # Set the width and height of the chart
plt.pie(percentages, labels=topics, autopct='%1.1f%%', colors=colors, startangle=140)

plt.title('Energy Sources Distribution in 2023', y=1.08)  # Change the headline to match the topic and position it to avoid overlap
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()