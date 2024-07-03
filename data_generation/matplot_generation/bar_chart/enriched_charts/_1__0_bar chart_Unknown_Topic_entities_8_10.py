
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
population = [
    37435191, 29399141, 26317104, 21846507, 21671908, 
    20484965, 20185064, 20035455, 19577916, 19222665, 
    18819000, 15400000, 14967000, 14838000, 14754000, 
    14681000, 13482000, 13478000, 13458000, 13215000, 
    13080500, 12506468, 12484000, 12188000, 11777000, 
    11027000, 10750000, 10750000, 10495000, 10360000, 
    10327000, 10203000, 9126366, 9026200, 8804500, 
    8837568, 8334951, 8171600, 8122900, 8099748
]

# Plotting the bar chart
plt.figure(figsize=(12, 10))
plt.bar(cities, population, width=0.7, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
    '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
    '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5'
])

# Customizing the plot
plt.ylabel('Population')
plt.title('Population of Major Cities Around the World', pad=20)
plt.ylim(7000000, 38000000)
plt.xticks(rotation=90)

# Show the plot
plt.show()