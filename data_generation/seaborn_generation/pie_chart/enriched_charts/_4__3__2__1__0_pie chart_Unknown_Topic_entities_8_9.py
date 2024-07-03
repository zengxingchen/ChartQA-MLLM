
import matplotlib.pyplot as plt

# Data points
categories = ['Fashion Trends', 'Sustainable Materials', 'Designer Brands', 'Fast Fashion', 'Vintage & Thrift', 'Seasonal Collections', 'Accessories']
percentage = [20.0, 15.0, 25.0, 10.0, 8.0, 12.0, 10.0]
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#34495e', '#e67e22']

# Create a pie chart
plt.figure(figsize=(14, 10))  # Modify the width and height of the chart
plt.pie(percentage, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Distribution of Fashion & Beauty Categories in 2023', pad=20)

# Display the chart
plt.show()