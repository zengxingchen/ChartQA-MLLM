
import matplotlib.pyplot as plt

locations = ['Paris', 'New York', 'Tokyo', 'Sydney', 'Berlin', 'London', 'Moscow', 'Rio de Janeiro', 'Toronto', 'Rome', 'Dubai', 'Beijing']
sales = [150, 120, 130, 100, 110, 140, 115, 125, 135, 145, 105, 160]
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33', '#FF8C33', '#33FFA6']

plt.figure(figsize=(10, 8))
plt.barh(locations, sales, color=colors, height=0.5)
plt.xlabel('Sales (thousands)')
plt.title('Sales by City')
plt.xlim(0, max(sales) + 20)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()