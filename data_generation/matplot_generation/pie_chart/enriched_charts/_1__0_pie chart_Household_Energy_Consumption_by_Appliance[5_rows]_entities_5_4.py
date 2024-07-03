
import matplotlib.pyplot as plt

# Data to plot
labels = 'Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy'
sizes = [35.4, 30.2, 15.6, 10.3, 8.5]
colors = ['#f4a582', '#92c5de', '#d6604d', '#4393c3', '#b2abd2']

# Create pie chart
plt.figure(figsize=(12, 9))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Popularity of Book Genres in 2023', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()