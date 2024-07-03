
import matplotlib.pyplot as plt

# Data from the provided table
data = [
    {'Genre': 'Fiction', 'Checkouts': 14523},
    {'Genre': 'Non-Fiction', 'Checkouts': 13412},
    {'Genre': 'Young Adult', 'Checkouts': 9723},
    {'Genre': "Children's Books", 'Checkouts': 15432},
    {'Genre': 'Biographies', 'Checkouts': 4723},
    {'Genre': 'Science Fiction', 'Checkouts': 6235},
    {'Genre': 'Mystery', 'Checkouts': 7312},
    {'Genre': 'Romance', 'Checkouts': 5650},
    {'Genre': 'Cookbooks', 'Checkouts': 2999},
    {'Genre': 'Graphic Novels', 'Checkouts': 3562},
    {'Genre': 'Self-Help', 'Checkouts': 4188},
    {'Genre': 'History', 'Checkouts': 3876}
]

# Prepare data for pie chart
genres = [item['Genre'] for item in data]
checkouts = [item['Checkouts'] for item in data]

# Define colors for each slice
colors = plt.cm.Paired(range(len(data)))

# Define the explode parameter to separate slices a little bit
explode = [0.05] * len(data)

# Generate the pie chart
plt.figure(figsize=(10,8))
plt.pie(checkouts, explode=explode, labels=genres, colors=colors, autopct='%.1f%%', startangle=140, shadow=True)

# Set the aspect ratio to be equal so that the pie is drawn as a circle
plt.axis('equal')

# Title for the chart
plt.title('Library Genre Checkouts Distribution', pad=20)

# Display the chart
plt.show()