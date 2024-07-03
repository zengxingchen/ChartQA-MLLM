
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
plt.figure(figsize=(16, 10))
plt.bar(countries, gdp, width=0.6, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', 
    '#ffff33', '#a65628', '#f781bf', '#999999', '#e7298a', 
    '#66a61e', '#e6ab02', '#a6761d', '#666666', '#1b9e77', 
    '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', 
    '#a6761d', '#666666', '#1b9e77', '#d95f02', '#7570b3', 
    '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00'
])

# Customizing the plot
plt.ylabel('GDP in Millions')
plt.title('GDP Distribution of Major Countries', pad=20)
plt.ylim(300000, 23000000)
plt.xticks(rotation=90)

# Show the plot
plt.show()