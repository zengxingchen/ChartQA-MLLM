
import matplotlib.pyplot as plt

# Data
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Thriller', 'Romance', 
          'Biography', 'History', 'Poetry', 'Drama', 'Philosophy', 'Self-Help', "Children's", 
          'Travel', 'Comics', 'Cookbooks', 'Art', 'Religion', 'Health', 'Science', 'Education', 
          'Business', 'Technology', 'Music']
books_published = [1200, 980, 450, 400, 350, 320, 300, 250, 220, 180, 150, 130, 110, 100, 90, 80, 
                   70, 60, 50, 40, 30, 20, 15, 10, 5]

# Create horizontal bar chart
plt.figure(figsize=(14, 10))  # Change width and height of the chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFA6', '#FFA633', 
          '#5733FF', '#33FFF3', '#A6FF33', '#33A6FF', '#FF5733', '#33FF57', '#3357FF', 
          '#FF33A6', '#A633FF', '#33FFA6', '#FFA633', '#5733FF', '#33FFF3', '#A6FF33', 
          '#33A6FF', '#FF5733', '#33FF57', '#3357FF']

plt.barh(genres, books_published, color=colors, height=0.5)  # Change direction of chart and bar height

# Customizing the plot
plt.xlabel('Books Published (in thousands)')
plt.title('Number of Books Published by Genre (2020)', pad=20)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()