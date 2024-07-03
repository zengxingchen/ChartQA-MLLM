
import matplotlib.pyplot as plt

# Data
topics = ['Oil Painting', 'Digital Art', 'Sculpture', 'Photography', 'Graphic Design', 'Animation', 'Illustration', 
          '3D Modeling', 'Street Art', 'Calligraphy', 'Ceramics', 'Fashion Design']
year = [2022] * len(topics)
values = [9500, 12000, 8000, 11000, 10500, 14000, 13000, 9000, 6000, 7500, 8500, 12500]
count = [50, 70, 40, 65, 60, 85, 80, 55, 35, 45, 50, 75]

# Size is proportional to count, and color represents values
size = [x * 2 for x in count]
colors = ['#3498DB', '#E74C3C', '#2ECC71', '#F1C40F', '#9B59B6', '#1ABC9C', '#F39C12', '#8E44AD', '#34495E', '#C0392B', '#7F8C8D', '#2980B9']

# Create a figure with specific width and height
fig, ax = plt.subplots(figsize=(14, 8))

# Bubble chart
sc = ax.scatter(topics, year, s=size, c=colors, alpha=0.6, edgecolors='w')

# Customize chart
ax.set_title('Art & Design - Popularity and Number of Artists (2022)')
ax.set_xlabel('Art & Design Topics')
ax.set_ylabel('Year')
ax.set_yticks([2022])  # Only one year on the y-axis
ax.grid(True)

# Adding a color bar to indicate values
value_tick_vals = range(6000, 14500, 1000)
value_tick_labels = ['$' + str(val) for val in value_tick_vals]
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=plt.Normalize(vmin=min(values), vmax=max(values)))
sm._A = []  # ScalarMappable expects an array of data values for colormap scaling; we provide a dummy
cbar = plt.colorbar(sm, ticks=value_tick_vals)
cbar.ax.set_yticklabels(value_tick_labels)
cbar.set_label('Values')

# Show plot
plt.show()