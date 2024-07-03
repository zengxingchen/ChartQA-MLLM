
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Beverage': 'Espresso', 'Daily Sales (USD)': 950},
    {'Beverage': 'Latte', 'Daily Sales (USD)': 1100},
    {'Beverage': 'Cappuccino', 'Daily Sales (USD)': 780},
    {'Beverage': 'Americano', 'Daily Sales (USD)': 640},
    {'Beverage': 'Mocha', 'Daily Sales (USD)': 550}
]

# Extracting 'Beverage' and 'Daily Sales (USD)' values
beverages = [item['Beverage'] for item in data]
sales = [item['Daily Sales (USD)'] for item in data]

# Creating a bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure size

# Creating the bars with differentiated colors and a pattern
colors = ['blue', 'green', 'red', 'cyan', 'magenta']
patterns = ['/', '\\', '|', '-', '+']

bars = ax.bar(beverages, sales, color=colors, edgecolor='black')

# Adding patterns to the bars
for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

# Adding labels and title
ax.set_xlabel('Beverage', fontsize=12)
ax.set_ylabel('Daily Sales (USD)', fontsize=12)
ax.set_title('Daily Sales by Beverage', fontsize=16)

# Adding a grid
ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
ax.set_axisbelow(True)

# Annotating the bar chart with the sales values
for i, rect in enumerate(bars):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., 1.005*height,
            f'${sales[i]}', ha='center', va='bottom')

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Showing the plot
plt.tight_layout()
plt.show()