
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Category": ["Pop Music", "Classical Music", "Jazz", "Rock", "Hip-Hop", "Electronic", "Country", "Blues", "Reggae",
                 "Soul", "Folk", "R&B", "Gospel", "Latin", "Metal", "Punk", "Disco", "Opera", "K-Pop", "Soundtrack",
                 "Alternative", "Indie", "Funk", "Ska", "Techno", "House", "Dubstep", "Trap", "Trance"],
    "Amount": [1200, 900, 1500, 600, 1100, 800, 1000, 700, 1300, 500, 400, 950, 850, 720, 530, 470, 650, 300, 550,
               770, 900, 820, 480, 520, 430, 610, 760, 670, 780]
}

df = pd.DataFrame(data)
grouped_data = df.groupby("Category").sum().reset_index()

colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33A1", "#33FFF6", "#FF8333", "#8C33FF", "#33FF96",
          "#FF3333", "#33FF33", "#3333FF", "#FFCC33", "#FF3399", "#33FFCC", "#FF6633", "#9933FF", "#33FF66",
          "#FF3366", "#66FF33", "#3366FF", "#CCFF33", "#FF33CC", "#33FF99", "#FF9933", "#3333CC", "#33CCFF",
          "#FF3396", "#33CC66"]

plt.figure(figsize=(18, 14))
squarify.plot(sizes=grouped_data['Amount'], label=grouped_data['Category'], alpha=0.8, color=colors)
plt.title('Music Genres by Popularity', fontsize=22, pad=20)
plt.axis('off')
plt.show()