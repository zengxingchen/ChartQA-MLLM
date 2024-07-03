
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
views = [150, 200, 250, 180, 220, 300, 280]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A1FF33', '#33A1FF', '#FF5733']

# Create a horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(days, views, color=colors, edgecolor='black', height=0.6)

# Customizing the plot
plt.xlabel('Number of Views')
plt.title('Daily Views on a Blog')
plt.xlim(0, max(views) + 50)
plt.tight_layout()

# Show grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()