
import matplotlib.pyplot as plt
import squarify

# Data
data = [
    {'Section': 'Fiction', 'Genre': 'Novels', 'Monthly Visitors': 450, 'Books Checked Out': 700},
    {'Section': 'Fiction', 'Genre': 'Short Stories', 'Monthly Visitors': 150, 'Books Checked Out': 300},
    {'Section': 'Non-Fiction', 'Genre': 'Biographies', 'Monthly Visitors': 300, 'Books Checked Out': 400},
    {'Section': 'Non-Fiction', 'Genre': 'History', 'Monthly Visitors': 200, 'Books Checked Out': 350},
    {"Section": "Children's Books", 'Genre': 'Fairy Tales', 'Monthly Visitors': 500, 'Books Checked Out': 850},
    {"Section": "Children's Books", 'Genre': 'Educational', 'Monthly Visitors': 320, 'Books Checked Out': 430},
    {'Section': 'Young Adult', 'Genre': 'Science Fiction', 'Monthly Visitors': 280, 'Books Checked Out': 600},
    {'Section': 'Young Adult', 'Genre': 'Fantasy', 'Monthly Visitors': 320, 'Books Checked Out': 575},
    {'Section': 'Reference', 'Genre': 'Encyclopedias', 'Monthly Visitors': 60, 'Books Checked Out': 50},
    {'Section': 'Reference', 'Genre': 'Dictionaries', 'Monthly Visitors': 80, 'Books Checked Out': 65},
    {'Section': 'Study Resources', 'Genre': 'Academic Journals', 'Monthly Visitors': 250, 'Books Checked Out': 310},
    {'Section': 'Study Resources', 'Genre': 'Textbooks', 'Monthly Visitors': 175, 'Books Checked Out': 215}
]

# Prepare data for the treemap
sizes = [entry['Books Checked Out'] for entry in data]
labels = [f"{entry['Genre']} ({entry['Books Checked Out']} books)" for entry in data]
colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

# Plot treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7)

# Customize the plot
plt.title('Book Checkout Treemap by Genre and Section')
plt.axis('off')

# Add color bar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
ax = plt.gca()
axins = inset_axes(ax, width="5%", height="50%", loc='lower left',
                   bbox_to_anchor=(1.05, 0., 1, 1), bbox_transform=ax.transAxes, borderpad=0)
cmap = plt.cm.Spectral
plt.colorbar(plt.cm.ScalarMappable(cmap=cmap), cax=axins, orientation='vertical')

# Show plot
plt.tight_layout()
plt.show()