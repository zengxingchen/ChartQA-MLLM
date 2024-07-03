
import matplotlib.pyplot as plt

# Data for the chart
genres = ['Action', 'Adventure', 'Puzzle', 'Strategy', 'Simulation', 'Role-Playing', 'Sports']
percentages = [30, 25, 15, 10, 10, 5, 5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFF5', '#FF8F33']

# Create a pie chart
plt.figure(figsize=(10, 10))  # Set the width and height of the chart
plt.pie(percentages, labels=genres, autopct='%1.1f%%', colors=colors, startangle=140)

plt.title('Popular Game Genres in 2023')  # Change the headline to match the topic
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()