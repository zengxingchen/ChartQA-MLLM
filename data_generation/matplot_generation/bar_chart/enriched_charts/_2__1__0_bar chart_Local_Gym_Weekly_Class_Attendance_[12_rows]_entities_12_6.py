
import matplotlib.pyplot as plt

# Data
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Romance', 'Science Fiction', 
          'Fantasy', 'Biography', 'History', 'Poetry', 'Graphic Novels',
          "Children's Books", 'Young Adult', 'Self-Help', 'Travel', 'Cookbooks', 'Education']
books_published = [1500, 800, 600, 700, 450, 
                   500, 300, 250, 150, 200, 
                   900, 650, 400, 350, 500, 100]

# Create horizontal bar chart
plt.figure(figsize=(10, 8))  # Change width and height of the chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#9edae5', '#c49c94', '#f7b6d2', '#dbdb8d', '#c7c7c7', '#ff9896']

plt.barh(genres, books_published, color=colors, height=0.5)  # Change direction of chart and bar height

# Customizing the plot
plt.xlabel('Number of Books Published')
plt.title('Number of Books Published by Genre (2020)', pad=20)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()