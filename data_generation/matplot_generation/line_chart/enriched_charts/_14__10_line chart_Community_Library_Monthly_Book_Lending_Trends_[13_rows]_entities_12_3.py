
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Comedies': 500, 'Action Movies': 700, 'Documentaries': 200, 'Romantic Movies': 400, 'Horror Movies': 600},
    {'Month': 'February', 'Comedies': 480, 'Action Movies': 680, 'Documentaries': 220, 'Romantic Movies': 420, 'Horror Movies': 580},
    {'Month': 'March', 'Comedies': 460, 'Action Movies': 660, 'Documentaries': 240, 'Romantic Movies': 440, 'Horror Movies': 560},
    {'Month': 'April', 'Comedies': 440, 'Action Movies': 640, 'Documentaries': 260, 'Romantic Movies': 460, 'Horror Movies': 540},
    {'Month': 'May', 'Comedies': 420, 'Action Movies': 620, 'Documentaries': 280, 'Romantic Movies': 480, 'Horror Movies': 520},
    {'Month': 'June', 'Comedies': 400, 'Action Movies': 600, 'Documentaries': 300, 'Romantic Movies': 500, 'Horror Movies': 500},
    {'Month': 'July', 'Comedies': 380, 'Action Movies': 580, 'Documentaries': 320, 'Romantic Movies': 520, 'Horror Movies': 480},
    {'Month': 'August', 'Comedies': 360, 'Action Movies': 560, 'Documentaries': 340, 'Romantic Movies': 540, 'Horror Movies': 460},
    {'Month': 'September', 'Comedies': 340, 'Action Movies': 540, 'Documentaries': 360, 'Romantic Movies': 560, 'Horror Movies': 440},
    {'Month': 'October', 'Comedies': 320, 'Action Movies': 520, 'Documentaries': 380, 'Romantic Movies': 580, 'Horror Movies': 420},
    {'Month': 'November', 'Comedies': 300, 'Action Movies': 500, 'Documentaries': 400, 'Romantic Movies': 600, 'Horror Movies': 400},
    {'Month': 'December', 'Comedies': 280, 'Action Movies': 480, 'Documentaries': 420, 'Romantic Movies': 620, 'Horror Movies': 380}
]

months = [entry['Month'] for entry in data]
comedies = [entry['Comedies'] for entry in data]
action_movies = [entry['Action Movies'] for entry in data]
documentaries = [entry['Documentaries'] for entry in data]
romantic_movies = [entry['Romantic Movies'] for entry in data]
horror_movies = [entry['Horror Movies'] for entry in data]

plt.figure(figsize=(14, 7))
plt.plot(months, comedies, marker='o', linestyle='-', color='#e6194b', label='Comedies')
plt.plot(months, action_movies, marker='s', linestyle='--', color='#3cb44b', label='Action Movies')
plt.plot(months, documentaries, marker='^', linestyle='-.', color='#ffe119', label='Documentaries')
plt.plot(months, romantic_movies, marker='x', linestyle=':', color='#4363d8', label='Romantic Movies')
plt.plot(months, horror_movies, marker='d', linestyle='-', color='#f58231', label='Horror Movies')

plt.title('Entertainment & Leisure: Monthly Movie Viewership Trends', pad=20)
plt.xlabel('Month')
plt.ylabel('Viewership (Units)')
plt.xticks(rotation=45)
plt.legend(loc='lower left')
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()