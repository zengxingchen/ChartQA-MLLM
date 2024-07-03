
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Month': 'January', 'Number of Visitors': 1530},
    {'Month': 'February', 'Number of Visitors': 1870},
    {'Month': 'March', 'Number of Visitors': 2050},
    {'Month': 'April', 'Number of Visitors': 1720},
    {'Month': 'May', 'Number of Visitors': 1980}
]

# Extract the months and the number of visitors
months = [entry['Month'] for entry in data]
visitors = [entry['Number of Visitors'] for entry in data]

# Generate a list of colors, one for each month
colors = plt.cm.rainbow([i/len(months) for i in range(len(months))])

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Set the figure size

# Scatter plot, assigning a unique marker and color to each month
for i, (month, num_visitors) in enumerate(zip(months, visitors)):
    plt.scatter(month, num_visitors, color=colors[i], label=month, s=100)

# Title and labels
plt.title('Number of Visitors per Month')
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Grid lines for readability
plt.grid(True)

# Annotate each point with the number of visitors
for i, txt in enumerate(visitors):
    plt.annotate(txt, (months[i], visitors[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Legend could be used if needed, but it might clutter the plot in this case
# plt.legend()

# Display the plot
plt.show()