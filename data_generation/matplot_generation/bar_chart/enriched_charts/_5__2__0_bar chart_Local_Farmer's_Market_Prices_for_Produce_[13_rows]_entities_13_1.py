
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Topic": ["Painting", "Sculpting", "Photography", "Music", "Dance", "Theatre", "Literature", "Film", "Architecture", "Fashion", "Crafts", "Design"],
    "Interest Level (%)": [85, 70, 90, 95, 80, 75, 88, 92, 78, 83, 77, 81],
    "Engagement Level": [12, 8, 10, 14, 9, 11, 13, 15, 7, 12, 6, 10],
    "Expenditure ($)": [300, 200, 250, 350, 150, 220, 280, 320, 230, 300, 170, 200],
    "Frequency of Participation": [15, 10, 12, 18, 9, 11, 14, 16, 10, 13, 8, 11]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 12))

bar_height = 0.2

indices = df.index
r1 = range(len(indices))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]

ax.barh(r1, df['Interest Level (%)'], color='#FF5733', edgecolor='white', height=bar_height, label='Interest Level (%)')
ax.barh(r2, df['Engagement Level'], color='#33FF57', edgecolor='white', height=bar_height, label='Engagement Level')
ax.barh(r3, df['Expenditure ($)'], color='#3357FF', edgecolor='white', height=bar_height, label='Expenditure ($)')
ax.barh(r4, df['Frequency of Participation'], color='#F333FF', edgecolor='white', height=bar_height, label='Frequency of Participation')

ax.set_xlabel('Values', fontsize=15)
ax.set_ylabel('Categories', fontsize=15)
ax.set_title('Engagement in Art & Design Activities', fontsize=18, pad=20)

ax.set_yticks([r + bar_height for r in range(len(r1))])
ax.set_yticklabels(df['Topic'])

ax.set_xlim([50, 400])

ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))
plt.tight_layout()
plt.show()