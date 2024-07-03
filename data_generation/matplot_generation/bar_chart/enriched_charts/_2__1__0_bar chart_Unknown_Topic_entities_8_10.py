
import matplotlib.pyplot as plt

# Data
countries = [
    'United States', 'China', 'Japan', 'Germany', 'United Kingdom', 
    'India', 'France', 'Italy', 'Canada', 'South Korea', 
    'Russia', 'Australia', 'Spain', 'Mexico', 'Indonesia', 
    'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland', 
    'Taiwan', 'Poland', 'Sweden', 'Belgium', 'Thailand', 
    'Austria', 'Nigeria', 'Israel', 'Argentina', 'Norway', 
    'South Africa', 'Ireland', 'Denmark', 'Singapore', 
    'Malaysia', 'Hong Kong', 'Philippines', 'Bangladesh', 
    'Egypt', 'Pakistan', 'Chile'
]
gdp = [
    22675271, 16642318, 5378136, 4291397, 3195655, 
    3176294, 3010101, 2106997, 2050034, 1835649, 
    1775554, 1550567, 1452145, 1257591, 1211200, 
    1031633, 833541, 815271, 802539, 788499, 
    674002, 586095, 577138, 543550, 503759, 
    476197, 468339, 453008, 452559, 419015, 
    403775, 397100, 396992, 372777, 368096, 
    361489, 353515, 331951, 327731, 318255
]

# Plotting the bar chart
plt.figure(figsize=(14, 8))
plt.barh(countries, gdp, height=0.6, color=[
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
    '#ffb3e6', '#c4e17f', '#76d7c4', '#ff6f61', '#6b5b95', 
    '#88b04b', '#d65076', '#45b8ac', '#e84a5f', '#ff7b25', 
    '#fdcc52', '#87bdd8', '#6a0572', '#d9bf77', '#d11141', 
    '#00b159', '#00aedb', '#f37735', '#ffc425', '#8ec06c', 
    '#d7c7ad', '#bc243c', '#c7a252', '#ff9f80', '#ffcd3c', 
    '#56d9fe', '#a56cc1', '#00cc99', '#ff6b6b', '#ff847c', 
    '#a8e6cf', '#ffd3b6', '#ff8b94', '#ffeead', '#dcedc1'
])

# Customizing the plot
plt.xlabel('GDP in Millions')
plt.title('GDP of Major Countries', pad=20)
plt.xlim(300000, 23000000)
plt.xticks(rotation=45)

# Show the plot
plt.show()