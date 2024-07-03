
import matplotlib.pyplot as plt

# Data
sports = ['Soccer', 'Basketball', 'Cricket', 'Tennis', 'Rugby', 'Baseball', 'Hockey', 'Swimming', 'Boxing', 'Athletics']
popularity = [4000, 2800, 3500, 2500, 1800, 2400, 2200, 2300, 1600, 1900]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF5', '#FF9933', '#99FF33', '#33FF99', '#5733FF']

# Figure size
plt.figure(figsize=(12, 6))

# Vertical bar chart
plt.bar(sports, popularity, color=colors, width=0.6)

# Labeling
plt.ylabel('Popularity (in millions)')
plt.title('Top 10 Most Popular Sports in the World')
plt.xticks(rotation=45, ha='right')

# Show and save plot
plt.tight_layout()
plt.show()