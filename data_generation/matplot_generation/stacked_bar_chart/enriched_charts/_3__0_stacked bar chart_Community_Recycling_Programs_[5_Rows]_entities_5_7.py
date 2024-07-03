
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
children_books = [25000, 27000, 29000, 31000, 33500, 35000, 37000]
young_adult = [18000, 19000, 20500, 22000, 23500, 24500, 26000]
adult_fiction = [32000, 33000, 34500, 36000, 37500, 39000, 41000]
adult_non_fiction = [21000, 22500, 24000, 26000, 28000, 30000, 32000]

# Bottom data for stacking
adult_fiction_bottom = [i + j for i, j in zip(children_books, young_adult)]
young_adult_bottom = children_books

# Figure and Axes
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart

# Stacked Vertical Bars
ax.bar(years, children_books, color='#ff9999', edgecolor='white', width=0.6, label="Children's Books")  # Children's books with pink color
ax.bar(years, young_adult, bottom=young_adult_bottom, color='#66b3ff', edgecolor='white', width=0.6, label='Young Adult')  # Young adult with light blue color
ax.bar(years, adult_fiction, bottom=adult_fiction_bottom, color='#99ff99', edgecolor='white', width=0.6, label='Adult Fiction')  # Adult fiction with light green color
ax.bar(years, adult_non_fiction, bottom=[i + j + k for i, j, k in zip(children_books, young_adult, adult_fiction)], color='#ffcc99', edgecolor='white', width=0.6, label='Adult Non-Fiction')  # Adult non-fiction with light orange color

# Labels and Title
ax.set_ylabel('Number of Books Sold')
ax.set_xlabel('Year')
ax.set_title('Book Sales by Category from 2015 to 2021', pad=20)

# Numerical labels
for i in range(len(years)):
    ax.text(i, children_books[i] / 2, f'{children_books[i]}', ha='center', va='center', color='black')
    ax.text(i, young_adult_bottom[i] + young_adult[i] / 2, f'{young_adult[i]}', ha='center', va='center', color='black')
    ax.text(i, adult_fiction_bottom[i] + adult_fiction[i] / 2, f'{adult_fiction[i]}', ha='center', va='center', color='black')
    ax.text(i, adult_fiction_bottom[i] + adult_fiction[i] + adult_non_fiction[i] / 2, f'{adult_non_fiction[i]}', ha='center', va='center', color='black')

# Display the legend
ax.legend(loc='upper left')

# Display the plot
plt.show()