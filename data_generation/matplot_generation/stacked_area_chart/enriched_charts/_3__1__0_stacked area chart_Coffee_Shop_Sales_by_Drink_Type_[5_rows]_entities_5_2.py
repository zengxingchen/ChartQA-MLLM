
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2024))
books = [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56]
movies = [70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96]
music = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66]
video_games = [60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86]

# Creating a stacked area chart
plt.figure(figsize=(16, 9))
plt.stackplot(years, books, movies, music, video_games, colors=['#FF6347', '#1E90FF', '#32CD32', '#FFD700'])

# Adding labels and title
plt.title('Leisure Activity Trends (2010-2023)', fontsize=18, pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Hours per Week', fontsize=14)

# Adding a legend
plt.legend(['Books', 'Movies', 'Music', 'Video Games'], loc='upper left')

# Annotating the last data point for Movies
plt.annotate(f'{movies[-1]} Hours/Week',
             (years[-1], sum([books[-1], movies[-1], music[-1], video_games[-1]])),
             textcoords="offset points",
             xytext=(0,10),
             ha='center',
             fontsize=12,
             color='#1E90FF')

plt.show()