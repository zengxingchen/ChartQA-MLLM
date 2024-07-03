
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2018', '2019', '2020', '2021', '2022', '2023']
book_sales = [30, 25, 20, 15, 10, 5]
music_sales = [40, 35, 25, 30, 20, 15]
movie_sales = [30, 40, 55, 55, 70, 80]

# Width and height of the chart
fig, ax = plt.subplots(figsize=(10, 7))

# Stacked bar chart
bar_width = 0.5
r = np.arange(len(categories))

p1 = plt.barh(r, book_sales, color='#ff9999', edgecolor='white', height=bar_width)
p2 = plt.barh(r, music_sales, left=book_sales, color='#66b3ff', edgecolor='white', height=bar_width)
p3 = plt.barh(r, movie_sales, left=np.array(book_sales) + np.array(music_sales), color='#99ff99', edgecolor='white', height=bar_width)

# Customizing the axes and title
plt.xlabel('Sales Percentage')
plt.ylabel('Year')
plt.title('Entertainment Sales Distribution Over Years', loc='center')
plt.yticks(r, categories)
plt.legend(['Book Sales', 'Music Sales', 'Movie Sales'], loc='lower right', bbox_to_anchor=(1, 0.5))

# Display the plot
plt.tight_layout()
plt.show()