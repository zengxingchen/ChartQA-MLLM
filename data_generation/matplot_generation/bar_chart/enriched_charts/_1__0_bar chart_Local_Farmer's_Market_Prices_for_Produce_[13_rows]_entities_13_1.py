
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
    "Classical": [3.2, 2.8, 3.0, 2.5, 2.6, 2.7, 2.4, 2.9, 2.8, 2.7],
    "Rock": [4.5, 4.2, 4.0, 3.8, 3.7, 4.1, 3.9, 4.3, 4.1, 4.0],
    "Pop": [5.3, 5.1, 5.0, 4.8, 4.7, 5.2, 4.6, 5.0, 4.9, 4.8],
    "Jazz": [2.8, 3.0, 2.7, 2.9, 2.5, 2.6, 2.4, 2.7, 2.8, 2.5],
    "Hip-Hop": [3.7, 3.9, 3.5, 3.6, 3.4, 3.8, 3.3, 3.6, 3.7, 3.5]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.12  # Adjusted bar width

r1 = range(len(df))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

ax.bar(r1, df['Classical'], color='#2E8B57', edgecolor='white', width=bar_width, label='Classical')
ax.bar(r2, df['Rock'], color='#8B0000', edgecolor='white', width=bar_width, label='Rock')
ax.bar(r3, df['Pop'], color='#4682B4', edgecolor='white', width=bar_width, label='Pop')
ax.bar(r4, df['Jazz'], color='#DAA520', edgecolor='white', width=bar_width, label='Jazz')
ax.bar(r5, df['Hip-Hop'], color='#4B0082', edgecolor='white', width=bar_width, label='Hip-Hop')

ax.set_ylabel('Average Daily Listening Hours', fontsize=15)
ax.set_xlabel('City', fontsize=15)
ax.set_title('Average Daily Listening Hours by Music Genre and City', fontsize=18)

ax.set_xticks([r + 2*bar_width for r in range(len(r1))])
ax.set_xticklabels(df['City'], rotation=45, ha='right')

ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.show()