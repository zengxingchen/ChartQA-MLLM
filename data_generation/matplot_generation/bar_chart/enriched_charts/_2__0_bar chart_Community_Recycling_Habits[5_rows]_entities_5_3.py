
import matplotlib.pyplot as plt

# Data
fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Iced Berry', 'Jackfruit', 'Kiwi', 'Lemon', 'Mango', 'Nectarine', 'Orange', 'Papaya', 'Quince', 'Raspberry', 'Strawberry', 'Tangerine']
sales = [150, 200, 75, 50, 30, 60, 220, 90, 45, 100, 80, 110, 170, 55, 130, 95, 20, 85, 140, 65]
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#D2691E', '#4B0082', '#8B4513', '#FF4500', '#228B22', '#DDA0DD', '#9ACD32', '#FF1493', '#B0C4DE', '#FFA500', '#FF6347', '#8A2BE2', '#FFD700', '#4B0082', '#D2691E', '#FF4500', '#228B22']

# Figure size
plt.figure(figsize=(12, 10))

# Vertical bar chart
plt.bar(fruits, sales, color=colors, width=0.4)

# Labeling
plt.ylabel('Sales')
plt.title('Fruit Sales in the Market')

# Show and save plot
plt.tight_layout()
plt.show()