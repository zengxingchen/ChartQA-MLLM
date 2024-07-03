
import matplotlib.pyplot as plt

# Data for the new chart
data = [
    {'Day': 'Monday', 'Popularity': 70},
    {'Day': 'Tuesday', 'Popularity': 50},
    {'Day': 'Wednesday', 'Popularity': 75},
    {'Day': 'Thursday', 'Popularity': 60},
    {'Day': 'Friday', 'Popularity': 90},
    {'Day': 'Saturday', 'Popularity': 100},
    {'Day': 'Sunday', 'Popularity': 85}
]

# Extracting the days and popularity into separate lists
days = [entry['Day'] for entry in data]
popularity = [entry['Popularity'] for entry in data]

# Creating the line chart
plt.figure(figsize=(16, 10))  # Set the size of the figure

# Plot the data
plt.plot(days, popularity, color='#3498db', linestyle='-', marker='o', linewidth=2, markersize=8, label="Weekly Popularity")

# Add titles and labels
plt.title('Weekly Popularity in Music & Performing Arts', fontsize=18, loc='center')
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Popularity Index', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add more diversified visual encoding such as text annotations for the data points
for i, count in enumerate(popularity):
    plt.text(days[i], count + 3, str(count), ha='center', color='black')

# Highlight the max and min popularity
max_popularity = max(popularity)
min_popularity = min(popularity)
plt.axhline(max_popularity, color='#2ecc71', linestyle='--', linewidth=1)
plt.axhline(min_popularity, color='#e74c3c', linestyle='--', linewidth=1)

# Adjust y-axis to be inverted
plt.gca().invert_yaxis()

# Add a legend
plt.legend(loc='upper right')

# Show the plot
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()