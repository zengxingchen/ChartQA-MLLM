
import matplotlib.pyplot as plt

# Input data
data = [
    {'Year': 2019, 'Glass': 120, 'Paper': 250, 'Plastic': 160, 'Metals': 90},
    {'Year': 2020, 'Glass': 130, 'Paper': 265, 'Plastic': 175, 'Metals': 95},
    {'Year': 2021, 'Glass': 150, 'Paper': 280, 'Plastic': 190, 'Metals': 110},
    {'Year': 2022, 'Glass': 160, 'Paper': 300, 'Plastic': 200, 'Metals': 120},
    {'Year': 2023, 'Glass': 170, 'Paper': 320, 'Plastic': 215, 'Metals': 130}
]

# Extracting the years and the materials data
years = [entry['Year'] for entry in data]
glass = [entry['Glass'] for entry in data]
paper = [entry['Paper'] for entry in data]
plastic = [entry['Plastic'] for entry in data]
metals = [entry['Metals'] for entry in data]

# Bottom positions for the bars
paper_bottom = [g + p for g, p in zip(glass, paper)]
plastic_bottom = [p + b for p, b in zip(paper_bottom, plastic)]
metals_bottom = [pl + m for pl, m in zip(plastic_bottom, metals)]

# Plotting the data
plt.bar(years, glass, label='Glass', color='skyblue')
plt.bar(years, paper, label='Paper', color='lightgreen', bottom=glass)
plt.bar(years, plastic, label='Plastic', color='lightcoral', bottom=paper_bottom)
plt.bar(years, metals, label='Metals', color='lightgrey', bottom=plastic_bottom)

# Adding other elements to the bar chart
plt.xlabel('Year')
plt.ylabel('Amount (in tons)')
plt.title('Materials Recycled over Years')
plt.xticks(years)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()