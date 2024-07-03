
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [120.5, 140.3, 155.0, 180.4, 220.1, 250.3, 270.8, 260.9, 230.5, 190.6, 160.4, 130.7]
colors = ['#FF5733', '#FF8D33', '#FFC733', '#FFE333', '#D7FF33', '#9BFF33',
          '#33FF57', '#33FFCE', '#33C7FF', '#338BFF', '#335BFF', '#5733FF']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(months, sales, color=colors, edgecolor='black', width=0.7)

# Customizing the plot
plt.ylabel('Apparel Sales (in million USD)')
plt.title('Monthly Apparel Sales in New York')
plt.ylim(100, max(sales) + 20)
plt.tight_layout()

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()