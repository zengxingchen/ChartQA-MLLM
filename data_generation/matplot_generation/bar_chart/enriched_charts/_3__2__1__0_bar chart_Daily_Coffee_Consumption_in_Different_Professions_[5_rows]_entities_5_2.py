
import matplotlib.pyplot as plt

# Data for plotting
countries = ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada']
gdp = [25.3, 18.2, 5.1, 4.2, 3.7, 3.2, 3.1, 2.3, 2.1, 1.8]

# Define the colors for each bar
colors = ['#3498DB', '#E74C3C', '#9B59B6', '#1ABC9C', '#F39C12', '#D35400', '#34495E', '#27AE60', '#E67E22', '#7F8C8D']

fig, ax = plt.subplots(figsize=(12, 10))

# Create vertical bars
ax.bar(countries, gdp, color=colors, edgecolor='black', width=0.6)

# Set chart title and labels
ax.set_title('Top 10 Countries by GDP (2024)', fontsize=18, pad=20)
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('GDP (Trillions USD)', fontsize=14)

# Set the limits for the y-axis
ax.set_ylim(0, max(gdp) + 5)

# Show the actual data points on the bars
for i, v in enumerate(gdp):
    ax.text(i, v + 0.3, str(v), color='black', ha='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off x ticks for cleaner look
ax.xaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()