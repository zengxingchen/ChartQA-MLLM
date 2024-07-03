
import matplotlib.pyplot as plt

# Data
types = [
    'Domestic Travel', 'International Travel', 'Adventure Sports', 'Cultural Tours', 
    'Wildlife Safaris', 'Cruises', 'Mountain Climbing', 'Beach Holidays', 
    'Road Trips', 'Luxury Escapes', 'Backpacking', 'City Breaks', 
    'Eco-Tourism', 'Spiritual Journeys'
]
inventory_count = [55, 40, 35, 25, 15, 30, 20, 45, 10, 25, 18, 22, 12, 8]
colors = [
    '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', 
    '#FF6347', '#FF4500', '#BA55D3', '#DA70D6', '#7B68EE', 
    '#32CD32', '#8A2BE2', '#FF8C00', '#FFD700'
]

# Create a pie chart
plt.figure(figsize=(14, 12))  # Adjusting the size of the pie chart
plt.pie(inventory_count, labels=types, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Travel & Adventure Distribution', pad=30)

plt.show()