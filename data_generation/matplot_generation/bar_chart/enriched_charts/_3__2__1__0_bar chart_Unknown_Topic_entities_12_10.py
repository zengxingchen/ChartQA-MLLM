
import matplotlib.pyplot as plt

locations = ['Paris', 'New York', 'Tokyo', 'Sydney', 'Berlin', 'London', 'Moscow', 'Rio de Janeiro', 'Toronto', 'Rome', 'Dubai', 'Beijing', 'Mumbai', 'Bangkok', 'Seoul', 'Buenos Aires', 'Cape Town', 'Istanbul', 'Singapore', 'Los Angeles', 'San Francisco', 'Hong Kong', 'Melbourne', 'Amsterdam']
sales = [150, 120, 130, 100, 110, 140, 115, 125, 135, 145, 105, 160, 170, 95, 155, 85, 75, 165, 180, 190, 200, 175, 185, 115]
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33', '#FF8C33', '#33FFA6', '#FF9933', '#3399FF', '#9933FF', '#FF3399', '#33FF99', '#99FF33', '#FF33F6', '#FF3366', '#33FF66', '#66FF33', '#FF6699', '#6699FF']

plt.figure(figsize=(12, 10))
plt.bar(locations, sales, color=colors, width=0.6)
plt.ylabel('Sales (thousands)')
plt.title('Sales by City')
plt.ylim(0, max(sales) + 20)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=90)
plt.show()