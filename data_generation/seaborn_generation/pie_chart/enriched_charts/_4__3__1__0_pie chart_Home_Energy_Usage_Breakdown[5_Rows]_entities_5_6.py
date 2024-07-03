
import matplotlib.pyplot as plt

# Data
food_types = ['Vegetables', 'Fruits', 'Grains', 'Dairy', 'Meat', 
              'Seafood', 'Nuts', 'Sweets', 'Beverages', 'Oils', 
              'Spices', 'Eggs', 'Legumes', 'Processed Foods', 'Condiments']
consumption = [150.0, 110.0, 130.0, 70.0, 90.0, 
               40.0, 35.0, 55.0, 65.0, 20.0, 
               30.0, 25.0, 45.0, 50.0, 15.0]

# Colors
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#00FA9A', '#FF4500',
          '#4682B4', '#D2691E', '#FF1493', '#32CD32', '#D3D3D3',
          '#B22222', '#FFA07A', '#8FBC8F', '#FFDEAD', '#2E8B57']

# Pie chart
fig, ax = plt.subplots(figsize=(14, 10))  # Width, Height of the chart
ax.pie(consumption, labels=food_types, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Distribution of Food Consumption by Type (Millions)', pad=20)
plt.show()