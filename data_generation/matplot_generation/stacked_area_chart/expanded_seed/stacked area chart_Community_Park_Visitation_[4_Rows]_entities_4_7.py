
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Year': 2018, 'Playground': 1200, 'Running Track': 1800, 'Picnic Area': 1500, 'Pond': 800},
    {'Year': 2019, 'Playground': 1250, 'Running Track': 1900, 'Picnic Area': 1550, 'Pond': 850},
    {'Year': 2020, 'Playground': 900, 'Running Track': 1500, 'Picnic Area': 1000, 'Pond': 500},
    {'Year': 2021, 'Playground': 1300, 'Running Track': 2000, 'Picnic Area': 1600, 'Pond': 900}
]

# Extracting the data
years = [item['Year'] for item in data]
playground_values = [item['Playground'] for item in data]
running_track_values = [item['Running Track'] for item in data]
picnic_area_values = [item['Picnic Area'] for item in data]
pond_values = [item['Pond'] for item in data]

# Plotting the stacked area chart
fig, ax = plt.subplots()

ax.stackplot(years, playground_values, labels=['Playground'], colors=['#FFD700'], alpha=0.8)
ax.stackplot(years, running_track_values, labels=['Running Track'], colors=['#FF8C00'], alpha=0.7)
ax.stackplot(years, picnic_area_values, labels=['Picnic Area'], colors=['#1E90FF'], alpha=0.5)
ax.stackplot(years, pond_values, labels=['Pond'], colors=['#32CD32'], alpha=0.3)

# Adding title and labels
plt.title('Usage of Park Areas Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Visitors')

# Adding legend
plt.legend(loc='upper left')

# Adding grid
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Show plot
plt.show()