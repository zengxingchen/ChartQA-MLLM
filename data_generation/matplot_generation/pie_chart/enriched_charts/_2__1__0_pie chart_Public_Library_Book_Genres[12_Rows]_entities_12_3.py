
import matplotlib.pyplot as plt

# Data for the chart
genres = ['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Historical Fiction', 'Non-Fiction', 'Biography']
percentages = [20, 15, 25, 10, 10, 15, 5]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Create a pie chart
plt.figure(figsize=(12, 8))  # Set the width and height of the chart
plt.pie(percentages, labels=genres, autopct='%1.1f%%', colors=colors, startangle=90)

plt.title('Popular Book Genres in 2023', y=1.05)  # Change the headline to match the topic and position it to avoid overlap
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()