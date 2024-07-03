
import matplotlib.pyplot as plt

# Data
cities = [
    'Bangkok', 'Paris', 'Dubai', 'Istanbul', 'New York City', 
    'Singapore', 'Kuala Lumpur', 'Tokyo', 'Seoul', 'Hong Kong', 
    'Barcelona', 'Osaka', 'Rome', 'Pattaya', 'Bali', 
    'London', 'Bangkok', 'Paris', 'Dubai', 'Istanbul', 
    'New York City', 'Singapore', 'Kuala Lumpur', 'Tokyo', 
    'Seoul', 'Hong Kong', 'Barcelona', 'Osaka', 'Rome', 
    'Pattaya', 'Bali', 'London'
]
tourist_arrivals = [
    22000000, 19000000, 18000000, 17000000, 16000000, 
    15500000, 14000000, 13700000, 13000000, 12500000, 
    12000000, 11500000, 11000000, 10000000, 9500000, 
    9000000, 22000000, 19000000, 18000000, 17000000, 
    16000000, 15500000, 14000000, 13700000, 13000000, 
    12500000, 12000000, 11500000, 11000000, 10000000, 
    9500000, 9000000
]

# Plotting the bar chart
plt.figure(figsize=(14, 10))
plt.barh(cities, tourist_arrivals, height=0.6, color=[
    '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', 
    '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5', 
    '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f',
    '#e5c494', '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', 
    '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999',
    '#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854',
    '#ffd92f', '#e5c494'
])

# Customizing the plot
plt.xlabel('Annual Tourist Arrivals')
plt.title('Annual Tourist Arrivals in Major Cities', pad=20)
plt.xlim(8000000, 23000000)
plt.gca().invert_yaxis()

# Show the plot
plt.show()