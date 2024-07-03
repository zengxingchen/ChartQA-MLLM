
import matplotlib.pyplot as plt

# Data to plot
labels = ['Fiction', 'Non-Fiction', "Children's Books", 'Mystery', 'Romance', 'Sci-Fi', 'Biographies', 'Self-Help']
sizes = [25, 20, 15, 10, 10, 10, 5, 5]
colors = ['#ff7f50', '#6a5acd', '#ff4500', '#2e8b57', '#daa520', '#ff69b4', '#8a2be2', '#4682b4']

# Change the size of the figure (width, height)
plt.figure(figsize=(10, 10))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Book Genres in a Library', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()