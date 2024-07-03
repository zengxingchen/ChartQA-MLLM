
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "City": ["New York", "New York", "New York", "Los Angeles", "Los Angeles", "Los Angeles",
             "Chicago", "Chicago", "Chicago", "Houston", "Houston", "Houston",
             "Phoenix", "Phoenix", "Phoenix", "Philadelphia", "Philadelphia", "Philadelphia",
             "San Antonio", "San Antonio", "San Antonio", "San Diego", "San Diego", "San Diego",
             "Dallas", "Dallas", "Dallas", "San Jose", "San Jose", "San Jose",
             "Seattle", "Seattle", "Seattle", "Miami", "Miami", "Miami",
             "Atlanta", "Atlanta", "Atlanta", "Boston", "Boston", "Boston"],
    "Music Genre": ["Pop", "Rap", "Rock", "Pop", "Rap", "Rock",
                    "Pop", "Rap", "Rock", "Pop", "Rap", "Rock",
                    "Pop", "Rap", "Rock", "Pop", "Rap", "Rock",
                    "Pop", "Rap", "Rock", "Pop", "Rap", "Rock",
                    "Pop", "Rap", "Rock", "Pop", "Rap", "Rock",
                    "Pop", "Rap", "Rock", "Pop", "Rap", "Rock",
                    "Pop", "Rap", "Rock", "Pop", "Rap", "Rock"],
    "Number of Artists": [520, 430, 350, 480, 400, 310, 440, 380, 290, 410, 360, 270,
                          380, 340, 250, 350, 310, 230, 320, 290, 210, 300, 270, 190,
                          280, 250, 170, 260, 240, 150, 240, 220, 130, 220, 200, 110,
                          200, 180, 90, 180, 160, 70]
}

df = pd.DataFrame(data)

grouped_data = df.groupby("Music Genre").sum().reset_index()

colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A5", "#33A5FF", "#A533FF", "#FFA533", "#33FFA5", "#FF3357"]

plt.figure(figsize=(16, 12))
squarify.plot(sizes=grouped_data['Number of Artists'], label=grouped_data['Music Genre'], alpha=0.8, color=colors)
plt.title('Number of Artists by Music Genre in Major Cities', fontsize=18, pad=20)
plt.axis('off')
plt.show()