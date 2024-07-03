
import matplotlib.pyplot as plt

genres = ['Action', 'Adventure', 'Strategy', 'Sports', 'Role-Playing', 'Simulation', 'Puzzle']
sales = [30, 20, 15, 10, 12, 8, 5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFBD33', '#33FFF6', '#DA33FF']

plt.figure(figsize=(12, 8))
plt.pie(sales, labels=genres, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})

plt.title('Popular Video Game Genres by Sales in 2023', pad=30)
plt.axis('equal')

plt.show()