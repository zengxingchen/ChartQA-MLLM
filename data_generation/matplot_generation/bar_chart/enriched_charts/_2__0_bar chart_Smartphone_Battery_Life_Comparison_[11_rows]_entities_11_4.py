
import matplotlib.pyplot as plt

# Monthly book sales data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
book_sales = [120, 150, 180, 130, 160, 200, 220, 210, 190, 170, 140, 180]

# Color scheme using specific color codes for each month
colors = [
    '#4B0082', '#8A2BE2', '#A52A2A', '#DEB887', '#5F9EA0',
    '#7FFF00', '#D2691E', '#FF7F50', '#6495ED', '#DC143C',
    '#00FFFF', '#00008B'
]

# Create vertical bar chart
plt.figure(figsize=(12, 6))  # Width and height of the chart
plt.bar(months, book_sales, color=colors, width=0.5)  # Bar color and band width

# Set the title and labels
plt.title('Monthly Book Sales', pad=20)
plt.ylabel('Book Sales')
plt.xlabel('Month')

# Display the bar chart
plt.show()