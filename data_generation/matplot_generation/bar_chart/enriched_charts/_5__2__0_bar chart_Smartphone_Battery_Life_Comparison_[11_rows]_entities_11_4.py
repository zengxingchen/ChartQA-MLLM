
import matplotlib.pyplot as plt

# Monthly book sales data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
book_sales = [320, 350, 380, 330, 360, 400, 420, 410, 390, 370, 340, 380]

# Color scheme using specific color codes for each month
colors = [
    '#1E90FF', '#FF6347', '#32CD32', '#FFD700', '#8A2BE2',
    '#FF4500', '#ADFF2F', '#FF1493', '#00BFFF', '#FF8C00',
    '#7FFF00', '#DC143C'
]

# Create horizontal bar chart
plt.figure(figsize=(10, 8))  # Width and height of the chart
plt.barh(months, book_sales, color=colors, height=0.4)  # Bar color and band height

# Set the title and labels
plt.title('Monthly Book Sales Analysis', pad=20)
plt.xlabel('Book Sales')
plt.ylabel('Month')

# Set y-axis limits
plt.xlim(300, 450)  # Truncated y-axis

# Display the bar chart
plt.show()