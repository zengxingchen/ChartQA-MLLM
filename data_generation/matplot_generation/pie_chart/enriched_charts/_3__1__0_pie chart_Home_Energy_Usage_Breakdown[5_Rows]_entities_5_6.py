
import matplotlib.pyplot as plt

# Data
genres = ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Jazz',
          'Classical', 'Country', 'R&B', 'Reggae', 'Latin',
          'Blues', 'Soul', 'Metal', 'Indie', 'Folk']
listeners = [120.0, 85.0, 95.0, 75.0, 45.0,
             40.0, 55.0, 60.0, 30.0, 50.0,
             25.0, 35.0, 20.0, 15.0, 10.0]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33',
          '#8FFF33', '#33FFF0', '#FF3333', '#8C33FF', '#FFD433',
          '#33D4FF', '#8CFF33', '#FF3386', '#33FF8F', '#FF8F57']

# Pie chart
fig, ax = plt.subplots(figsize=(12, 9))  # Width, Height of the chart
ax.pie(listeners, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Most Popular Music Genres by Number of Listeners (Millions)', pad=20)
plt.show()