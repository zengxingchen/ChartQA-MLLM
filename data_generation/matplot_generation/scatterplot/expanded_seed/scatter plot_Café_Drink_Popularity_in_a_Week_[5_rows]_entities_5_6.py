
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Day': 'Monday', 'Latte Sales': 95, 'Cappuccino Sales': 78, 'Espresso Sales': 89},
    {'Day': 'Tuesday', 'Latte Sales': 123, 'Cappuccino Sales': 94, 'Espresso Sales': 107},
    {'Day': 'Wednesday', 'Latte Sales': 135, 'Cappuccino Sales': 112, 'Espresso Sales': 120},
    {'Day': 'Thursday', 'Latte Sales': 150, 'Cappuccino Sales': 130, 'Espresso Sales': 140},
    {'Day': 'Friday', 'Latte Sales': 180, 'Cappuccino Sales': 150, 'Espresso Sales': 160}
]

# Extracting data for the plot
days = [d['Day'] for d in data]
latte_sales = [d['Latte Sales'] for d in data]
cappuccino_sales = [d['Cappuccino Sales'] for d in data]
espresso_sales = [d['Espresso Sales'] for d in data]

# Convert days to numerical values for plotting
day_numbers = range(len(days))

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Set the figure size

# Scatter plot for Latte Sales
plt.scatter(day_numbers, latte_sales, color='blue', label='Latte Sales', marker='o', s=100)  # 's' sets the marker size

# Scatter plot for Cappuccino Sales
plt.scatter(day_numbers, cappuccino_sales, color='green', label='Cappuccino Sales', marker='s', s=100)  # Square markers

# Scatter plot for Espresso Sales
plt.scatter(day_numbers, espresso_sales, color='red', label='Espresso Sales', marker='^', s=100)  # Triangle markers

# Add titles and labels
plt.title('Coffee Sales Scatter Plot')
plt.xlabel('Day of the Week')
plt.ylabel('Sales')

# Customize the x-axis to show the days of the week
plt.xticks(day_numbers, days)

# Add grid for better readability
plt.grid(True)

# Add a legend to identify each set of points
plt.legend()

# Display the plot
plt.show()