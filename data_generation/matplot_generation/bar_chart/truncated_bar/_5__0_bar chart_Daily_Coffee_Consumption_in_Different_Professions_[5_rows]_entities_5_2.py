
import matplotlib.pyplot as plt

# Data for plotting
countries = ['Japan', 'Switzerland', 'Singapore', 'Australia', 'Spain', 'Italy', 
             'Iceland', 'Israel', 'Sweden', 'France', 'South Korea', 'Canada', 
             'Norway', 'United Kingdom', 'Germany', 'United States']
life_expectancy = [84.6, 83.3, 83.2, 82.9, 82.8, 82.7, 82.7, 82.6, 82.4, 82.3, 
                   82.1, 82.0, 81.8, 81.3, 81.0, 78.9]

# Define the colors for each bar
colors = ['#FF5733', '#FF7D33', '#FFA133', '#FFC533', '#FFE633', 
          '#BFFF33', '#8FFF33', '#6AFF33', '#33FF57', '#33FF8E', 
          '#33FFFF', '#3378FF', '#3355FF', '#6A33FF', '#A033FF', '#D633FF']

fig, ax = plt.subplots(figsize=(10, 15))

# Create vertical bars
ax.bar(countries, life_expectancy, color=colors, edgecolor='black', width=0.7)

# Set chart title and labels
ax.set_title('Life Expectancy by Country (2024)', fontsize=18)
ax.set_ylabel('Life Expectancy (Years)', fontsize=14)
ax.set_xlabel('Country', fontsize=14)

# Set the limits for the y-axis
ax.set_ylim(75, 85)

# Show the actual data points on the bars
for i, v in enumerate(life_expectancy):
    ax.text(i, v + 0.2, str(v), color='black', ha='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)

# Turn off x ticks for cleaner look
ax.xaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.show()