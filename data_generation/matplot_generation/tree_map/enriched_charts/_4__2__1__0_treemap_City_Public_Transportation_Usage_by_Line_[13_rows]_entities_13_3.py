
import matplotlib.pyplot as plt
import squarify

# Data
labels = ['France', 'Spain', 'United States', 'China', 'Italy', 'Mexico', 'United Kingdom', 'Turkey', 'Germany', 'Thailand', 'Japan', 'Malaysia', 'Hong Kong', 'Russia', 'Canada', 'South Korea']
sizes = [83, 81, 76, 60, 58, 39, 37, 35, 33, 32, 31, 26, 26, 24, 22, 22]
colors = ['#3498db', '#e74c3c', '#f1c40f', '#2ecc71', '#9b59b6', '#e67e22', '#1abc9c', '#34495e', '#95a5a6', '#d35400', '#16a085', '#c0392b', '#8e44ad', '#27ae60', '#2980b9','#7f8c8d']

# Plot
plt.figure(figsize=(18, 15))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
plt.title('Popular Travel Destinations by Visitors (in millions)', fontsize=22, y=1.05)
plt.axis('off')
plt.show()