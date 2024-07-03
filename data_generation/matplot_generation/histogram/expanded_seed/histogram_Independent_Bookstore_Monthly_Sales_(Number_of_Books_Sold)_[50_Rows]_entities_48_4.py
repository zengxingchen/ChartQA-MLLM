
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', 'Books Sold': 850},
    {'Month': 'February', 'Books Sold': 760},
    {'Month': 'March', 'Books Sold': 940},
    {'Month': 'April', 'Books Sold': 860},
    {'Month': 'May', 'Books Sold': 880},
    {'Month': 'June', 'Books Sold': 910},
    {'Month': 'July', 'Books Sold': 890},
    {'Month': 'August', 'Books Sold': 930},
    {'Month': 'September', 'Books Sold': 845},
    {'Month': 'October', 'Books Sold': 810},
    {'Month': 'November', 'Books Sold': 970},
    {'Month': 'December', 'Books Sold': 1000},
    {'Month': 'January', 'Books Sold': 870},
    {'Month': 'February', 'Books Sold': 730},
    {'Month': 'March', 'Books Sold': 950},
]

# Extracting 'Books Sold' into a list for plotting
books_sold = [entry['Books Sold'] for entry in data]

# Creating a histogram
plt.figure(figsize=(10, 6)) # Set the size of the figure
n, bins, patches = plt.hist(books_sold, bins=8, color='skyblue', edgecolor='black')

# Adding some aesthetics
plt.title('Distribution of Books Sold') # Title of the histogram
plt.xlabel('Books Sold') # X-axis label
plt.ylabel('Frequency') # Y-axis label

# Adding value labels on top of each bin
for i in range(len(patches)):
    plt.text(patches[i].xy[0] + patches[i]._width / 2, 
             patches[i]._height + 0.5, 
             str(int(patches[i]._height)),
             ha='center')

# Showing the plot
plt.show()