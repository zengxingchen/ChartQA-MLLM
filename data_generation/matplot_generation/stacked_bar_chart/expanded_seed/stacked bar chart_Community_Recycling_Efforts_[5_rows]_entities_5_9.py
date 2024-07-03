
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Year': 2018, 'Paper (tons)': 1250, 'Glass (tons)': 800, 'Plastic (tons)': 950, 'Metal (tons)': 600},
    {'Year': 2019, 'Paper (tons)': 1300, 'Glass (tons)': 850, 'Plastic (tons)': 1100, 'Metal (tons)': 650},
    {'Year': 2020, 'Paper (tons)': 1400, 'Glass (tons)': 900, 'Plastic (tons)': 1200, 'Metal (tons)': 700},
    {'Year': 2021, 'Paper (tons)': 1500, 'Glass (tons)': 950, 'Plastic (tons)': 1300, 'Metal (tons)': 750},
    {'Year': 2022, 'Paper (tons)': 1600, 'Glass (tons)': 1000, 'Plastic (tons)': 1400, 'Metal (tons)': 800}
]

# Extract the years and each material amount
years = [entry['Year'] for entry in data]
paper = [entry['Paper (tons)'] for entry in data]
glass = [entry['Glass (tons)'] for entry in data]
plastic = [entry['Plastic (tons)'] for entry in data]
metal = [entry['Metal (tons)'] for entry in data]

# Plotting the stacked bar chart
fig, ax = plt.subplots()

ax.bar(years, paper, label='Paper', color='tan')
ax.bar(years, glass, bottom=paper, label='Glass', color='skyblue')
ax.bar(years, plastic, bottom=[i+j for i,j in zip(paper, glass)], label='Plastic', color='lightgreen')
ax.bar(years, metal, bottom=[i+j+k for i,j,k in zip(paper, glass, plastic)], label='Metal', color='silver')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Recycled Material (tons)')
plt.title('Recycled Materials by Year')

# Adding legend
plt.legend()

# Display the values on the bars to enhance readability.
for i, v in enumerate(paper):
    plt.text(years[i] - 0.15, v / 2, str(v), color='black', fontweight='bold')
    
for i, v in enumerate(glass):
    plt.text(years[i] - 0.15, v / 2 + paper[i], str(v), color='black', fontweight='bold')
    
for i, v in enumerate(plastic):
    plt.text(years[i] - 0.15, v / 2 + paper[i] + glass[i], str(v), color='black', fontweight='bold')
    
for i, v in enumerate(metal):
    plt.text(years[i] - 0.15, v / 2 + paper[i] + glass[i] + plastic[i], str(v), color='black', fontweight='bold')

# Show the plot
plt.show()