
import matplotlib.pyplot as plt

genres = ['Classical', 'Jazz', 'Rock', 'Pop', 'Hip-Hop', 'Country', 'Electronic']
sales = [25, 20, 18, 15, 10, 8, 4]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFBD33', '#33FFF6', '#DA33FF']

plt.figure(figsize=(10, 7))
plt.pie(sales, labels=genres, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})

plt.title('Popular Music Genres by Sales in 2023', pad=30)
plt.axis('equal')

plt.show()