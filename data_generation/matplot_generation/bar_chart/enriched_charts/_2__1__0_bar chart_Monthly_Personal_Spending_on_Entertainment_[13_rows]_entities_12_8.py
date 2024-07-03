
import matplotlib.pyplot as plt

# Data points
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grapes', 'Pineapple', 'Mango', 'Blueberry', 
          'Lemon', 'Lime', 'Watermelon', 'Papaya', 'Peach', 'Cherry', 'Kiwi', 'Cantaloupe', 'Plum', 
          'Raspberry', 'Blackberry', 'Grapefruit', 'Tangerine', 'Pomegranate', 'Coconut', 'Guava', 
          'Lychee', 'Passion Fruit', 'Durian', 'Starfruit', 'Dragon Fruit', 'Jackfruit', 'Fig', 'Date', 
          'Apricot', 'Pear', 'Cranberry', 'Nectarine', 'Mulberry', 'Persimmon', 'Tamarind', 'Kumquat']
vitamin_c = [6, 9, 53, 59, 4, 47, 36, 9, 53, 29, 8, 60, 6, 10, 92, 36, 9, 26, 21, 31, 26, 10, 3, 228, 72, 30, 20, 
             34, 9, 13, 2, 0, 10, 5, 14, 5, 36, 7, 3, 44]

# Colors for each bar
colors = ['#FF6347', '#FF7F50', '#FFD700', '#ADFF2F', '#7FFF00', '#7CFC00', '#00FF00', '#32CD32', '#00FF7F', 
          '#00FA9A', '#40E0D0', '#48D1CC', '#00CED1', '#20B2AA', '#5F9EA0', '#4682B4', '#1E90FF', '#6495ED', 
          '#7B68EE', '#6A5ACD', '#8A2BE2', '#9400D3', '#9932CC', '#BA55D3', '#FF00FF', '#FF1493', '#C71585', 
          '#DB7093', '#FFA07A', '#FF4500', '#DC143C', '#B22222', '#8B0000', '#800000', '#A52A2A', '#A0522D', 
          '#D2691E', '#CD853F', '#F4A460', '#DEB887']

# Create a horizontal bar chart
plt.figure(figsize=(12, 16))
plt.barh(fruits, vitamin_c, color=colors, height=0.6)

# Modify the ticks, labels, and title
plt.xlabel('Vitamin C Content (mg)')
plt.title('Vitamin C Content in Various Fruits')
plt.xlim(0, 250)  # Assuming the vitamin C content ranges between 0 and 250 mg

# Display the plot
plt.tight_layout()
plt.show()