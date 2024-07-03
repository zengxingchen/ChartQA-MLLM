
import matplotlib.pyplot as plt

# Sample data for stacked bar chart
stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E', 'Store F', 'Store G', 'Store H', 'Store I', 'Store J']
robotics = [12, 18, 10, 14, 22, 17, 20, 16, 19, 15]
renewable_energy = [8, 12, 6, 10, 15, 13, 14, 9, 11, 7]
biotechnology = [5, 7, 4, 6, 10, 8, 9, 6, 7, 5]
ai_solutions = [9, 15, 8, 12, 20, 16, 18, 13, 17, 12]

# Stacked bar chart configuration
fig, ax = plt.subplots(figsize=(12, 8))  # Set width and height of the chart
bars1 = ax.barh(stores, robotics, label='Robotics', color='#4c72b0', edgecolor='white', height=0.6)
bars2 = ax.barh(stores, renewable_energy, label='Renewable Energy', color='#55a868', edgecolor='white', height=0.6, left=robotics)
bars3 = ax.barh(stores, biotechnology, label='Biotechnology', color='#c44e52', edgecolor='white', height=0.6, left=[i+j for i, j in zip(robotics, renewable_energy)])
bars4 = ax.barh(stores, ai_solutions, label='AI Solutions', color='#8172b2', edgecolor='white', height=0.6, left=[i+j+k for i, j, k in zip(robotics, renewable_energy, biotechnology)])

# Labeling and customization
ax.set_ylabel('Stores')
ax.set_xlabel('Sales (Thousands of Dollars)')
ax.set_title('Investment in Future Technologies by Store')
ax.legend()

# Display the chart
plt.show()