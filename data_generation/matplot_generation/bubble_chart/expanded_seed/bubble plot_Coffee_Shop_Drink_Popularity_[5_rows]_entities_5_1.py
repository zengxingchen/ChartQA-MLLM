
import matplotlib.pyplot as plt

# Create a list of dictionaries with the provided data
data = [
    {'Drink': 'Latte', 'Average_Price': 3.5, 'Customer_Rating (out of 5)': 4.2, 'Number_of_Sales_per_Day': 90},
    {'Drink': 'Cappuccino', 'Average_Price': 3.2, 'Customer_Rating (out of 5)': 4.0, 'Number_of_Sales_per_Day': 70},
    {'Drink': 'Americano', 'Average_Price': 2.8, 'Customer_Rating (out of 5)': 4.3, 'Number_of_Sales_per_Day': 50},
    {'Drink': 'Espresso', 'Average_Price': 2.5, 'Customer_Rating (out of 5)': 4.5, 'Number_of_Sales_per_Day': 60},
    {'Drink': 'Iced Coffee', 'Average_Price': 3.0, 'Customer_Rating (out of 5)': 4.1, 'Number_of_Sales_per_Day': 80}
]

# Seperate the data into lists for plotting
x = [drink['Drink'] for drink in data]
y = [drink['Customer_Rating (out of 5)'] for drink in data]
sizes = [drink['Number_of_Sales_per_Day'] * 10 for drink in data]  # Scale number of sales for bubble size
colors = [drink['Average_Price'] for drink in data]  # Use average price for color

# Create the bubble chart
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')

# Title and labels
plt.title('Shop Drink Data (Bubble Chart)')
plt.xlabel('Drink')
plt.ylabel('Customer Rating (out of 5)')

# Color bar for the average prices
cbar = plt.colorbar()
cbar.set_label('Average Price ($)')

# Adjust the x-axis to show drink names clearly
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()