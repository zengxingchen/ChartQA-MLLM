
import matplotlib.pyplot as plt

# Data to plot
labels = 'Fiction', 'Non-Fiction', 'Sci-Fi', 'Romance', 'Mystery', 'Biography'
sizes = [45, 25, 10, 8, 7, 5]
colors = ['#ff6347','#4682b4','#ffb6c1','#32cd32','#ff69b4','#8a2be2']

# Change the size of the figure (width, height)
plt.figure(figsize=(12, 8))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Book Genres Distribution', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()