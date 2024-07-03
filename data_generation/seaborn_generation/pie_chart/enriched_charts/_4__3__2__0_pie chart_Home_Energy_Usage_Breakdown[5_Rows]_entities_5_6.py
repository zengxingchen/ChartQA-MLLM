
import matplotlib.pyplot as plt

# Data
fields = ['Fiction', 'Non-Fiction', 'Poetry', 'Drama', 'Mystery', 'Romance', 
          'Horror', 'Science Fiction', 'Fantasy', 'Historical', 'Adventure', 
          'Biography', 'Self-Help', 'Graphic Novel', 'Memoir']
values = [400, 350, 300, 250, 200, 180, 160, 140, 120, 100, 90, 80, 70, 60, 50]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF',
          '#FF8C33', '#33FF8C', '#FF3333', '#33FFD4', '#D4FF33',
          '#336FFF', '#FF33E5', '#33FFEC', '#FFA833', '#A8FF33']

# Pie chart
fig, ax = plt.subplots(figsize=(14, 10))  # Width, Height of the chart
ax.pie(values, labels=fields, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Popularity of Literary Genres', pad=20)
plt.show()