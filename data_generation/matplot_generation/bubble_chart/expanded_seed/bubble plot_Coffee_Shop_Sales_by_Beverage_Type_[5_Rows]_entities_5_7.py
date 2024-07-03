
import matplotlib.pyplot as plt

# Data
data = [
    {'Beverage Type': 'Coffee', 'Average Sales per Day ($)': 1200, 'Average Cup Size (oz)': 12, 'Customer Satisfaction (1-5 scale)': 4.3},
    {'Beverage Type': 'Tea', 'Average Sales per Day ($)': 800, 'Average Cup Size (oz)': 10, 'Customer Satisfaction (1-5 scale)': 4.1},
    {'Beverage Type': 'Smoothie', 'Average Sales per Day ($)': 500, 'Average Cup Size (oz)': 16, 'Customer Satisfaction (1-5 scale)': 4.5},
    {'Beverage Type': 'Espresso', 'Average Sales per Day ($)': 300, 'Average Cup Size (oz)': 2, 'Customer Satisfaction (1-5 scale)': 4.8},
    {'Beverage Type': 'Hot Chocolate', 'Average Sales per Day ($)': 400, 'Average Cup Size (oz)': 12, 'Customer Satisfaction (1-5 scale)': 4.2}
]

# Extracting data
beverage_types = [item['Beverage Type'] for item in data]
sales_per_day = [item['Average Sales per Day ($)'] for item in data]
cup_sizes = [item['Average Cup Size (oz)'] for item in data]
customer_satisfaction = [item['Customer Satisfaction (1-5 scale)'] for item in data]

# Normalize the customer satisfaction scores to control bubble sizes
bubble_sizes = [(score * 100) for score in customer_satisfaction]  # Multiply by a factor to get a visible bubble size

# Color mapping for each beverage
colors = {'Coffee': 'brown', 'Tea': 'green', 'Smoothie': 'magenta', 'Espresso': 'black', 'Hot Chocolate': 'chocolate'}
beverage_colors = [colors[beverage] for beverage in beverage_types]

# Creating the bubble chart
plt.figure(figsize=(10, 6))
bubble = plt.scatter(sales_per_day, cup_sizes, s=bubble_sizes, c=beverage_colors, alpha=0.6, edgecolors='w', linewidth=1)

# Adding title and labels
plt.title('Beverage Sales, Cup Size, and Customer Satisfaction')
plt.xlabel('Average Sales per Day ($)')
plt.ylabel('Average Cup Size (oz)')

# Adding legend
for beverage in colors:
    plt.scatter([], [], c=colors[beverage], alpha=0.6, s=100, label=beverage)
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Beverage Type')

# Annotate each bubble with the Beverage Type
for i, txt in enumerate(beverage_types):
    plt.annotate(txt, (sales_per_day[i], cup_sizes[i]), ha='center', va='center')

# Show the plot
plt.tight_layout()
plt.show()