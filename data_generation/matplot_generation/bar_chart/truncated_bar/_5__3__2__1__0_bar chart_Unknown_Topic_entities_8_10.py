
import matplotlib.pyplot as plt

# Data
genres = [
    'Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 
    'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'Western', 'Documentary', 
    'Musical', 'Animation', 'Biographical', 'Historical', 'Crime', 
    'Family', 'Sports', 'War'
]
sales = [
    68, 48, 57, 84, 49, 30, 
    34, 27, 63, 45, 12, 20, 
    18, 55, 36, 23, 41, 
    33, 29, 16
]

# Plotting the bar chart
plt.figure(figsize=(12, 8))
plt.bar(genres, sales, width=0.6, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#dbdb8d', 
    '#9edae5', '#ffbb78', '#98df8a', '#ff9896', '#c7c7c7'
])

# Customizing the plot
plt.ylabel('Sales in Millions')
plt.title('Top Movie Genres by Sales', pad=20)
plt.ylim(10, 90)
plt.yticks(rotation=45)

# Show the plot
plt.show()