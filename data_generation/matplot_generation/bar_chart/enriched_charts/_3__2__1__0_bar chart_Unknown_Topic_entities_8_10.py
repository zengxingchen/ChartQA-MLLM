
import matplotlib.pyplot as plt

# Data
destinations = [
    'France', 'Spain', 'United States', 'China', 'Italy', 
    'Turkey', 'Mexico', 'Germany', 'Thailand', 'United Kingdom', 
    'Japan', 'Austria', 'Greece', 'Russia', 'Canada', 
    'Saudi Arabia', 'Netherlands', 'South Korea', 'Malaysia', 
    'Portugal', 'Poland', 'Indonesia', 'South Africa', 
    'Egypt', 'Australia', 'Switzerland', 'Argentina', 
    'Sweden', 'Denmark', 'Brazil', 'Ireland', 'Norway', 
    'Singapore', 'New Zealand', 'Israel'
]
visitors = [
    89000000, 83000000, 79000000, 65000000, 62000000, 
    51000000, 45000000, 38000000, 35000000, 34000000, 
    32000000, 30000000, 28000000, 25000000, 22000000, 
    20000000, 19000000, 18000000, 17000000, 16000000, 
    15000000, 14000000, 13000000, 12000000, 11000000, 
    10000000, 9000000, 8000000, 7000000, 6000000, 
    5000000, 4000000, 3000000, 2000000, 1000000
]

# Plotting the bar chart
plt.figure(figsize=(10, 16))
plt.barh(destinations, visitors, height=0.5, color=[
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
    '#ffb3e6', '#c4e17f', '#76d7c4', '#ff6f61', '#6b5b95', 
    '#88b04b', '#d65076', '#45b8ac', '#e84a5f', '#ff7b25', 
    '#fdcc52', '#87bdd8', '#6a0572', '#d9bf77', '#d11141', 
    '#00b159', '#00aedb', '#f37735', '#ffc425', '#8ec06c', 
    '#d7c7ad', '#bc243c', '#c7a252', '#ff9f80', '#ffcd3c', 
    '#56d9fe', '#a56cc1', '#00cc99', '#ff6b6b', '#ff847c'
])

# Customizing the plot
plt.xlabel('Visitors in Millions')
plt.title('Top Tourist Destinations by Annual Visitors', pad=20)
plt.xlim(0, 100000000)
plt.xticks(rotation=45)

# Show the plot
plt.show()