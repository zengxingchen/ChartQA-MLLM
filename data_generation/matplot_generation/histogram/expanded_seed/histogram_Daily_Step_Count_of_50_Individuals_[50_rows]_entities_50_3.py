
import matplotlib.pyplot as plt

# Provided data
data = [
    {'PersonID': 1, 'Step Count': 3234},
    {'PersonID': 2, 'Step Count': 7890},
    {'PersonID': 3, 'Step Count': 5643},
    {'PersonID': 4, 'Step Count': 9055},
    {'PersonID': 5, 'Step Count': 7098},
    {'PersonID': 6, 'Step Count': 6574},
    {'PersonID': 7, 'Step Count': 4882},
    {'PersonID': 8, 'Step Count': 8310},
    {'PersonID': 9, 'Step Count': 10234},
    {'PersonID': 10, 'Step Count': 3421},
    {'PersonID': 11, 'Step Count': 8060},
    {'PersonID': 12, 'Step Count': 6957},
    {'PersonID': 13, 'Step Count': 5850},
    {'PersonID': 14, 'Step Count': 8095},
    {'PersonID': 15, 'Step Count': 9230}
]

# Extract 'Step Count' values from data
step_counts = [person['Step Count'] for person in data]

# Create a histogram
plt.figure(figsize=(10, 6)) # Set the figure size
n, bins, patches = plt.hist(step_counts, bins=8, color='skyblue', edgecolor='black')

# We will color each bar of histogram based on its height
max_height = max(n)
for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(n[i] / max_height))

plt.title('Step Count Histogram') # Title for the histogram
plt.xlabel('Step Count')          # X-axis label
plt.ylabel('Number of Persons')   # Y-axis label

# Adding a color bar to represent the height of bars
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(0, max_height))
plt.colorbar(sm, label='Height (Number of Persons)')

# Show grid
plt.grid(axis='y', alpha=0.75)

# Add annotations for bar heights
for i in range(len(bins)-1):
    plt.text(bins[i]+0.5*(bins[i+1]-bins[i]), n[i] + 0.1, str(int(n[i])), color='darkblue', fontweight='bold', ha='center')

# Display the histogram
plt.show()