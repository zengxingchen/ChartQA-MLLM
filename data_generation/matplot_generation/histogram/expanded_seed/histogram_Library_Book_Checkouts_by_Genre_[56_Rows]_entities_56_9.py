
import matplotlib.pyplot as plt

# The data provided
data = [
    {'Genre': 'Mystery', 'Checkouts': 120},
    {'Genre': 'Romance', 'Checkouts': 95},
    {'Genre': 'Science Fiction', 'Checkouts': 87},
    {'Genre': 'Biography', 'Checkouts': 76},
    {'Genre': "Children's Books", 'Checkouts': 130},
    {'Genre': 'History', 'Checkouts': 65},
    {'Genre': 'Fantasy', 'Checkouts': 112},
    {'Genre': 'Self-Help', 'Checkouts': 90},
    {'Genre': 'Cookbooks', 'Checkouts': 58},
    {'Genre': 'Travel', 'Checkouts': 49},
    {'Genre': 'Mystery', 'Checkouts': 125},
    {'Genre': 'Romance', 'Checkouts': 80},
    {'Genre': 'Science Fiction', 'Checkouts': 92},
    {'Genre': 'Biography', 'Checkouts': 81},
    {'Genre': "Children's Books", 'Checkouts': 120}
]

# Aggregating the checkouts by genre
from collections import defaultdict
checkout_totals = defaultdict(int)
for item in data:
    checkout_totals[item['Genre']] += item['Checkouts']

# Prepare data for plotting
genres = list(checkout_totals.keys())
totals = list(checkout_totals.values())

# Plot histogram-like bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(genres, totals, color='skyblue', edgecolor='black')

# Add details to the bars
for bar, total in zip(bars, totals):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 3, total, ha='center', va='bottom')

# Annotating the chart with titles and labels
plt.title('Total Book Checkouts by Genre')
plt.xlabel('Genre')
plt.ylabel('Number of Checkouts')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.tight_layout()
plt.show()