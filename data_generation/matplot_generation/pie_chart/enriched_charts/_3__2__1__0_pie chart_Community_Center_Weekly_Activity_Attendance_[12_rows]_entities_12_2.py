
import matplotlib.pyplot as plt

categories = ['Classical', 'Rock', 'Jazz', 'Hip-Hop', 'Electronic', 'Country', 'Pop']
percentages = [20, 25, 15, 10, 10, 10, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffccff']

fig, ax = plt.subplots(figsize=(12, 8))
ax.pie(percentages, labels=categories, autopct='%1.1f%%', colors=colors, startangle=90)
ax.set_title('Distribution of Music Genres', pad=20)

plt.show()