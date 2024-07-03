
import matplotlib.pyplot as plt

# Data to plot
labels = 'Shoes', 'Clothing', 'Accessories', 'Cosmetics', 'Jewelry'
sizes = [35, 30, 20, 10, 5]
colors = ['#ff6347', '#4682b4', '#daa520', '#ff69b4', '#8a2be2']

# Change the size of the figure (width, height)
plt.figure(figsize=(8, 8))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Spending on Fashion & Beauty Products', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()