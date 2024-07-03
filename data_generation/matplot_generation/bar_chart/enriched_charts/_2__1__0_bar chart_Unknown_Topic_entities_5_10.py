
import matplotlib.pyplot as plt

# Data
genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Romance', 'Science Fiction', 'Thriller', 'Animation', 'Documentary', 'Musical']
revenue = [35.7, 12.4, 24.9, 28.2, 15.1, 7.6, 10.3, 22.5, 19.8, 18.9, 3.2, 4.1]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.barh(genres, revenue, height=0.6, color=['#1E90FF', '#32CD32', '#FFD700', '#FF4500', '#8A2BE2', '#FF69B4', '#A52A2A', '#5F9EA0', '#D2691E', '#DC143C', '#008B8B', '#B8860B'])

# Customizing the plot
ax.set_title('Revenue by Movie Genre (in billion USD)', fontsize=20, pad=20)
ax.set_xlabel('Revenue (in billion USD)', fontsize=16)
ax.set_ylabel('Movie Genre', fontsize=16)

# Set bar labels to show the revenue values
for bar in bars:
    width = bar.get_width()
    label_x_pos = width if width > 0 else width + 1  # Adjust label position
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} bn', ha='left', va='center')

# Show the plot
plt.tight_layout()
plt.show()