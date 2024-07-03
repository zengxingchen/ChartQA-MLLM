
import matplotlib.pyplot as plt

# Data points
activities = [
    'Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Geothermal',
    'Tidal', 'Nuclear', 'Natural Gas', 'Coal', 'Oil'
]

popularity = [
    25.6, 22.1, 18.4, 12.7, 9.5,
    6.3, 3.9, 1.5, 0.8, 0.2
]

# Colors for each section
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF4',
    '#F4FF33', '#5733FF', '#FF8333', '#33FF83', '#FF5733'
]

# Resize the chart
plt.figure(figsize=(14, 8))

# Create the pie chart
plt.pie(popularity, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Renewable Energy Sources in 2023', pad=20)

# Display the chart
plt.show()