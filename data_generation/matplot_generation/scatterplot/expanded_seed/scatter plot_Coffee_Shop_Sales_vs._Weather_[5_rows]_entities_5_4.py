
import matplotlib.pyplot as plt

# Given data in the form of a list of dictionaries
data = [
    {'Day': 'Monday', 'Temperature (°C)': 20, 'Coffee Sales ($)': 250},
    {'Day': 'Tuesday', 'Temperature (°C)': 22, 'Coffee Sales ($)': 260},
    {'Day': 'Wednesday', 'Temperature (°C)': 18, 'Coffee Sales ($)': 240},
    {'Day': 'Thursday', 'Temperature (°C)': 21, 'Coffee Sales ($)': 255},
    {'Day': 'Friday', 'Temperature (°C)': 19, 'Coffee Sales ($)': 235}
]

# Extracting the Temperature, Coffee Sales, and Days for plotting
temperatures = [item['Temperature (°C)'] for item in data]
coffee_sales = [item['Coffee Sales ($)'] for item in data]
days = [item['Day'] for item in data]
day_numbers = range(len(days))  # Convert days to numerical values

# Start by creating a scatter plot
plt.figure(figsize=(10, 6))  # Set the size of the figure

# Create a scatterplot, with temperature being the x-axis and coffee sales being the y-axis.
# We will also use the day of the week to determine the color of the points.
colors = ['blue', 'green', 'red', 'cyan', 'magenta']  # Color list corresponding to each day
sizes = [sales / 5 for sales in coffee_sales]  # Compute size of each point based on coffee sales to diversify the encoding

# Scatter plot with Temperature on x-axis and Coffee Sales on y-axis. Day of week is represented by color.
plt.scatter(temperatures, coffee_sales, c=colors, s=sizes, alpha=0.5)

# Labeling each data point with the corresponding day of the week
for i, day in enumerate(days):
    plt.text(temperatures[i], coffee_sales[i], day, fontsize=9, ha='center')

# Adding titles and labels
plt.title("Coffee Sales in Relation to Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Coffee Sales ($)")

# Adding grid lines for better readability
plt.grid(True)

# Showing a legend to explain the colors/sizes, here we'll use a proxy artist for the legend
import matplotlib.patches as mpatches
legend_handles = [mpatches.Patch(color=colors[i], label=days[i]) for i in range(len(days))]
plt.legend(handles=legend_handles, title='Day of Week')

# Show the plot
plt.show()