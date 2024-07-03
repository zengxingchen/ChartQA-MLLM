
import matplotlib.pyplot as plt

# Your data
data = [
    {'Week': 'Week 1', 'Fruits': 320, 'Vegetables': 450, 'Dairy': 230, 'Bakery Goods': 180, 'Honey': 45, 'Jams': 60},
    {'Week': 'Week 2', 'Fruits': 310, 'Vegetables': 425, 'Dairy': 240, 'Bakery Goods': 190, 'Honey': 50, 'Jams': 65},
    # ... (other data points)
    {'Week': 'Week 12', 'Fruits': 400, 'Vegetables': 520, 'Dairy': 330, 'Bakery Goods': 260, 'Honey': 95, 'Jams': 115}
]

# Extracting the weeks' labels
weeks = [d['Week'] for d in data]

# Extracting product sales data
fruits = [d['Fruits'] for d in data]
vegetables = [d['Vegetables'] for d in data]
dairy = [d['Dairy'] for d in data]
bakery_goods = [d['Bakery Goods'] for d in data]
honey = [d['Honey'] for d in data]
jams = [d['Jams'] for d in data]

# Bar chart creation
fig, ax = plt.subplots()

# Stacking each category on top of the previous one
ax.bar(weeks, fruits, label='Fruits')
ax.bar(weeks, vegetables, bottom=fruits, label='Vegetables')
ax.bar(weeks, dairy, bottom=[i+j for i, j in zip(fruits, vegetables)], label='Dairy')
ax.bar(weeks, bakery_goods, bottom=[i+j+k for i, j, k in zip(fruits, vegetables, dairy)], label='Bakery Goods')
ax.bar(weeks, honey, bottom=[i+j+k+l for i, j, k, l in zip(fruits, vegetables, dairy, bakery_goods)], label='Honey')
ax.bar(weeks, jams, bottom=[i+j+k+l+m for i, j, k, l, m in zip(fruits, vegetables, dairy, bakery_goods, honey)], label='Jams')

# Adding labels and title
plt.xlabel('Weeks')
plt.ylabel('Sales')
plt.title('Weekly Sales Data by Product Category')

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Adding a legend
plt.legend()

# Display the plotted chart
plt.tight_layout()
plt.show()