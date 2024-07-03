
import matplotlib.pyplot as plt

# Data from the chart table
data = [
    {'Person': 'Person 1', 'Cups of Coffee per Week': 14},
    {'Person': 'Person 2', 'Cups of Coffee per Week': 3},
    {'Person': 'Person 3', 'Cups of Coffee per Week': 21},
    {'Person': 'Person 4', 'Cups of Coffee per Week': 10},
    {'Person': 'Person 5', 'Cups of Coffee per Week': 12},
    {'Person': 'Person 6', 'Cups of Coffee per Week': 8},
    {'Person': 'Person 7', 'Cups of Coffee per Week': 0},
    {'Person': 'Person 8', 'Cups of Coffee per Week': 7},
    {'Person': 'Person 9', 'Cups of Coffee per Week': 5},
    {'Person': 'Person 10', 'Cups of Coffee per Week': 18},
    {'Person': 'Person 11', 'Cups of Coffee per Week': 4},
    {'Person': 'Person 12', 'Cups of Coffee per Week': 9},
    {'Person': 'Person 13', 'Cups of Coffee per Week': 1},
    {'Person': 'Person 14', 'Cups of Coffee per Week': 17},
    {'Person': 'Person 15', 'Cups of Coffee per Week': 2}
]

# Extracting the number of cups of coffee per week into a list
cups_of_coffee = [person['Cups of Coffee per Week'] for person in data]

# Histogram settings
number_of_bins = 5
color = '#A52A2A'  # A shade of brown to represent coffee
edge_color = '#FFFFFF'  # White edges for the bars

# Creating the histogram
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(cups_of_coffee, bins=number_of_bins, color=color, edgecolor=edge_color)

# Set the title and labels
plt.title('Cups of Coffee per Week', fontdict={'fontsize': 16})
plt.xlabel('Cups of Coffee', fontdict={'fontsize': 12})
plt.ylabel('Number of People', fontdict={'fontsize': 12})

# Customize ticks
plt.xticks(ticks=bins)
plt.yticks(range(1, max(n)+1))

# Annotate the histogram bars with the count of people
for i in range(len(patches)):
    plt.text(patches[i].xy[0], patches[i].get_height() + 0.1, str(int(patches[i].get_height())),
             fontsize=10, ha='left')

# Show a grid for better readability
plt.grid(axis='y', alpha=0.75)

# Display the histogram
plt.show()