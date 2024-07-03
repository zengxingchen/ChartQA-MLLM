
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
temperatures = [
    16.5, 25.1, 17.6, 19.3, 16.0, 
    22.2, 27.2, 12.6, 25.9, 16.8, 
    12.5, 26.8, 17.9, 18.1, 14.1, 
    26.9, 27.1, 27.1, 23.2, 12.5, 
    22.4, 5.8, 22.5, 24.3, 24.2, 
    11.3, 14.5, 27.6, 28.0, 18.1, 
    28.1, 26.5, 11.0, 17.5, 11.1, 
    16.2, 15.7, 17.1, 27.8, 23.7
]

# Plotting the bar chart
plt.figure(figsize=(14, 8))
plt.barh(cities, temperatures, height=0.6, color=[
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
plt.xlabel('Average Annual Temperature (°C)')
plt.title('Average Annual Temperature of Major Cities Around the World', pad=20)
plt.xlim(0, 30)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()