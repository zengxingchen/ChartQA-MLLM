
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Profession': 'Software Engineers', 'Cups of Coffee Consumed Per Day': 3},
    {'Profession': 'Teachers', 'Cups of Coffee Consumed Per Day': 2},
    {'Profession': 'Nurses', 'Cups of Coffee Consumed Per Day': 4},
    {'Profession': 'Lawyers', 'Cups of Coffee Consumed Per Day': 2},
    {'Profession': 'Truck Drivers', 'Cups of Coffee Consumed Per Day': 5}
]

# Extracting profession names and corresponding cups of coffee consumed per day
professions = [item['Profession'] for item in data]
cups_of_coffee = [item['Cups of Coffee Consumed Per Day'] for item in data]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Colors, edge colors and hatch patterns for diversifying the bars
colors = ['blue', 'green', 'red', 'purple', 'orange']
edge_colors = ['black', 'darkgreen', 'darkred', 'indigo', 'darkorange']
hatch_patterns = ['/', '\\', '|', '-', '+']

# Creating the bar chart
bars = ax.bar(professions, cups_of_coffee, color=colors, edgecolor=edge_colors, hatch=hatch_patterns)

# Adding the data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom')

# Setting the title and labels
ax.set_title('Cups of Coffee Consumed Per Day by Profession')
ax.set_xlabel('Profession')
ax.set_ylabel('Cups of Coffee Consumed Per Day')

# Rotating the x-axis labels to fit and make them readable
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()