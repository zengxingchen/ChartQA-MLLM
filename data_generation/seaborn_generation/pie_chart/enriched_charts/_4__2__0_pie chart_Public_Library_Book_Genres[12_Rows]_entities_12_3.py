
import matplotlib.pyplot as plt

cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian', 'French', 'Other']
popularity = [30, 25, 20, 15, 5, 5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF5']

plt.figure(figsize=(12, 8))
plt.pie(popularity, labels=cuisines, autopct='%1.1f%%', colors=colors, startangle=90)

plt.title('Popularity of Various Cuisines in 2023', pad=20)
plt.axis('equal')

plt.show()