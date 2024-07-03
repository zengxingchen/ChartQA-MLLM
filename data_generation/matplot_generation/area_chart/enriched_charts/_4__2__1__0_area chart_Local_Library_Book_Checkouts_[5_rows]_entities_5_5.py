
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Visitors': [150, 180, 170, 200, 220, 190, 210, 230, 250, 240, 230, 260, 280, 270, 300, 310, 330, 320, 340, 350, 340, 330, 360, 370, 360, 380, 390, 400, 390, 410, 420]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df['Day'], df['Visitors'], color='#ADD8E6', alpha=0.7)
plt.plot(df['Day'], df['Visitors'], color='#00008B')

for i in range(len(df)):
    plt.text(df['Day'][i], df['Visitors'][i] + 10, str(df['Visitors'][i]), ha='center', va='bottom', fontsize=8)

plt.title('Daily Visitors to the Museum Over a Month', fontsize=18, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

plt.tight_layout()
plt.show()