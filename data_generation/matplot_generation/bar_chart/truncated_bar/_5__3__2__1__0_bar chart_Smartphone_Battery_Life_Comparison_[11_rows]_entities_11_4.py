
import matplotlib.pyplot as plt

# Book genre sales data
genres = [
    "Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery",
    "Romance", "Thriller", "Biography", "Self-Help", "Children's",
    "Historical Fiction", "Young Adult", "Graphic Novels", "Classics", 
    "Poetry", "Travel", "Cooking", "Art", "Comics", "Education",
    "Health", "Psychology", "Technology", "Business", "Sports",
    "Music", "Politics", "Economics", "Philosophy", "Anthropology",
    "Religion", "Spirituality", "Memoir"
]
sales = [
    1200, 1100, 950, 980, 880, 1020, 970, 1050, 950, 920, 
    990, 1080, 870, 890, 860, 900, 930, 910, 880, 1070, 
    950, 960, 940, 1010, 980, 930, 920, 980, 910, 900, 
    870, 890, 900
]

# New color scheme using specific color codes for each genre
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', 
    '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#aec7e8', '#ffbb78', '#98df8a'
]

# Create horizontal bar chart
plt.figure(figsize=(12, 18))  # Width and height of the chart
plt.barh(genres, sales, color=colors, height=0.6)  # Bar color and bar height

# Set the title and labels
plt.title('Book Sales by Genre', fontsize=18, pad=20)
plt.xlabel('Sales (in thousands)', fontsize=16)
plt.ylabel('Genre', fontsize=16)

# Set y-axis limit to start from 800 for a truncated bar chart
plt.xlim(800, 1250)

# Display the bar chart
plt.show()