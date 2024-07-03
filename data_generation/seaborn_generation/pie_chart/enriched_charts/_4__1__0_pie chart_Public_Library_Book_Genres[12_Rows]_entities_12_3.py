
import matplotlib.pyplot as plt

# Data for the chart
sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
percentages = [35, 30, 20, 10, 5]
colors = ['#FFD700', '#32CD32', '#1E90FF', '#FF69B4', '#8A2BE2']

# Create a pie chart
plt.figure(figsize=(12, 8))  # Set the width and height of the chart
plt.pie(percentages, labels=sources, autopct='%1.1f%%', colors=colors, startangle=140)

plt.title('Renewable Energy Sources in 2023', pad=20)  # Change the headline to match the topic, added padding
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()