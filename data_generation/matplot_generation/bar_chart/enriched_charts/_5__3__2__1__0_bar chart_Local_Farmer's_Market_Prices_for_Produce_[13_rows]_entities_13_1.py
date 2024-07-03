import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Topic": ["Space Exploration", "Natural Sciences", "Fashion & Beauty", "Literature & Writing", "History & Archaeology", "Climate Change", "Travel & Adventure", "Economics & Finance", "Business & Entrepreneurship", "Sports & Fitness", "Music & Performing Arts", "Food & Nutrition", "Culture & Society", "Art & Design", "Entertainment & Leisure", "Politics & Governance", "Future Technologies", "Health & Psychology", "Philosophy & Ethics"],
    "Online Courses": [4.7, 4.5, 4.3, 4.4, 4.6, 4.8, 4.2, 4.3, 4.5, 4.1, 4.4, 4.6, 4.5, 4.3, 4.2, 4.6, 4.7, 4.5, 4.4],
    "Workshops": [3.9, 4.0, 3.8, 4.1, 4.2, 4.3, 3.7, 3.9, 4.1, 3.6, 4.0, 4.2, 4.0, 3.9, 3.8, 4.2, 4.3, 4.0, 3.9],
    "Webinars": [4.2, 4.1, 3.9, 4.3, 4.1, 4.5, 4.0, 4.2, 4.3, 3.9, 4.2, 4.3, 4.2, 4.0, 3.9, 4.4, 4.5, 4.2, 4.1],
    "Study Groups": [4.3, 4.4, 4.1, 4.5, 4.4, 4.7, 4.2, 4.4, 4.6, 4.0, 4.5, 4.6, 4.4, 4.2, 4.1, 4.5, 4.7, 4.4, 4.3],
    "Independent Study": [4.8, 4.7, 4.5, 4.8, 4.9, 5.0, 4.4, 4.6, 4.9, 4.3, 4.7, 4.8, 4.7, 4.5, 4.4, 4.9, 5.0, 4.8, 4.7]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 14))

bar_height = 0.12

r1 = range(len(df))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]
r5 = [x + bar_height for x in r4]

ax.barh(r1, df['Online Courses'], color='#FF6347', edgecolor='white', height=bar_height, label='Online Courses')
ax.barh(r2, df['Workshops'], color='#4682B4', edgecolor='white', height=bar_height, label='Workshops')
ax.barh(r3, df['Webinars'], color='#32CD32', edgecolor='white', height=bar_height, label='Webinars')
ax.barh(r4, df['Study Groups'], color='#FFD700', edgecolor='white', height=bar_height, label='Study Groups')
ax.barh(r5, df['Independent Study'], color='#8A2BE2', edgecolor='white', height=bar_height, label='Independent Study')

ax.set_ylabel('Average Engagement', fontsize=15)
ax.set_xlabel('Learning Method', fontsize=15)
ax.set_title('Average Engagement in Different Learning Methods by Topic', fontsize=18, pad=20)

ax.set_yticks([r + 2*bar_height for r in range(len(r1))])
ax.set_yticklabels(df['Topic'])

ax.set_xlim([3.5, 5])

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
plt.tight_layout()
plt.show()