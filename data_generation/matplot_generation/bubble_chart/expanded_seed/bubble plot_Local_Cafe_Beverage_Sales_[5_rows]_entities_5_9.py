
import matplotlib.pyplot as plt

# The data provided
data = [
    {'Day': 'Monday', 'Beverage': 'Coffee', 'Units Sold': 75, 'Revenue ($)': 225, 'Average Preparation Time (sec)': 60},
    {'Day': 'Tuesday', 'Beverage': 'Latte', 'Units Sold': 50, 'Revenue ($)': 200, 'Average Preparation Time (sec)': 90},
    {'Day': 'Wednesday', 'Beverage': 'Espresso', 'Units Sold': 60, 'Revenue ($)': 180, 'Average Preparation Time (sec)': 45},
    {'Day': 'Thursday', 'Beverage': 'Cappuccino', 'Units Sold': 40, 'Revenue ($)': 160, 'Average Preparation Time (sec)': 80},
    {'Day': 'Friday', 'Beverage': 'Tea', 'Units Sold': 30, 'Revenue ($)': 90, 'Average Preparation Time (sec)': 30}
]

# Unpacking the data into variables
days = [entry['Day'] for entry in data]
units_sold = [entry['Units Sold'] for entry in data]
revenue = [entry['Revenue ($)'] for entry in data]
prep_time = [entry['Average Preparation Time (sec)'] for entry in data]

# Set up the figure
plt.figure(figsize=(10, 6))

# Create the bubble chart
bubble_sizes = [revenue_value / max(revenue) * 1000 for revenue_value in revenue]  # Normalize for bubble size
scatter = plt.scatter(days, units_sold, s=bubble_sizes, c=prep_time, alpha=0.5, cmap='viridis')

# Create a colorbar
plt.colorbar(scatter, label='Average Preparation Time (sec)')

# Set the title and labels
plt.title('Beverage Sales: Units Sold and Revenue per Day with Prep Time')
plt.xlabel('Day of the Week')
plt.ylabel('Units Sold')

# Add text inside bubbles for revenue
for i, revenue_value in enumerate(revenue):
    plt.annotate(f'${revenue_value}', (days[i], units_sold[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()