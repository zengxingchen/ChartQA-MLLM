
import matplotlib.pyplot as plt

# Data
genres = [
    'Fantasy', 'Mystery', 'Romance', 'Science Fiction', 
    'Non-Fiction', 'Historical', 'Horror'
]
percentages = [25.5, 20.0, 18.0, 15.5, 10.5, 7.0, 3.5]

# Colors
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', 
    '#A133FF', '#FFD733', '#33FFF5'
]

# Plot
plt.figure(figsize=(10, 8))  # Width and height of the chart
plt.pie(percentages, labels=genres, colors=colors, startangle=140, autopct='%1.1f%%')

plt.title("Popular Book Genres in 2023", pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()