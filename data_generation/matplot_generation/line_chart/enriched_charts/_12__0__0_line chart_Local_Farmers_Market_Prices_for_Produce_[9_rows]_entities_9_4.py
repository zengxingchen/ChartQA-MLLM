
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
new_book_releases = [400, 420, 390, 450, 470, 460, 480, 510, 500, 520, 540, 530, 550, 580]

# Create figure and plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

# Change the color scheme using specific hex codes
ax.plot(years, new_book_releases, color='#ff5733', marker='o')  # Example color code and marker for each point

# Set the title and labels
ax.set_title('Annual New Book Releases', fontsize=18, pad=20)  # Change the topic and headline of the chart
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Books', fontsize=14)

# Adding annotations/labels
for (year, n_books) in zip(years, new_book_releases):
    ax.annotate(f'{n_books}', xy=(year, n_books), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)  # Adding grid
plt.show()