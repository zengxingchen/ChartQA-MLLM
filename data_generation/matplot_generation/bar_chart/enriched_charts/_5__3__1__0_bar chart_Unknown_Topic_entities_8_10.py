
import matplotlib.pyplot as plt

# Data
cities = [
    'Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City', 
    'Cairo', 'Mumbai', 'Beijing', 'Dhaka', 'Osaka', 
    'New York City', 'Karachi', 'Buenos Aires', 'Chongqing', 
    'Istanbul', 'Kolkata', 'Manila', 'Lagos', 'Rio de Janeiro', 
    'Tianjin', 'Guangzhou', 'Moscow', 'Shenzhen', 'Lahore', 
    'Bangalore', 'Paris', 'Bogota', 'Jakarta', 'Chennai', 
    'Lima', 'Bangkok', 'Hyderabad', 'London', 'Tehran', 
    'Chicago', 'Chengdu', 'Nanjing', 'Wuhan', 'Ho Chi Minh City', 
    'Luanda'
]
activities = [
    20.5, 25.1, 18.6, 22.3, 16.0, 
    23.2, 27.2, 19.6, 24.9, 20.8, 
    22.5, 26.8, 17.9, 19.1, 21.1, 
    26.9, 27.1, 27.1, 23.2, 19.5, 
    24.4, 15.8, 24.5, 26.3, 24.2, 
    15.3, 19.5, 27.6, 28.0, 21.1, 
    28.1, 26.5, 18.0, 20.5, 18.1, 
    19.2, 21.7, 17.1, 27.8, 23.7
]

# Plotting the bar chart
plt.figure(figsize=(10, 12))
plt.barh(cities, activities, height=0.5, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFB833', 
    '#8D33FF', '#33FFBD', '#FF334C', '#FF8633', '#33A1FF',
    '#FFC733', '#B833FF', '#33FFD8', '#FF3333', '#A1FF33',
    '#FF33F7', '#57FF33', '#3333FF', '#FF33AF', '#FF5733',
    '#33FF57', '#3357FF', '#FF33A1', '#FFB833', '#8D33FF',
    '#33FFBD', '#FF334C', '#FF8633', '#33A1FF', '#FFC733',
    '#B833FF', '#33FFD8', '#FF3333', '#A1FF33', '#FF33F7',
    '#57FF33', '#3333FF', '#FF33AF', '#FF5733', '#33FF57'
])

# Customizing the plot
plt.xlabel('Average Monthly Hours of Physical Activities')
plt.title('Average Monthly Hours of Physical Activities in Various Cities', pad=20)
plt.xlim(10, 30)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.ylim(0, len(cities)-1)

# Show the plot
plt.show()