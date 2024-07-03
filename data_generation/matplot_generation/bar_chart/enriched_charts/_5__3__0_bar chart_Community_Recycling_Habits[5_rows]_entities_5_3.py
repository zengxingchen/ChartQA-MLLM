
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'China', 'Japan', 'Great Britain', 'Russia', 'Australia', 'Netherlands', 'France', 'Germany', 'Italy', 'Canada', 'Brazil', 'New Zealand', 'Cuba', 'Hungary', 'South Korea', 'Spain', 'Poland', 'Turkey', 'Norway']
gold_medals = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6, 6, 3, 4, 2, 4]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5']

# Figure size
plt.figure(figsize=(10, 8))

# Horizontal bar chart
plt.barh(countries, gold_medals, color=colors, height=0.6)

# Labeling
plt.xlabel('Number of Gold Medals')
plt.title('Gold Medals Won by Countries in Recent Olympics')

# Set y-axis limits
plt.xlim(2, 45)

# Rotate y-axis labels for better readability
plt.yticks(rotation=0, ha='right')

# Show and save plot
plt.tight_layout()
plt.show()