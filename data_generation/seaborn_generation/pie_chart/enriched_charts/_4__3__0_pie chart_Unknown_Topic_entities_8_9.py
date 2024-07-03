
import matplotlib.pyplot as plt

# Data points
genres = ['Pop', 'Rock', 'Hip-Hop', 'Jazz', 'Classical', 'Electronic', 'Country', 'Reggae']
percentages = [22.0, 18.0, 14.0, 10.0, 12.0, 9.0, 8.0, 7.0]
colors = ['#FF6347', '#1E90FF', '#32CD32', '#FFD700', '#8A2BE2', '#FF4500', '#4B0082', '#FF69B4']

# Create a pie chart
plt.figure(figsize=(10, 7))  # Modify the width and height of the chart
plt.pie(percentages, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Distribution of Popular Music Genres in 2023', pad=20)

# Display the chart
plt.show()