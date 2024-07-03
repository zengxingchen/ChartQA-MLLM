
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
page_views = [150, 180, 200, 230, 260, 300, 310, 350, 370, 390]
unique_visitors = [30, 45, 55, 60, 65, 80, 78, 90, 100, 110]

# Scatter plot
plt.figure(figsize=(12, 7))  # Width:12, Height:7
plt.scatter(days, page_views, color='#FF6347', label='Page Views')  # Tomato
plt.scatter(days, unique_visitors, color='#4682B4', label='Unique Visitors')  # Steel Blue

# Customize the plot
plt.title('Website Traffic Over 10 Days', pad=20)
plt.xlabel('Day')
plt.ylabel('Count')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()