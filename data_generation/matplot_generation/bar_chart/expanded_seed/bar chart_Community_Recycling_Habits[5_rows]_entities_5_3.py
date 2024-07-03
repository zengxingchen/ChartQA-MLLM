
import matplotlib.pyplot as plt
import numpy as np

# Data from the provided table
data = [
    {'Year': 2018, 'Plastic Recycling (tons)': 1200, 'Paper Recycling (tons)': 3000,
     'Glass Recycling (tons)': 800, 'Metal Recycling (tons)': 500},
    {'Year': 2019, 'Plastic Recycling (tons)': 1300, 'Paper Recycling (tons)': 3200,
     'Glass Recycling (tons)': 900, 'Metal Recycling (tons)': 600},
    {'Year': 2020, 'Plastic Recycling (tons)': 1250, 'Paper Recycling (tons)': 3100,
     'Glass Recycling (tons)': 850, 'Metal Recycling (tons)': 550},
    {'Year': 2021, 'Plastic Recycling (tons)': 1400, 'Paper Recycling (tons)': 3300,
     'Glass Recycling (tons)': 920, 'Metal Recycling (tons)': 620},
    {'Year': 2022, 'Plastic Recycling (tons)': 1450, 'Paper Recycling (tons)': 3450,
     'Glass Recycling (tons)': 950, 'Metal Recycling (tons)': 700}
]

# Parsing data
years = [item['Year'] for item in data]
plastic = [item['Plastic Recycling (tons)'] for item in data]
paper = [item['Paper Recycling (tons)'] for item in data]
glass = [item['Glass Recycling (tons)'] for item in data]
metal = [item['Metal Recycling (tons)'] for item in data]

# Bar chart configuration
bar_width = 0.35
index = np.arange(len(years))

# Plotting the bars
fig, ax = plt.subplots()

bars_plastic = ax.bar(index, plastic, bar_width, label='Plastic', color='blue', alpha=0.6)
bars_paper = ax.bar(index, paper, bar_width, label='Paper', color='green', alpha=0.6, bottom=plastic)
bars_glass = ax.bar(index, glass, bar_width, label='Glass', color='red', alpha=0.6, 
                    bottom=[i+j for i,j in zip(plastic, paper)])
bars_metal = ax.bar(index, metal, bar_width, label='Metal', color='yellow', alpha=0.6, 
                    bottom=[i+j+k for i,j,k in zip(plastic, paper, glass)])

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Recycling (tons)')
ax.set_title('Recycling Statistics by Material and Year')
ax.set_xticks(index)
ax.set_xticklabels(years)

# Adding a legend
ax.legend()

# Showing the plot
plt.show()