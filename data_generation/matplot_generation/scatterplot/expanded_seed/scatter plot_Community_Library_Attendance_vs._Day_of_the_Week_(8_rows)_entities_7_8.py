
import matplotlib.pyplot as plt

# Given data
data = [
    {'Day of the Week': 'Monday', 'Visitors': 150, "Children's Book Borrowed": 60},
    {'Day of the Week': 'Tuesday', 'Visitors': 100, "Children's Book Borrowed": 40},
    {'Day of the Week': 'Wednesday', 'Visitors': 130, "Children's Book Borrowed": 55},
    {'Day of the Week': 'Thursday', 'Visitors': 90, "Children's Book Borrowed": 30},
    {'Day of the Week': 'Friday', 'Visitors': 200, "Children's Book Borrowed": 75},
    {'Day of the Week': 'Saturday', 'Visitors': 220, "Children's Book Borrowed": 100},
    {'Day of the Week': 'Sunday', 'Visitors': 180, "Children's Book Borrowed": 85}
]

# Extracting the day labels for the x-axis
days = [d['Day of the Week'] for d in data]

# Encoding the days of the week as numerical values for plotting
day_mapping = {day: i for i, day in enumerate(days)}
numerical_days = [day_mapping[day] for day in days]

# Visitors will be on the y-axis
visitors = [d['Visitors'] for d in data]

# The size of points will represent the number of Children's Book Borrowed
book_borrowed = [d["Children's Book Borrowed"] for d in data]
sizes = [borrowed * 10 for borrowed in book_borrowed]  # Multiplying by 10 for better visualization

# We can also map each day to a color
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink']

# Create the scatter plot
plt.figure(figsize=(10, 6))

for i, day in enumerate(days):
    plt.scatter(numerical_days[i], visitors[i], s=sizes[i], c=colors[i], label=day, alpha=0.6, edgecolors='w')

# Add titles and labels
plt.title('Library Visitors and Children\'s Books Borrowed Over a Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Visitors')

# Adding day labels to the x-axis
plt.xticks(ticks=list(day_mapping.values()), labels=days, rotation=45)

# Adding a legend to explain sizes
for size in [30, 60, 90]:
    plt.scatter([], [], c='k', alpha=0.6, s=size,
                label=str(size // 10) + " Children's Books Borrowed")

plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Day & Books Borrowed')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()