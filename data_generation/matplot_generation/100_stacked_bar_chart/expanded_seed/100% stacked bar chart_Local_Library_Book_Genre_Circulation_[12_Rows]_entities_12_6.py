
import matplotlib.pyplot as plt
import numpy as np

# Data from the chart table provided by user
table_data = [
    {'Genre': 'Science Fiction', 'January': '12%', 'February': '10%', 'March': '11%', 'April': '13%', 'May': '12%', 'June': '9%', 'July': '7%', 'August': '8%', 'September': '10%', 'October': '11%', 'November': '12%', 'December': '10%'},
    {'Genre': 'Mystery', 'January': '15%', 'February': '17%', 'March': '16%', 'April': '14%', 'May': '13%', 'June': '15%', 'July': '14%', 'August': '15%', 'September': '14%', 'October': '16%', 'November': '15%', 'December': '17%'},
    # ... (other genres as provided in the table_data)
    {'Genre': 'Other', 'January': '4%', 'February': '4%', 'March': '4%', 'April': '4%', 'May': '4%', 'June': '4%', 'July': '4%', 'August': '4%', 'September': '4%', 'October': '4%', 'November': '4%', 'December': '4%'}
]

# Months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Convert percentages to actual values (0-1 range)
data = {genre['Genre']: [float(value.strip('%'))/100 for value in genre.values() if value.endswith('%')] for genre in table_data}

# Create an array for the month labels on the x-axis
indices = np.arange(len(months))

# Initialize the bottom array for stacking
bottom = np.zeros(len(months))

# Colors and hatch patterns for visual variety
colors = plt.cm.get_cmap('tab20').colors
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']

# Generate the bars for each genre
for i, (genre, values) in enumerate(data.items()):
    plt.bar(indices, values, bottom=bottom, color=colors[i % len(colors)], label=genre, hatch=hatches[i % len(hatches)])
    bottom += values

# Customizing the plot
plt.xlabel('Month')
plt.ylabel('Percentage (%)')
plt.title('Book Genre Popularity (100% Stacked Bar Chart)')
plt.xticks(indices, months, rotation=45)
plt.yticks(np.arange(0, 1.1, 0.1), [f"{int(val*100)}%" for val in np.arange(0, 1.1, 0.1)])
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Genres")

# Ensure the stacked bar takes up the full 100%
plt.ylim(0, 1)

# Display the plot
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Make space for the legend
plt.show()