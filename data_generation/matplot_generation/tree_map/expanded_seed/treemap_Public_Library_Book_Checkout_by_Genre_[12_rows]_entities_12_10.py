
import matplotlib.pyplot as plt
import squarify

# Given chart table data
data = [
    {'Genre': 'Mystery', 'Checkouts': 120, 'Month': 'January'},
    {'Genre': 'Science Fiction', 'Checkouts': 110, 'Month': 'January'},
    {'Genre': 'Romance', 'Checkouts': 130, 'Month': 'January'},
    {'Genre': 'Biographies', 'Checkouts': 70, 'Month': 'January'},
    {'Genre': 'Young Adult', 'Checkouts': 160, 'Month': 'January'},
    {"Genre": "Children's Books", 'Checkouts': 200, 'Month': 'January'},
    {'Genre': 'Mystery', 'Checkouts': 90, 'Month': 'February'},
    {'Genre': 'Science Fiction', 'Checkouts': 95, 'Month': 'February'},
    {'Genre': 'Romance', 'Checkouts': 125, 'Month': 'February'},
    {'Genre': 'Biographies', 'Checkouts': 65, 'Month': 'February'},
    {'Genre': 'Young Adult', 'Checkouts': 150, 'Month': 'February'},
    {"Genre": "Children's Books", 'Checkouts': 190, 'Month': 'February'}
]

# Aggregate the checkouts by genre over the months
aggregated_checkouts = {}
for item in data:
    if item['Genre'] in aggregated_checkouts:
        aggregated_checkouts[item['Genre']] += item['Checkouts']
    else:
        aggregated_checkouts[item['Genre']] = item['Checkouts']

# Prepare data for the treemap
labels = [f"{genre}\n{checkouts}" for genre, checkouts in aggregated_checkouts.items()]
sizes = list(aggregated_checkouts.values())
colors = plt.cm.Spectral([float(x) / max(sizes) for x in sizes])

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Adding a title and eliminating the axis
plt.title('Book Genre Checkout Treemap')
plt.axis('off')

# Display the plot
plt.show()