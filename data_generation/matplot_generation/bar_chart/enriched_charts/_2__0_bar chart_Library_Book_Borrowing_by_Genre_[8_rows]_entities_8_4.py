
import matplotlib.pyplot as plt

# Data
cities = [
    "Paris", "Bangkok", "London", "Dubai", "Istanbul", "New York", 
    "Singapore", "Kuala Lumpur", "Tokyo", "Antalya", "Seoul", "Osaka", 
    "Barcelona", "Hong Kong", "Milan"
]
visitors = [
    19.1, 22.7, 19.6, 16.3, 14.7, 13.1, 12.9, 13.8, 12.5, 13.6, 11.9, 10.1, 
    12.3, 9.0, 9.1
]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(12, 8))

# Vertical bar chart
bars = ax.bar(cities, visitors, color=[
    '#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#e67e22',
    '#1abc9c', '#34495e', '#d35400', '#7f8c8d', '#27ae60', '#8e44ad',
    '#c0392b', '#2980b9', '#16a085'], width=0.6)

# Set the title and labels
ax.set_title('Top 15 Most Visited Cities in 2023 (Millions of Visitors)', fontsize=15)
ax.set_ylabel('Visitors (millions)', fontsize=12)
ax.set_xlabel('City', fontsize=12)

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Show Values on Bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 0.3
    ax.text(bar.get_x() + bar.get_width() / 2, label_y_pos, f'{height:.1f}', ha='center')

# Set the layout to be tight
plt.tight_layout()

# Show the plot
plt.show()