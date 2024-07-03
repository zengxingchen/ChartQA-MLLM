
import matplotlib.pyplot as plt

# Data for plotting
cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mexico City', 'Cairo', 'Mumbai', 'Beijing', 'Dhaka', 'Osaka']
population = [37.4, 30.3, 27.0, 22.0, 21.6, 20.4, 20.0, 19.6, 19.3, 19.0]

# Define the colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', '#FFA133', '#5733FF', '#FF3333', '#33FF8C']

fig, ax = plt.subplots(figsize=(14, 8))

# Create horizontal bars
ax.barh(cities, population, color=colors, edgecolor='black', height=0.5)

# Set chart title and labels
ax.set_title('Top 10 Most Populated Cities in 2024', fontsize=18, pad=20)
ax.set_xlabel('Population (Millions)', fontsize=14)
ax.set_ylabel('City', fontsize=14)

# Set the limits for the x-axis
ax.set_xlim(15, max(population) + 5)

# Show the actual data points on the bars
for i, v in enumerate(population):
    ax.text(v + 0.5, i, str(v), color='black', va='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off y ticks for cleaner look
ax.yaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()