
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Day': 'Monday', 'Weekly Sales ($)': 1200, 'Average Temperature (°F)': 68},
    {'Day': 'Tuesday', 'Weekly Sales ($)': 1500, 'Average Temperature (°F)': 72},
    {'Day': 'Wednesday', 'Weekly Sales ($)': 1100, 'Average Temperature (°F)': 67},
    {'Day': 'Thursday', 'Weekly Sales ($)': 1700, 'Average Temperature (°F)': 76},
    {'Day': 'Friday', 'Weekly Sales ($)': 1800, 'Average Temperature (°F)': 74}
]

# Extracting the data for plotting
days = [d['Day'] for d in data]
sales = [d['Weekly Sales ($)'] for d in data]
temperatures = [d['Average Temperature (°F)'] for d in data]

# Create a scatterplot
plt.figure(figsize=(10, 6))

# Using the sales ($) value for coloring and the temperature for marker size.
# Multiply by a factor to make size differences more visible.
scatter = plt.scatter(days, sales, c=temperatures, s=[t*20 for t in temperatures], cmap="coolwarm", alpha=0.6, edgecolors='w', linewidth=1)

# Adding titles and labels
plt.title('Weekly Sales vs Day of the Week with Temperature Encoding')
plt.xlabel('Day of the Week')
plt.ylabel('Weekly Sales ($)')

# Create a colorbar for the temperature
cbar = plt.colorbar(scatter)
cbar.set_label('Average Temperature (°F)')

# Show the plot
plt.show()