
import matplotlib.pyplot as plt
import numpy as np

# Provided data
data = [
    {'Month': 'January', 'Visitors': 1200},
    {'Month': 'February', 'Visitors': 1400},
    {'Month': 'March', 'Visitors': 1250},
    {'Month': 'April', 'Visitors': 1350},
    {'Month': 'May', 'Visitors': 1450}
]

# Extracting Month and Visitors from the data
months = [entry['Month'] for entry in data]
visitors = np.array([entry['Visitors'] for entry in data])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create an area chart
ax.fill_between(months, visitors, color="skyblue", alpha=0.4)
ax.plot(months, visitors, color="Slateblue", alpha=0.6, linewidth=2)

# Adding details
ax.set_title('Monthly Visitors', fontsize=18)     # Set the title
ax.set_xlabel('Month', fontsize=14)               # Set the x-axis label
ax.set_ylabel('Number of Visitors', fontsize=14)  # Set the y-axis label

# Customizing the grid
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight the data points on the line
for i in range(len(months)):
    plt.text(months[i], visitors[i] + 50, f"{visitors[i]}", ha='center')

# Beautify the plot
ax.set_facecolor('whitesmoke')           # Set the background color for the plot
plt.xticks(rotation=45)                   # Rotate the x-axis labels for better readability
plt.tight_layout()                        # Adjust plot parameters to give some padding

# Show the plot
plt.show()