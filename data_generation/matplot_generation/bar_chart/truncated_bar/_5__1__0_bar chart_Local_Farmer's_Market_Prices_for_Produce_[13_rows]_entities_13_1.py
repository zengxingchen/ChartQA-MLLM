
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
    "Running": [5.2, 5.5, 5.0, 4.8, 5.1, 5.3, 4.9, 5.4, 5.2, 5.1],
    "Cycling": [4.8, 4.7, 4.5, 4.2, 4.6, 4.7, 4.3, 4.9, 4.6, 4.5],
    "Swimming": [3.5, 3.6, 3.2, 3.0, 3.4, 3.6, 3.3, 3.7, 3.5, 3.4],
    "Yoga": [4.0, 4.3, 3.8, 3.5, 4.1, 4.2, 3.7, 4.4, 4.0, 4.1],
    "Weightlifting": [3.8, 4.0, 3.5, 3.2, 3.7, 3.8, 3.4, 4.1, 3.8, 3.7]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.15

r1 = range(len(df))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]
r5 = [x + bar_height for x in r4]

ax.barh(r1, df['Running'], color='#1f77b4', edgecolor='white', height=bar_height, label='Running')
ax.barh(r2, df['Cycling'], color='#ff7f0e', edgecolor='white', height=bar_height, label='Cycling')
ax.barh(r3, df['Swimming'], color='#2ca02c', edgecolor='white', height=bar_height, label='Swimming')
ax.barh(r4, df['Yoga'], color='#d62728', edgecolor='white', height=bar_height, label='Yoga')
ax.barh(r5, df['Weightlifting'], color='#9467bd', edgecolor='white', height=bar_height, label='Weightlifting')

ax.set_xlabel('Average Weekly Exercise Hours', fontsize=15)
ax.set_ylabel('City', fontsize=15)
ax.set_title('Average Weekly Exercise Hours by Activity and City', fontsize=18)

ax.set_yticks([r + 2*bar_height for r in range(len(r1))])
ax.set_yticklabels(df['City'])

ax.set_xlim(3, 6)

ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))
plt.tight_layout()
plt.show()