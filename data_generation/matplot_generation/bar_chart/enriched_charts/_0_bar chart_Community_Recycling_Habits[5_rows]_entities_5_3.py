
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City', 'Cairo', 'Mumbai', 'Beijing', 'Dhaka', 'Osaka']
population = [37435191, 29399141, 26317104, 21846507, 21671908, 20484965, 20411274, 20035455, 19751581, 19222665]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Figure size
plt.figure(figsize=(10, 8))

# Horizontal bar chart
plt.barh(cities, population, color=colors, height=0.5)

# Labeling
plt.xlabel('Population')
plt.title('Top 10 Most Populous Cities in the World')
plt.gca().invert_yaxis()  # Invert y-axis to have the city with highest population at the top

# Show and save plot
plt.tight_layout()
plt.show()