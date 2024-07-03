
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [12.5, 14.8, 18.2, 25.6, 30.4, 33.1, 38.7, 42.3, 35.6, 28.4, 20.9, 15.3]
colors = ['#FF5733', '#FF8D33', '#FFC733', '#FFE333', '#D7FF33', '#9BFF33',
          '#33FF57', '#33FFCE', '#33C7FF', '#338BFF', '#335BFF', '#5733FF']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(months, revenue, color=colors, edgecolor='black', width=0.6)

# Customizing the plot
plt.ylabel('Monthly Revenue (in millions USD)')
plt.title('Monthly Revenue for a Tech Company', pad=20)
plt.ylim(0, max(revenue) + 5)
plt.tight_layout()

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()