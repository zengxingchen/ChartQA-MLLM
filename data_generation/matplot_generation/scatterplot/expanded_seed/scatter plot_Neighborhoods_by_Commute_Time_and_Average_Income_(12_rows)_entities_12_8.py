
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Neighborhood': 'Elmwood', 'Average Commute Time (min)': 30, 'Average Income (USD)': 45000},
    {'Neighborhood': 'Pinecrest', 'Average Commute Time (min)': 45, 'Average Income (USD)': 55000},
    {'Neighborhood': 'Maple Grove', 'Average Commute Time (min)': 35, 'Average Income (USD)': 47000},
    {'Neighborhood': 'Oakdale', 'Average Commute Time (min)': 60, 'Average Income (USD)': 62000},
    {'Neighborhood': 'Cedar Bluff', 'Average Commute Time (min)': 50, 'Average Income (USD)': 50000},
    {'Neighborhood': 'Willow Park', 'Average Commute Time (min)': 20, 'Average Income (USD)': 39500},
    {'Neighborhood': 'Sycamore Heights', 'Average Commute Time (min)': 55, 'Average Income (USD)': 58000},
    {'Neighborhood': 'Rosewood', 'Average Commute Time (min)': 40, 'Average Income (USD)': 57000},
    {'Neighborhood': 'Hickory Corner', 'Average Commute Time (min)': 25, 'Average Income (USD)': 43000},
    {'Neighborhood': 'Aspen Meadows', 'Average Commute Time (min)': 30, 'Average Income (USD)': 48000},
    {'Neighborhood': 'Birchwood', 'Average Commute Time (min)': 65, 'Average Income (USD)': 64000},
    {'Neighborhood': 'Iron Gate', 'Average Commute Time (min)': 70, 'Average Income (USD)': 67000}
]

# Extracting data
neighborhoods = [item['Neighborhood'] for item in data]
commute_times = [item['Average Commute Time (min)'] for item in data]
incomes = [item['Average Income (USD)'] for item in data]

# Normalizing data for color mapping
income_normalized = [(income - min(incomes)) / (max(incomes) - min(incomes)) for income in incomes]

# Setting up color map
color_map = plt.cm.get_cmap('viridis')

# Creating the scatter plot
plt.figure(figsize=(14,8))
scatter = plt.scatter(commute_times, incomes, s=100, c=income_normalized, cmap=color_map, alpha=0.6, edgecolors='w')

# Adding labels
for i, neighborhood in enumerate(neighborhoods):
    plt.text(commute_times[i], incomes[i], neighborhood, fontsize=9, ha='center')

# Adding color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Normalized Average Income')

# Adding titles and labels
plt.title('Scatter Plot of Average Commute Times and Incomes by Neighborhood')
plt.xlabel('Average Commute Time (min)')
plt.ylabel('Average Income (USD)')

# Adjusting layout to prevent clip of tick-label
plt.tight_layout()

# Show plot
plt.show()