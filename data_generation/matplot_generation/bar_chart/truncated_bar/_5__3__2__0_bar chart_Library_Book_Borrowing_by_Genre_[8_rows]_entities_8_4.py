
import matplotlib.pyplot as plt

# Data
countries = [
    "USA", "Switzerland", "Germany", "Netherlands", "Sweden", "France", 
    "Canada", "Japan", "Australia", "South Korea", "Italy", "Spain", 
    "United Kingdom", "Norway", "Denmark"
]
health_expenditure = [17.1, 12.3, 11.2, 10.4, 11.0, 11.5, 10.7, 10.9, 9.8, 8.1, 8.8, 8.4, 10.0, 10.5, 10.1]
life_expectancy = [78.5, 83.6, 81.1, 82.2, 82.5, 82.9, 82.3, 84.5, 83.0, 82.8, 83.4, 83.2, 81.3, 82.4, 81.0]
obesity_rate = [36.2, 19.4, 22.3, 20.4, 20.6, 24.5, 29.4, 4.3, 29.0, 4.7, 19.9, 23.8, 28.1, 23.1, 19.7]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(12, 14))

# Vertical bar chart
bars_health = ax.bar(countries, health_expenditure, color='#1f77b4', width=0.5, label='Health Expenditure')
bars_life = ax.bar(countries, life_expectancy, bottom=health_expenditure, color='#ff7f0e', width=0.5, label='Life Expectancy')
bars_obesity = ax.bar(countries, obesity_rate, bottom=[i+j for i,j in zip(health_expenditure, life_expectancy)], color='#2ca02c', width=0.5, label='Obesity Rate')

# Set the title and labels
ax.set_title('Health Statistics of Various Countries', fontsize=18, pad=20)
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Values', fontsize=14)

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Set y-axis limits to truncate the chart
ax.set_ylim(20, 85)

# Show Values on Bars
for bar in bars_health:
    height = bar.get_height()
    label_y_pos = height - 2
    ax.text(bar.get_x() + bar.get_width() / 2, label_y_pos, f'{height}', ha='center', va='center', color='white')

for bar in bars_life:
    height = bar.get_height()
    label_y_pos = bar.get_y() + height - 2
    ax.text(bar.get_x() + bar.get_width() / 2, label_y_pos, f'{height}', ha='center', va='center', color='white')

for bar in bars_obesity:
    height = bar.get_height()
    label_y_pos = bar.get_y() + height - 2
    ax.text(bar.get_x() + bar.get_width() / 2, label_y_pos, f'{height}', ha='center', va='center', color='white')

# Add a legend
ax.legend(loc='upper right', fontsize=12)

# Set the layout to be tight
plt.tight_layout()

# Show the plot
plt.show()