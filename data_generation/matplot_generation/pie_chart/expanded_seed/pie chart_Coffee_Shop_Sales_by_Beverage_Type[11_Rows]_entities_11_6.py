
import matplotlib.pyplot as plt

# Provided data for the pie chart
data = [
    {'Beverage Type': 'Espresso', 'Percentage of Sales': 18},
    {'Beverage Type': 'Americano', 'Percentage of Sales': 15},
    {'Beverage Type': 'Latte', 'Percentage of Sales': 20},
    {'Beverage Type': 'Cappuccino', 'Percentage of Sales': 14},
    {'Beverage Type': 'Mocha', 'Percentage of Sales': 10},
    {'Beverage Type': 'Iced Coffee', 'Percentage of Sales': 9},
    {'Beverage Type': 'Cold Brew', 'Percentage of Sales': 5},
    {'Beverage Type': 'Tea', 'Percentage of Sales': 2},
    {'Beverage Type': 'Hot Chocolate', 'Percentage of Sales': 4},
    {'Beverage Type': 'Smoothie', 'Percentage of Sales': 2},
    {'Beverage Type': 'Water and Other', 'Percentage of Sales': 1}
]

# Extracting the categories and corresponding percentages
categories = [x['Beverage Type'] for x in data]
percentages = [x['Percentage of Sales'] for x in data]

# Choosing a color palette for the pie chart
colors = plt.cm.Paired(range(len(categories)))

# Using explode to separate the biggest category, Latte in this case
explode = [0 if x < max(percentages) else 0.1 for x in percentages]

# Create a pie chart
plt.figure(figsize=(10, 8))  # Making the figure larger for readability
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)

# Adding title
plt.title('Sales Percentage by Beverage Type')

# Display the legend outside the pie chart
plt.legend(categories, title='Beverage Types', loc='center left', bbox_to_anchor=(1, 0.5))

# Show the plot
plt.tight_layout()
plt.show()