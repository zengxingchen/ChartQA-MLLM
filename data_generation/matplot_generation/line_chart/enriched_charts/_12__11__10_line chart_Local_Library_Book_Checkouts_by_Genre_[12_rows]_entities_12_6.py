
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Streaming Services': 300, 'Books': 450, 'Video Games': 200, 'Movies': 320, 'Concerts': 150},
    {'Month': 'February', 'Streaming Services': 310, 'Books': 460, 'Video Games': 210, 'Movies': 330, 'Concerts': 160},
    {'Month': 'March', 'Streaming Services': 320, 'Books': 470, 'Video Games': 220, 'Movies': 310, 'Concerts': 170},
    {'Month': 'April', 'Streaming Services': 330, 'Books': 480, 'Video Games': 230, 'Movies': 300, 'Concerts': 180},
    {'Month': 'May', 'Streaming Services': 340, 'Books': 490, 'Video Games': 240, 'Movies': 290, 'Concerts': 190},
    {'Month': 'June', 'Streaming Services': 350, 'Books': 500, 'Video Games': 250, 'Movies': 280, 'Concerts': 200},
    {'Month': 'July', 'Streaming Services': 360, 'Books': 510, 'Video Games': 260, 'Movies': 270, 'Concerts': 210},
    {'Month': 'August', 'Streaming Services': 370, 'Books': 520, 'Video Games': 270, 'Movies': 260, 'Concerts': 220},
    {'Month': 'September', 'Streaming Services': 380, 'Books': 530, 'Video Games': 280, 'Movies': 250, 'Concerts': 230},
    {'Month': 'October', 'Streaming Services': 390, 'Books': 540, 'Video Games': 290, 'Movies': 240, 'Concerts': 240},
    {'Month': 'November', 'Streaming Services': 400, 'Books': 550, 'Video Games': 300, 'Movies': 230, 'Concerts': 250},
    {'Month': 'December', 'Streaming Services': 410, 'Books': 560, 'Video Games': 310, 'Movies': 220, 'Concerts': 260}
]

months = [record['Month'] for record in data]
streaming_services = [record['Streaming Services'] for record in data]
books = [record['Books'] for record in data]
video_games = [record['Video Games'] for record in data]
movies = [record['Movies'] for record in data]
concerts = [record['Concerts'] for record in data]

plt.figure(figsize=(18, 12))

plt.plot(months, streaming_services, label='Streaming Services', marker='o', linestyle='-', color='#FF5733')
plt.plot(months, books, label='Books', marker='X', linestyle='--', color='#33FF57')
plt.plot(months, video_games, label='Video Games', marker='^', linestyle='-.', color='#3357FF')
plt.plot(months, movies, label='Movies', marker='s', linestyle=':', color='#FF33A5')
plt.plot(months, concerts, label='Concerts', marker='D', linestyle='-', color='#FFC300')

plt.title('Monthly Entertainment Preferences', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Participants')

plt.legend(loc='upper right')

plt.annotate('Peak in Book Reading', xy=('December', 560), xytext=('November', 600),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()

plt.show()