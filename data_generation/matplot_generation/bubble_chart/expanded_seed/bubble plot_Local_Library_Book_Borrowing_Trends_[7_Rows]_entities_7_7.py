
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Provided table data
data = [
    {'Month': 'January', "Children's Books (units)": 150, 'Adult Fiction (units)': 120, 'Adult Non-Fiction (units)': 90, 'Average Borrowing Duration (days)': 14, 'Library Visitors (per day)': 50},
    {'Month': 'February', "Children's Books (units)": 120, 'Adult Fiction (units)': 110, 'Adult Non-Fiction (units)': 95, 'Average Borrowing Duration (days)': 16, 'Library Visitors (per day)': 45},
    {'Month': 'March', "Children's Books (units)": 180, 'Adult Fiction (units)': 140, 'Adult Non-Fiction (units)': 100, 'Average Borrowing Duration (days)': 12, 'Library Visitors (per day)': 55},
    {'Month': 'April', "Children's Books (units)": 160, 'Adult Fiction (units)': 130, 'Adult Non-Fiction (units)': 110, 'Average Borrowing Duration (days)': 15, 'Library Visitors (per day)': 60},
    {'Month': 'May', "Children's Books (units)": 175, 'Adult Fiction (units)': 125, 'Adult Non-Fiction (units)': 95, 'Average Borrowing Duration (days)': 10, 'Library Visitors (per day)': 80},
    {'Month': 'June', "Children's Books (units)": 200, 'Adult Fiction (units)': 150, 'Adult Non-Fiction (units)': 90, 'Average Borrowing Duration (days)': 8, 'Library Visitors (per day)': 70},
    {'Month': 'July', "Children's Books (units)": 190, 'Adult Fiction (units)': 145, 'Adult Non-Fiction (units)': 85, 'Average Borrowing Duration (days)': 7, 'Library Visitors (per day)': 75}
]

# Prepare lists for each variable
months = [d['Month'] for d in data]
children_books = [d["Children's Books (units)"] for d in data]
adult_fiction = [d['Adult Fiction (units)'] for d in data]
adult_non_fiction = [d['Adult Non-Fiction (units)'] for d in data]
borrowing_duration = [d['Average Borrowing Duration (days)'] for d in data]
visitors = [d['Library Visitors (per day)'] for d in data]

# Calculate bubble sizes. The formula for size can be adjusted as needed
# In this case, assume size is proportional to total units borrowed, with a scaling factor for better visibility
total_units_borrowed = np.add(np.add(children_books, adult_fiction), adult_non_fiction)
bubble_sizes = (total_units_borrowed / np.max(total_units_borrowed)) * 1000  # Scale for better visibility

# Create a color map based on 'Average Borrowing Duration (days)'
norm = mcolors.Normalize(vmin=min(borrowing_duration), vmax=max(borrowing_duration))
colormap = plt.cm.viridis  # We can also choose another colormap like plt.cm.plasma, plt.cm.inferno, etc.

# Create the bubble chart
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
for i in range(len(months)):
    plt.scatter(months[i], visitors[i], s=bubble_sizes[i], c=[borrowing_duration[i]],
                cmap=colormap, alpha=0.6, edgecolors='w', linewidth=0.5, norm=norm)

# Create a colorbar
plt.colorbar(mappable=plt.cm.ScalarMappable(norm=norm, cmap=colormap),
             orientation='vertical', label='Average Borrowing Duration (days)')

# Set the chart title and axes labels
plt.title('Library Data Bubble Chart')
plt.xlabel('Months')
plt.ylabel('Library Visitors (per day)')

# Show the bubble chart
plt.show()