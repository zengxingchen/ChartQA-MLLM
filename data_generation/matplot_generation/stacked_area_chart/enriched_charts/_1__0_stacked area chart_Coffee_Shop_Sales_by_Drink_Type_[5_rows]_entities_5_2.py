
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2024))
books = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
movies = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
music = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
video_games = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]

# Creating a stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, books, movies, music, video_games, colors=['#8B4513', '#4682B4', '#32CD32', '#800080'])

# Adding labels and title
plt.title('Entertainment Consumption Trends (2010-2023)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Consumption (Hours per Week)', fontsize=14)

# Adding a legend
plt.legend(['Books', 'Movies', 'Music', 'Video Games'], loc='upper left')

# Annotating the last data point for Video Games
plt.annotate(f'{video_games[-1]} Hours/Week',
             (years[-1], sum([books[-1], movies[-1], music[-1], video_games[-1]])),
             textcoords="offset points",
             xytext=(0,10),
             ha='center',
             fontsize=12,
             color='#800080')

plt.show()