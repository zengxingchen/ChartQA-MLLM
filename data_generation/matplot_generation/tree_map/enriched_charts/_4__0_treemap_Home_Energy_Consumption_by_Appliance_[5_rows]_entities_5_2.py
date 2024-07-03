
import matplotlib.pyplot as plt
import squarify

# Dataset
regions = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Oceania', 'Antarctica']
populations = [4641054775, 1340598147, 747636026, 592072212, 430759766, 43111704, 1000]

# Color Scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

plt.figure(figsize=(14, 10))

# Creating the treemap
squarify.plot(sizes=populations, label=regions, color=colors, alpha=0.8)

# Adding a title
plt.title('World Population by Region', fontsize=18, weight='bold')

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()