
import matplotlib.pyplot as plt
import seaborn as sns

# Provided data
data = [
    {'Genre': 'Fiction', 'Percentage of Total Checkouts': 30},
    {'Genre': 'Non-fiction', 'Percentage of Total Checkouts': 25},
    {'Genre': "Children's Literature", 'Percentage of Total Checkouts': 15},
    {'Genre': 'Biographies', 'Percentage of Total Checkouts': 7},
    {'Genre': 'Science Fiction & Fantasy', 'Percentage of Total Checkouts': 5},
    {'Genre': 'Mystery & Thriller', 'Percentage of Total Checkouts': 4},
    {'Genre': 'Graphic Novels', 'Percentage of Total Checkouts': 3},
    {'Genre': 'Romance', 'Percentage of Total Checkouts': 3},
    {'Genre': 'History', 'Percentage of Total Checkouts': 2},
    {'Genre': 'Self-help', 'Percentage of Total Checkouts': 3},
    {'Genre': 'Religion & Spirituality', 'Percentage of Total Checkouts': 1},
    {'Genre': 'Travel & Adventure', 'Percentage of Total Checkouts': 2}
]

# Extract the genres and their corresponding percentages
genres = [item['Genre'] for item in data]
percentages = [item['Percentage of Total Checkouts'] for item in data]

# Use Seaborn to set the color palette
colors = sns.color_palette('hsv', len(genres))

# Create the pie chart
plt.figure(figsize=(10, 8))  # Set the figure size
plt.pie(percentages, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Optional: Add a shadow to the pie chart for better visual appeal
plt.gca().set_aspect('equal')  # Set the aspect ratio to be equal, so the pie is circular
plt.title('Library Genre Distribution')  # Title of the pie chart

# Optional: Adjust legend
plt.legend(title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Show the pie chart
plt.show()