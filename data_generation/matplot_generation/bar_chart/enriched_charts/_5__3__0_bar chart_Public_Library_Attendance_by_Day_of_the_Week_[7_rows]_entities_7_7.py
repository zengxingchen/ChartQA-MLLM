
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [13.2, 15.1, 18.6, 26.3, 31.0, 33.9, 39.3, 43.0, 36.1, 29.0, 21.2, 16.0]
colors = ['#FF4500', '#FF6347', '#FFA500', '#FFD700', '#ADFF2F', '#32CD32',
          '#00FF7F', '#40E0D0', '#1E90FF', '#0000FF', '#8A2BE2', '#9400D3']

# Create a horizontal bar chart
plt.figure(figsize=(14, 8))
bars = plt.barh(months, revenue, color=colors, edgecolor='black', height=0.5)

# Customizing the plot
plt.xlabel('Monthly Revenue (in millions USD)')
plt.title('Monthly Revenue for a Tech Company', pad=20)
plt.xlim(10, max(revenue) + 5)
plt.tight_layout()

# Show grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()