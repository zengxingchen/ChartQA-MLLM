
import matplotlib.pyplot as plt

# Data provided:
data = [
    {'Genre': 'Fiction', 'Percentage': 24},
    {'Genre': 'Non-Fiction', 'Percentage': 20},
    {'Genre': 'Mystery', 'Percentage': 12},
    {'Genre': 'Biographies', 'Percentage': 10},
    {'Genre': 'Science Fiction', 'Percentage': 9},
    {'Genre': 'Self-Help', 'Percentage': 7},
    {'Genre': 'Graphic Novels', 'Percentage': 5},
    {'Genre': 'Romance', 'Percentage': 4},
    {'Genre': 'History', 'Percentage': 3},
    {'Genre': 'Travel', 'Percentage': 2},
    {'Genre': 'Cookbooks', 'Percentage': 2},
    {'Genre': 'Other', 'Percentage': 2}
]

# Prepare data for plotting:
genres = [item['Genre'] for item in data]
percentages = [item['Percentage'] for item in data]

# Determine pie chart colors and explode values to offset the first slice:
colors = plt.get_cmap('tab20').colors
explode = [0.1] + [0]* (len(genres) - 1)  # Only "explode" the first slice

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=genres, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)

# Add a title
plt.title('Book Genre Popularity')

# Display the pie chart
plt.show()