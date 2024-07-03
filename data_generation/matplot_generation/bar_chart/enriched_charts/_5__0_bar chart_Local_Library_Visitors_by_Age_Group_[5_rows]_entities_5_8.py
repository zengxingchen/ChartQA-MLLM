
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "Chicago", "Houston",
    "Phoenix", "Philadelphia", "San Antonio", "San Diego", 
    "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", 
    "Columbus", "Charlotte"
]
crime_rates = [5.2, 7.1, 6.8, 8.4, 4.9, 5.7, 7.3, 3.8, 6.4, 3.9, 4.5, 6.0, 6.3, 4.7, 5.1]

# Colors for each city
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF',
    '#33FFF3', '#FFB833', '#FF3333', '#5733FF', '#FF5733',
    '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF3'
]

# Plot
fig, ax = plt.subplots(figsize=(10, 14))
bars = ax.bar(cities, crime_rates, color=colors, width=0.5) # Adjusted bar width to 0.5

# Set the title and labels
ax.set_title('Crime Rates in Various Cities', fontsize=15, pad=20)
ax.set_ylabel('Crime Rate (per 1000 people)', fontsize=12)
ax.set_xlabel('City', fontsize=12)

# Customize the tick labels
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)

# Set y-axis limit starting from a specific value
ax.set_ylim(3, 9)

# Add the data values on the bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 0.2
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height}', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()