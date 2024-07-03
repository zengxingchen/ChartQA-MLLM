
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Fashion Trends', 'Social Media Influence', 'Sustainable Fashion', 'Haute Couture', 'Streetwear', 'Vintage Fashion', 'Sportswear', 'Accessories', 'Footwear', 'Seasonal Collections']
A = [18, 25, 30, 20, 15, 22, 25, 30, 20, 25]
B = [22, 30, 25, 20, 30, 20, 25, 25, 30, 20]
C = [25, 20, 30, 30, 25, 25, 20, 25, 25, 30]
D = [35, 25, 15, 30, 30, 33, 30, 20, 25, 25]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Plotting
barWidth = 0.8
fig, ax = plt.subplots(figsize=(10, 14))

# Create stacked bar chart
bars1 = np.add(A, B).tolist()
bars2 = np.add(bars1, C).tolist()

ax.bar(categories, A, color=colors[0], edgecolor='white', width=barWidth, label='Category A')
ax.bar(categories, B, bottom=A, color=colors[1], edgecolor='white', width=barWidth, label='Category B')
ax.bar(categories, C, bottom=bars1, color=colors[2], edgecolor='white', width=barWidth, label='Category C')
ax.bar(categories, D, bottom=bars2, color=colors[3], edgecolor='white', width=barWidth, label='Category D')

# Add title and labels
ax.set_title('Fashion Industry Trends', fontsize=18, pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Categories')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Show plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()