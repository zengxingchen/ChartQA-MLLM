
import matplotlib.pyplot as plt

# Given data
data = [
    {'Day': 'Monday', ' Temperature (°C)': 20, ' Coffee Sales (Units)': 100},
    {'Day': 'Tuesday', ' Temperature (°C)': 24, ' Coffee Sales (Units)': 150},
    {'Day': 'Wednesday', ' Temperature (°C)': 22, ' Coffee Sales (Units)': 125},
    {'Day': 'Thursday', ' Temperature (°C)': 19, ' Coffee Sales (Units)': 95},
    {'Day': 'Friday', ' Temperature (°C)': 17, ' Coffee Sales (Units)': 80}
]

# Prepare data
days = [d['Day'] for d in data]
temperatures = [d[' Temperature (°C)'] for d in data]
coffee_sales = [d[' Coffee Sales (Units)'] for d in data]

# Determine color based on the temperature (warmer temperatures will be redder)
colors = temperatures

# Determine size based on coffee sales (larger sales result in larger points)
sizes = [sales * 3 for sales in coffee_sales]  # Scale the sales to make differences more visible

# Create scatter plot
plt.scatter(temperatures, coffee_sales, s=sizes, c=colors, cmap='coolwarm', alpha=0.6, edgecolors='w')

# Add labels for each point based on the day of the week
for i, day in enumerate(days):
    plt.text(temperatures[i], coffee_sales[i] + 5, day, ha='center', va='bottom')

# Add a color bar for reference
cbar = plt.colorbar()
cbar.set_label('Temperature (°C)')

# Add labels and title to the plot
plt.xlabel('Temperature (°C)')
plt.ylabel('Coffee Sales (Units)')
plt.title('Coffee Sales vs Temperature')

# Show the plot
plt.tight_layout()
plt.show()