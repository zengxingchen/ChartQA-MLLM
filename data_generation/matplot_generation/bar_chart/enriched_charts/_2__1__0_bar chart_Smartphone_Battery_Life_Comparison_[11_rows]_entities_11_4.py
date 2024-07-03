
import matplotlib.pyplot as plt

# City population data
cities = [
    "Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mexico City", 
    "Cairo", "Mumbai", "Beijing", "Dhaka", "Osaka", 
    "New York", "Karachi", "Buenos Aires", "Chongqing", 
    "Istanbul", "Kolkata", "Manila", "Lagos", "Rio de Janeiro", 
    "Tianjin", "Kinshasa", "Guangzhou", "Los Angeles", 
    "Moscow", "Shenzhen", "Lahore", "Bangalore", "Paris", 
    "Bogota", "Jakarta", "Chennai", "Lima", "Bangkok", 
    "Hyderabad"
]
populations = [
    37435191, 29399141, 26317104, 21846507, 21671908, 
    20484965, 20411274, 19612368, 19577939, 19222665, 
    18819000, 15400000, 15257663, 14838000, 14657434, 
    14500000, 13923452, 13500000, 13458000, 13245000, 
    13200000, 13080500, 12815475, 12506468, 12331000, 
    12188000, 11845000, 11020000, 10981000, 10770487, 
    10473000, 10422400, 10334401, 10020100
]

# New color scheme using specific color codes for each city
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', 
    '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#aec7e8', '#ffbb78', '#98df8a', '#ff9896'
]

# Create horizontal bar chart
plt.figure(figsize=(14, 10))  # Width and height of the chart
plt.barh(cities, populations, color=colors, height=0.7)  # Bar color and bar height

# Set the title and labels
plt.title('Population of Major Cities in the World', fontsize=16, pad=20)
plt.xlabel('Population', fontsize=14)
plt.ylabel('City', fontsize=14)

# Display the bar chart
plt.show()