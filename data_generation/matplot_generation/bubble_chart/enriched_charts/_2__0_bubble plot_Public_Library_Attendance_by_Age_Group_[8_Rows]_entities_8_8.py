
import matplotlib.pyplot as plt

# Data
categories = ['Fiction', 'Non-Fiction', "Children's Books", 'Young Adult', 'Mystery', 'Science Fiction', 'Fantasy', 'Biography', 'Self-Help', 'Comics', 'Poetry', 'Cookbooks', 'Graphic Novels', 'History', 'Travel', 'Art & Design', 'Health & Wellness', 'Education', 'Religion & Spirituality', 'Science', 'Sports', 'Entertainment', 'Romance', 'Politics', 'Technology', 'Philosophy', 'Gardening', 'Pets', 'Humor']
average_sales = [500, 300, 450, 350, 250, 200, 300, 150, 100, 350, 50, 75, 400, 225, 175, 275, 125, 275, 150, 100, 225, 200, 300, 100, 150, 75, 50, 125, 225]
sales_numbers = [100000, 60000, 75000, 85000, 50000, 40000, 65000, 30000, 20000, 70000, 15000, 25000, 80000, 45000, 35000, 55000, 25000, 50000, 30000, 20000, 45000, 40000, 60000, 20000, 30000, 15000, 10000, 25000, 45000]

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', '#393b79', '#5254a3', '#6b6ecf', '#9c9ede', '#637939', '#8ca252', '#b5cf6b', '#cedb9c', '#8c6d31']

# Set the figure size
plt.figure(figsize=(14, 10))

# Scatter plot with bubble sizes
bubble_sizes = [n / 500 for n in sales_numbers]  # Scaling the number of sales for bubble size
plt.scatter(categories, average_sales, s=bubble_sizes, c=colors, alpha=0.6)

# Labels and title
plt.xlabel('Book Category')
plt.ylabel('Average Monthly Book Sales')
plt.title('Average Monthly Book Sales by Category in a Hypothetical Bookstore')

# Rotate category labels for better readability
plt.xticks(rotation=45, ha='right')

# Show plot
plt.show()