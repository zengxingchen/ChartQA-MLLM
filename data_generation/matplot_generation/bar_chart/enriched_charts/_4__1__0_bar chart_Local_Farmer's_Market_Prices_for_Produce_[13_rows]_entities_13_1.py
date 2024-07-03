
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Miami", "Seattle", "Denver", "Boston"],
    "Classical": [3.2, 2.8, 3.0, 2.5, 2.6, 2.7, 2.4, 2.9, 2.8, 2.7, 3.1, 2.9, 3.0, 2.6, 2.7],
    "Rock": [4.5, 4.2, 4.0, 3.8, 3.7, 4.1, 3.9, 4.3, 4.1, 4.0, 4.4, 4.2, 4.3, 3.9, 4.1],
    "Pop": [5.3, 5.1, 5.0, 4.8, 4.7, 5.2, 4.6, 5.0, 4.9, 4.8, 5.1, 5.0, 5.2, 4.8, 5.3],
    "Jazz": [2.8, 3.0, 2.7, 2.9, 2.5, 2.6, 2.4, 2.7, 2.8, 2.5, 2.8, 3.1, 2.9, 2.6, 2.7],
    "Hip-Hop": [3.7, 3.9, 3.5, 3.6, 3.4, 3.8, 3.3, 3.6, 3.7, 3.5, 3.9, 3.7, 3.8, 3.6, 3.7]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.12

r1 = range(len(df))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]
r5 = [x + bar_height for x in r4]

ax.barh(r1, df['Classical'], color='#1E90FF', edgecolor='white', height=bar_height, label='Classical')
ax.barh(r2, df['Rock'], color='#FF4500', edgecolor='white', height=bar_height, label='Rock')
ax.barh(r3, df['Pop'], color='#32CD32', edgecolor='white', height=bar_height, label='Pop')
ax.barh(r4, df['Jazz'], color='#FFD700', edgecolor='white', height=bar_height, label='Jazz')
ax.barh(r5, df['Hip-Hop'], color='#8A2BE2', edgecolor='white', height=bar_height, label='Hip-Hop')

ax.set_xlabel('Average Daily Listening Hours', fontsize=13)
ax.set_ylabel('City', fontsize=13)
ax.set_title('Average Daily Listening Hours by Music Genre and City', fontsize=15, pad=20)

ax.set_yticks([r + 2*bar_height for r in range(len(r1))])
ax.set_yticklabels(df['City'])

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()