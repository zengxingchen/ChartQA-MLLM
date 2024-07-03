
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Topic": ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Literature", "Philosophy", "Sociology", "Psychology", "Economics"],
    "Online Courses": [4.5, 4.2, 4.0, 4.3, 4.1, 4.4, 4.2, 4.3, 4.5, 4.1],
    "Workshops": [3.8, 3.9, 3.7, 4.0, 3.9, 4.1, 3.8, 4.0, 4.2, 3.9],
    "Webinars": [4.1, 4.0, 3.9, 4.2, 4.1, 4.3, 4.0, 4.1, 4.4, 4.0],
    "Study Groups": [4.3, 4.1, 4.0, 4.4, 4.2, 4.5, 4.1, 4.3, 4.6, 4.2],
    "Independent Study": [4.7, 4.4, 4.3, 4.6, 4.5, 4.8, 4.3, 4.5, 4.8, 4.4]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.12

r1 = range(len(df))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

ax.bar(r1, df['Online Courses'], color='#FF4500', edgecolor='white', width=bar_width, label='Online Courses')
ax.bar(r2, df['Workshops'], color='#1E90FF', edgecolor='white', width=bar_width, label='Workshops')
ax.bar(r3, df['Webinars'], color='#32CD32', edgecolor='white', width=bar_width, label='Webinars')
ax.bar(r4, df['Study Groups'], color='#FFD700', edgecolor='white', width=bar_width, label='Study Groups')
ax.bar(r5, df['Independent Study'], color='#8A2BE2', edgecolor='white', width=bar_width, label='Independent Study')

ax.set_xlabel('Average Engagement', fontsize=15)
ax.set_ylabel('Learning Method', fontsize=15)
ax.set_title('Average Engagement in Different Learning Methods by Topic', fontsize=18)

ax.set_xticks([r + 2*bar_width for r in range(len(r1))])
ax.set_xticklabels(df['Topic'])

ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.show()