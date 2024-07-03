
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
    "Indianapolis", "San Francisco", "Seattle", "Denver", "Washington",
    "Boston", "Detroit", "Nashville", "Memphis", "Portland",
    "Las Vegas", "Louisville", "Baltimore", "Milwaukee", "Oklahoma City"
]
unemployment_rates = [
    5.2, 4.8, 6.1, 5.4, 4.6,
    6.0, 4.3, 4.1, 5.3, 3.9,
    3.8, 4.7, 5.5, 4.2, 4.5,
    5.0, 3.7, 4.0, 3.6, 3.4,
    3.5, 6.3, 3.9, 5.7, 4.3,
    6.6, 4.6, 6.4, 5.8, 4.0
]

# Colors for each city
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#A533FF',
    '#FF8533', '#33FFF5', '#F5FF33', '#FF3357', '#33FFA5',
    '#8533FF', '#FF33F5', '#FF5733', '#33FF57', '#3357FF',
    '#FF33A5', '#A533FF', '#FF8533', '#33FFF5', '#F5FF33',
    '#FF3357', '#33FFA5', '#8533FF', '#FF33F5', '#FF5733',
    '#33FF57', '#3357FF', '#FF33A5', '#A533FF', '#FF8533'
]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))
bars = ax.bar(cities, unemployment_rates, color=colors, width=0.7) # Adjusted bar width to 0.7

# Set the title and labels
ax.set_title('Unemployment Rates in Various Cities', fontsize=18)
ax.set_xlabel('City', fontsize=15)
ax.set_ylabel('Unemployment Rate (%)', fontsize=15)

# Customize the tick labels
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)

# Set the y-axis limit to start from 3
ax.set_ylim(3, 7)

# Add the data values on the bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 0.1
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height}%', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()