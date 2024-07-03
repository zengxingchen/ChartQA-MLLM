
import matplotlib.pyplot as plt

# Define data
products = [
    "Product A", "Product B", "Product C", "Product D", "Product E", "Product F",
    "Product G", "Product H", "Product I", "Product J", "Product K", "Product L",
    "Product M", "Product N", "Product O", "Product P", "Product Q", "Product R",
    "Product S", "Product T", "Product U", "Product V", "Product W", "Product X",
    "Product Y", "Product Z"
]

price = [
    10, 15, 12, 20, 25, 30, 18, 22, 28, 35, 40, 8, 14, 16, 19, 27, 33, 11, 24, 29,
    21, 17, 23, 13, 26, 32
]

sales = [
    500, 600, 450, 700, 650, 300, 520, 480, 310, 290, 260, 570, 610, 530, 490, 320,
    280, 550, 640, 305, 470, 560, 460, 620, 630, 285
]

customer_satisfaction = [
    80, 85, 75, 90, 88, 70, 78, 83, 72, 68, 65, 82, 87, 80, 85, 73, 67, 81, 89, 71,
    84, 86, 79, 88, 90, 69
]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(16, 10))

# Bubble sizes as a fraction of sales (adjust the scaling as needed)
sizes = [sales[i] / 2 for i in range(len(sales))]

# Scatter plot (using price as weight for bubble size)
scatter = ax.scatter(
    price, customer_satisfaction, s=sizes, alpha=0.6,
    color=[
        '#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3333', '#FF33FF',
        '#57FFC8', '#FFC857', '#33FFFA', '#DD33FF', '#3FFFA5', '#A53FFF',
        '#3FA5FF', '#FFA53F', '#FF3FA5', '#FF5733', '#33FF57', '#3357FF',
        '#57FF33', '#FF3333', '#FF33FF', '#57FFC8', '#FFC857', '#33FFFA',
        '#DD33FF', '#3FFFA5'
    ]
)

# Customize the appearance
ax.set_title('Product Prices, Sales, and Customer Satisfaction', pad=20)
ax.set_xlabel('Price')
ax.set_ylabel('Customer Satisfaction (%)')
ax.grid(True)

# Adding the names of the products to the bubbles
for i, txt in enumerate(products):
    ax.annotate(txt, (price[i], customer_satisfaction[i]))

plt.show()