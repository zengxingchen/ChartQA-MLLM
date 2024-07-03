
import matplotlib.pyplot as plt

# Data
movies = [
    "Avatar", "Avengers: Endgame", "Titanic", "Star Wars: The Force Awakens",
    "Avengers: Infinity War", "Jurassic World", "The Lion King", "The Avengers",
    "Furious 7", "Frozen II", "Avengers: Age of Ultron", "Black Panther",
    "Harry Potter and the Deathly Hallows: Part 2", "Star Wars: The Last Jedi",
    "Jurassic World: Fallen Kingdom", "Frozen", "Beauty and the Beast",
    "Incredibles 2", "The Fate of the Furious", "Iron Man 3"
]
release_years = [2009, 2019, 1997, 2015, 2018, 2015, 2019, 2012, 2015, 2019, 2015, 2018, 2011, 2017, 2018, 2013, 2017, 2018, 2017, 2013]
box_office_grosses = [2920, 2797, 2187, 2068, 2048, 1671, 1663, 1518, 1516, 1450, 1405, 1347, 1342, 1332, 1309, 1290, 1263, 1243, 1236, 1215]

# Scatter plot
fig, ax = plt.subplots(figsize=(18, 10))  # Change the width and height of the chart
scatter = ax.scatter(
    release_years,
    box_office_grosses,
    alpha=0.8,
    c=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF',
        '#FFC300', '#DAF7A6', '#FF33F6', '#33FFF0', '#A6FF33',
        '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300',
        '#DAF7A6', '#FF33F6', '#33FFF0', '#A6FF33', '#FF5733'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Top Grossing Movies: Release Year vs Box Office Gross', pad=20)
ax.set_xlabel('Release Year')
ax.set_ylabel('Box Office Gross (in millions)')

# Adding the movie names as labels next to each point
for i, movie in enumerate(movies):
    ax.annotate(movie, (release_years[i], box_office_grosses[i]), fontsize=8, ha='right')

plt.show()