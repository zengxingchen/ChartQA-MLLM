
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
books_sold = [120, 130, 150, 170, 200, 230, 220, 210, 180, 160, 140, 110]

# Colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78']

# Plotting the bar chart horizontally
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.barh(months, books_sold, color=colors, edgecolor='black', height=0.7)  # Change width for bars and apply color scheme

# Chart title and labels
plt.title('Monthly Book Sales in a Store', fontsize=18, pad=20)
plt.xlabel('Books Sold', fontsize=14)

# Setting the ylim to start from 100 for better clarity
plt.xlim(100, max(books_sold) + 50)

# Display the chart
plt.tight_layout()
plt.show()