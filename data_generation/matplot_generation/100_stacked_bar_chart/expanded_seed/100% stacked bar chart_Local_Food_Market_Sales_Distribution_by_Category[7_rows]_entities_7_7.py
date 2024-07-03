
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Month': 'January', 'Fruits': '25%', 'Vegetables': '30%', 'Meat': '15%', 'Dairy': '10%', 'Bakery': '10%', 'Seafood': '10%'},
    {'Month': 'February', 'Fruits': '22%', 'Vegetables': '28%', 'Meat': '17%', 'Dairy': '11%', 'Bakery': '12%', 'Seafood': '10%'},
    {'Month': 'March', 'Fruits': '20%', 'Vegetables': '29%', 'Meat': '18%', 'Dairy': '12%', 'Bakery': '10%', 'Seafood': '11%'},
    {'Month': 'April', 'Fruits': '23%', 'Vegetables': '26%', 'Meat': '17%', 'Dairy': '12%', 'Bakery': '12%', 'Seafood': '10%'},
    {'Month': 'May', 'Fruits': '25%', 'Vegetables': '25%', 'Meat': '15%', 'Dairy': '15%', 'Bakery': '10%', 'Seafood': '10%'},
    {'Month': 'June', 'Fruits': '27%', 'Vegetables': '23%', 'Meat': '13%', 'Dairy': '17%', 'Bakery': '10%', 'Seafood': '10%'},
    {'Month': 'July', 'Fruits': '30%', 'Vegetables': '20%', 'Meat': '12%', 'Dairy': '18%', 'Bakery': '10%', 'Seafood': '10%'}
]

# Convert percentage strings to float
for month_data in data:
    for key in month_data:
        if key != 'Month':
            month_data[key] = float(month_data[key].rstrip('%'))

# Extract categories and values for each month
categories = list(data[0].keys())[1:]  # Skip the 'Month' key
months = [month_data['Month'] for month_data in data]
values_by_category = {category: [month_data[category] for month_data in data] for category in categories}

# Plotting the 100% stacked bar chart
bottoms = [0] * len(data)  # Initialize bottom values for the stacking
fig, ax = plt.subplots()

# Use diverse colors to differentiate the categories
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
for category, color in zip(categories, colors):
    ax.bar(months, values_by_category[category], label=category, color=color, bottom=bottoms)
    # Update bottoms for the next stack
    bottoms = [bottoms[i] + values_by_category[category][i] for i in range(len(data))]

# Adding labels and title
plt.ylabel('Percentage (%)')
plt.xlabel('Month')
plt.title('Monthly Consumption by Category (100% Stacked Bar Chart)')
plt.legend()

# Display the figure.
plt.show()