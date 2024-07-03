
import matplotlib.pyplot as plt
import squarify

# Data points for the treemap
categories = ['Technology', 'Finance', 'Education', 'Healthcare', 'Retail', 'Manufacturing', 'Energy', 'Telecommunications', 'Transport', 'Construction', 'Agriculture', 'RealEstate', 'Media', 'Hospitality', 'Entertainment']
count = [1400, 1100, 900, 800, 700, 600, 500, 400, 350, 300, 250, 200, 180, 150, 120]

# TreeMap customization
color_palette = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000']
plt.figure(figsize=(18, 10))

# Creating the treemap
squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.8)

# Title and labels
plt.title('Distribution of Employment by Sector', fontsize=20, fontweight='bold')
plt.axis('off')

plt.show()