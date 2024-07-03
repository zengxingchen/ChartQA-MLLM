
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
product_a = [120, 100, 140, 130, 200, 180, 160, 140, 190, 210, 230, 240]
product_b = [150, 180, 160, 170, 190, 220, 210, 230, 240, 260, 220, 210]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bar chart (horizontal)
plt.barh(months, product_a, color='#FFD700', edgecolor='white', height=0.85, label='Product A')
plt.barh(months, product_b, left=product_a, color='#6495ED', edgecolor='white', height=0.85, label='Product B')

# Labels, title and legend
plt.xlabel('Sales')
plt.title('Monthly Sales of Product A and B')
plt.legend()

# Show the plot
plt.show()