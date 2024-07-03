
import matplotlib.pyplot as plt

# Example data
data = [
    {'Month': 'January', 'Children (0-12)': 120, 'Teens (13-19)': 80, 'Adults (20-64)': 300, 'Seniors (65+)': 100},
    {'Month': 'February', 'Children (0-12)': 115, 'Teens (13-19)': 75, 'Adults (20-64)': 290, 'Seniors (65+)': 95},
    # ... (include all other months here)
    {'Month': 'March (next year)', 'Children (0-12)': 145, 'Teens (13-19)': 105, 'Adults (20-64)': 380, 'Seniors (65+)': 130}
]

# Parsing the data
months = [entry['Month'] for entry in data]
children = [entry['Children (0-12)'] for entry in data]
teens = [entry['Teens (13-19)'] for entry in data]
adults = [entry['Adults (20-64)'] for entry in data]
seniors = [entry['Seniors (65+)'] for entry in data]

# Define the width of the bars and x positions
bar_width = 0.5
x = range(len(months))

# Starting points for the stacked bars
teens_start = [c for c in children]
adults_start = [c+t for c, t in zip(children, teens)]
seniors_start = [c+t+a for c, t, a in zip(children, teens, adults)]

# Plotting the stacked bar chart
plt.bar(x, children, width=bar_width, label='Children (0-12)', color='skyblue')
plt.bar(x, teens, width=bar_width, bottom=teens_start, label='Teens (13-19)', color='orange')
plt.bar(x, adults, width=bar_width, bottom=adults_start, label='Adults (20-64)', color='lightgreen')
plt.bar(x, seniors, width=bar_width, bottom=seniors_start, label='Seniors (65+)', color='purple')

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Number of People')
plt.title('Monthly Demographics')

# Adding x-axis labels rotated for better readability
plt.xticks(x, months, rotation=45)

# Adding a legend
plt.legend()

# Adjusting the subplot for better layout
plt.tight_layout()

# Display the plot
plt.show()