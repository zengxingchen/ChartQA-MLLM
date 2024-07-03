import matplotlib.pyplot as plt

# Data for plotting
countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico']
population = [1440, 1390, 332, 276, 225, 214, 211, 167, 145, 129]

# Define the colors for each bar
colors = ['#FF6347', '#4682B4', '#3CB371', '#FFD700', '#8A2BE2', '#FF69B4', '#A52A2A', '#00CED1', '#DA70D6', '#7FFF00']

fig, ax = plt.subplots(figsize=(14, 8))

# Create horizontal bars
ax.barh(countries, population, color=colors, edgecolor='black', height=0.5)

# Set chart title and labels
ax.set_title('Top 10 Most Populous Countries (2024)', fontsize=18, pad=20)
ax.set_xlabel('Population (Millions)', fontsize=14)
ax.set_ylabel('Country', fontsize=14)

# Set the limits for the x-axis
ax.set_xlim(0, max(population) + 200)

# Show the actual data points on the bars
for i, v in enumerate(population):
    ax.text(v + 20, i, str(v), color='black', va='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off y ticks for cleaner look
ax.yaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()