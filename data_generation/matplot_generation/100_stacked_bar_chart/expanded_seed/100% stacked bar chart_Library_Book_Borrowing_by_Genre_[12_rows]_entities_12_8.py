
import matplotlib.pyplot as plt
import numpy as np

# The provided data
data = [
    {'Month': 'January', 'Mystery & Thriller': 120, 'Romance': 90, 'Science Fiction': 80, 'Fantasy': 110, 'Non-Fiction': 130, 'Biographies': 70, "Children's Literature": 140, 'Young Adult': 85, 'History': 65, 'Graphic Novels': 50, 'Cookbooks': 30, 'Self-Help': 40},
    {'Month': 'February', 'Mystery & Thriller': 85, 'Romance': 95, 'Science Fiction': 70, 'Fantasy': 90, 'Non-Fiction': 145, 'Biographies': 80, "Children's Literature": 150, 'Young Adult': 75, 'History': 70, 'Graphic Novels': 45, 'Cookbooks': 35, 'Self-Help': 50},
    # ... (include other months here)
    {'Month': 'December', 'Mystery & Thriller': 130, 'Romance': 140, 'Science Fiction': 110, 'Fantasy': 120, 'Non-Fiction': 180, 'Biographies': 115, "Children's Literature": 200, 'Young Adult': 110, 'History': 88, 'Graphic Novels': 77, 'Cookbooks': 65, 'Self-Help': 85}
]

# Extracting month labels
months = [entry['Month'] for entry in data]

# Extracting genre labels (all but the first key, Month)
genres = list(data[0].keys())[1:]

# Number of months and genres
num_months = len(months)
num_genres = len(genres)

# Preparing the data matrix and normalizing it to percentage
values = np.array([[entry[genre] for genre in genres] for entry in data], dtype=float)
sums_by_month = values.sum(axis=1)
percentages = (values.T / sums_by_month * 100).T  # Transpose, divide, multiply, then transpose back

# Plotting each genre
bottoms = np.zeros(num_months)
for i, genre in enumerate(genres):
    plt.bar(months, percentages[:, i], bottom=bottoms, label=genre)
    bottoms += percentages[:, i]

# Improving the plot
plt.ylabel('Percentage of Books Sold (%)')
plt.title('Monthly Genre Sales as a Percentage of Total Sales')
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Genres')
plt.tight_layout()

# Display the plot
plt.show()