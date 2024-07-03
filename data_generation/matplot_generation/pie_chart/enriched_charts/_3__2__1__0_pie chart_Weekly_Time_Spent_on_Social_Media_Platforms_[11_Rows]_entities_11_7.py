
import matplotlib.pyplot as plt

# Data
genres = ['Classical', 'Jazz', 'Rock', 'Pop', 'Hip-Hop', 'Electronic', 'Country', 'Folk']
percentages = [20, 15, 25, 10, 8, 12, 5, 5]
colors = ['#ff6666', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ffccff']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(14, 10))
ax.pie(percentages, labels=genres, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Distribution of Music Genres in 2022", pad=20)

# Display the chart
plt.show()