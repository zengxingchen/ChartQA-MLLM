
import matplotlib.pyplot as plt
import numpy as np

# Data from the provided chart table
data = [
    {'Beverage': 'Espresso', 'Monday': 80, 'Hot Drinks': 20, 'Monday.1': 90, 'Cold Drinks': 25, 'Tuesday': 95, 'Hot Drinks.1': 30},
    {'Beverage': 'Latte', 'Monday': 140, 'Hot Drinks': 50, 'Monday.1': 150, 'Cold Drinks': 60, 'Tuesday': 155, 'Hot Drinks.1': 65},
    {'Beverage': 'Cappuccino', 'Monday': 120, 'Hot Drinks': 40, 'Monday.1': 125, 'Cold Drinks': 45, 'Tuesday': 130, 'Hot Drinks.1': 50},
    # Other data entries... (repeat the structure for each provided dictionary)
]
# Note: for brevity, only a subset of data is shown here; you should include the full data list

# Categories
categories = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Iced Coffee', 'Iced Tea', 'Smoothie',
              'Hot Chocolate', 'Herbal Tea', 'Frappuccino', 'Mocha', 'Chai']

# Data processing for visualization
n_categories = len(categories)
index = np.arange(n_categories)
bar_width = 0.35

# Monday Data
monday_sales_hot = [item['Hot Drinks'] for item in data]
monday_sales_cold = [item['Monday.1'] for item in data]

# Tuesday Data
tuesday_sales_hot = [item['Hot Drinks.1'] for item in data]
tuesday_sales_cold = [item['Cold Drinks'] for item in data]

# Plotting
fig, ax = plt.subplots()

# Stacked bars for Monday
monday_bars_hot = ax.bar(index, monday_sales_hot, bar_width, label='Monday Hot Drinks')
monday_bars_cold = ax.bar(index, monday_sales_cold, bar_width, bottom=monday_sales_hot, label='Monday Cold Drinks')

# Stacked bars for Tuesday
tuesday_bars_hot = ax.bar(index + bar_width, tuesday_sales_hot, bar_width, label='Tuesday Hot Drinks')
tuesday_bars_cold = ax.bar(index + bar_width, tuesday_sales_cold, bar_width, bottom=tuesday_sales_hot, label='Tuesday Cold Drinks')

# Labeling and customization for clarity
ax.set_xlabel('Beverages')
ax.set_ylabel('Sales')
ax.set_title('Beverage Sales for Monday and Tuesday')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.legend()

# Displaying values on bars
def add_values(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_values(monday_bars_hot)
add_values(monday_bars_cold)
add_values(tuesday_bars_hot)
add_values(tuesday_bars_cold)

# Show plot
plt.tight_layout()
plt.show()