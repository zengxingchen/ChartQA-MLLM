
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Streaming Services': 600, 'Books': 450, 'Video Games': 500, 'Movies': 540, 'Concerts': 700},
    {'Month': 'February', 'Streaming Services': 590, 'Books': 460, 'Video Games': 480, 'Movies': 530, 'Concerts': 680},
    {'Month': 'March', 'Streaming Services': 580, 'Books': 470, 'Video Games': 470, 'Movies': 520, 'Concerts': 660},
    {'Month': 'April', 'Streaming Services': 570, 'Books': 480, 'Video Games': 460, 'Movies': 510, 'Concerts': 640},
    {'Month': 'May', 'Streaming Services': 560, 'Books': 490, 'Video Games': 450, 'Movies': 500, 'Concerts': 620},
    {'Month': 'June', 'Streaming Services': 550, 'Books': 500, 'Video Games': 440, 'Movies': 490, 'Concerts': 600},
    {'Month': 'July', 'Streaming Services': 540, 'Books': 510, 'Video Games': 430, 'Movies': 480, 'Concerts': 580},
    {'Month': 'August', 'Streaming Services': 530, 'Books': 520, 'Video Games': 420, 'Movies': 470, 'Concerts': 560},
    {'Month': 'September', 'Streaming Services': 520, 'Books': 530, 'Video Games': 410, 'Movies': 460, 'Concerts': 540},
    {'Month': 'October', 'Streaming Services': 510, 'Books': 540, 'Video Games': 400, 'Movies': 450, 'Concerts': 520},
    {'Month': 'November', 'Streaming Services': 500, 'Books': 550, 'Video Games': 390, 'Movies': 440, 'Concerts': 500},
    {'Month': 'December', 'Streaming Services': 490, 'Books': 560, 'Video Games': 380, 'Movies': 430, 'Concerts': 480}
]

months = [record['Month'] for record in data]
streaming_services = [record['Streaming Services'] for record in data]
books = [record['Books'] for record in data]
video_games = [record['Video Games'] for record in data]
movies = [record['Movies'] for record in data]
concerts = [record['Concerts'] for record in data]

plt.figure(figsize=(20, 14))

plt.plot(months, streaming_services, label='Streaming Services', marker='o', linestyle='-', color='#1f77b4')
plt.plot(months, books, label='Books', marker='X', linestyle='--', color='#ff7f0e')
plt.plot(months, video_games, label='Video Games', marker='^', linestyle='-.', color='#2ca02c')
plt.plot(months, movies, label='Movies', marker='s', linestyle=':', color='#d62728')
plt.plot(months, concerts, label='Concerts', marker='D', linestyle='-', color='#9467bd')

plt.title('Monthly Cultural Participation', pad=20, fontsize=16)
plt.xlabel('Month')
plt.ylabel('Number of Participants')
plt.gca().invert_yaxis()
plt.legend(loc='lower left')

plt.annotate('Peak in Streaming Services', xy=('January', 600), xytext=('March', 700),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()

plt.show()