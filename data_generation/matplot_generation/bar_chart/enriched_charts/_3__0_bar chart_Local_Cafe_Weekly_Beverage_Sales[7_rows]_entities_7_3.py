
import matplotlib.pyplot as plt

# Data points
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Romance', 'Science Fiction', 
          'Fantasy', 'Biography', 'Self-Help', 'Historical', "Children's", 
          'Horror', 'Poetry']
book_sales = [55000, 47000, 62000, 49000, 56000, 61000, 43000, 45000, 52000, 
              53000, 44000, 39000]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF1', 
          '#A133FF', '#FF8633', '#33FFA1', '#A1FF33', '#3383FF', 
          '#FF3333', '#33FF83']

# Creating vertical bar chart
plt.figure(figsize=(12, 10)) # changing the width and height of the chart
plt.bar(genres, book_sales, color=colors, edgecolor='black', width=0.6) # changed direction, color, and band width

# Customizing the chart
plt.xlabel('Book Genre', fontsize=12)
plt.ylabel('Book Sales in Units', fontsize=12)
plt.title('Annual Book Sales by Genre for 2021', fontsize=16)
plt.ylim(0, 65000) # Adjust the y-axis to accommodate the data range

# Display the chart
plt.tight_layout()
plt.show()