
import matplotlib.pyplot as plt

# Data for the chart
genres = ['Jazz', 'Classical', 'Rock', 'Pop', 'Hip-Hop', 'Country', 'Electronic']
percentages = [20, 10, 30, 15, 5, 10, 10]
colors = ['#3498db', '#e74c3c', '#f1c40f', '#2ecc71', '#9b59b6', '#34495e', '#e67e22']

# Create a pie chart
plt.figure(figsize=(10, 6))  # Set the width and height of the chart
plt.pie(percentages, labels=genres, autopct='%1.1f%%', colors=colors, startangle=90)

plt.title('Popular Music Genres in 2023', y=1.08)  # Change the headline to match the topic and position it to avoid overlap
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()