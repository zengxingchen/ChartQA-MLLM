
import matplotlib.pyplot as plt
import squarify

# Data
topics = [
    'Economics', 'Finance', 'Technology', 'Health', 'Education', 
    'Sports', 'Entertainment', 'Music', 'Travel', 'Food', 
    'Fashion', 'Politics', 'Science', 'Environment', 'History', 
    'Literature', 'Philosophy', 'Archaeology', 'Psychology'
]
popularity = [
    4500, 3200, 2800, 2600, 2400, 
    2200, 2100, 2000, 1800, 1700, 
    1600, 1500, 1400, 1300, 1200, 
    1100, 1000, 900, 800
]
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
    '#ffb3e6', '#c4e17f', '#ff6666', '#c2f0c2', '#ffccff', 
    '#d9d9d9', '#aaffc3', '#ffd700', '#87ceeb', '#ff6347', 
    '#dda0dd', '#fa8072', '#eee8aa', '#dda0dd'
]

# Plot
plt.figure(figsize=(18, 14))
squarify.plot(sizes=popularity, label=topics, color=colors, alpha=0.8)
plt.title('Most Discussed Topics by Popularity', fontsize=22, pad=30)
plt.axis('off')
plt.show()