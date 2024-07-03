
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Item': 'Espresso', 'Monday': '40%', 'Tuesday': '35%', 'Wednesday': '50%', 'Thursday': '45%', 'Friday': '40%'},
    {'Item': 'Latte', 'Monday': '30%', 'Tuesday': '40%', 'Wednesday': '25%', 'Thursday': '30%', 'Friday': '35%'},
    {'Item': 'Cappuccino', 'Monday': '20%', 'Tuesday': '15%', 'Wednesday': '15%', 'Thursday': '15%', 'Friday': '10%'},
    {'Item': 'Tea', 'Monday': '10%', 'Tuesday': '10%', 'Wednesday': '10%', 'Thursday': '10%', 'Friday': '15%'}
]

# Extract the days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Initialize a dictionary to hold percentages for each item per day
percentages = {day: [] for day in days}
items = []

# Populate the percentages dictionary and items list
for entry in data:
    items.append(entry['Item'])
    for day in days:
        percentages[day].append(float(entry[day].rstrip('%')) / 100)  # Convert strings to float and remove the '%' sign

# Initialize the bottom for the stacked bars
bottoms = [0] * len(days)

# Set up colors for each stack
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Feel free to change the color codes

# Create the figure and axis objects
fig, ax = plt.subplots()

for idx, item in enumerate(items):
    ax.bar(days, percentages[day][idx], bottom=bottoms, label=item, color=colors[idx])
    # Update the bottoms array to stack the next item on top
    bottoms = [bottoms[j] + percentages[day][idx] for j in range(len(days))]

# Add labels and title
ax.set_ylabel('Percentage')
ax.set_title('Sales Distribution by Items Throughout the Week')

# Format y-ticks as percentages
plt.yticks(ticks=[i/10 for i in range(0, 11)], labels=['{}%'.format(i*10) for i in range(0, 11)])

# Add legend
ax.legend()

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()