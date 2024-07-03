
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Category": ["Fiction", "Non-Fiction", "Science", "History", "Biography", "Fantasy", "Mystery", "Self-Help", "Comics", "Travel", "Poetry", "Drama", "Philosophy", "Education", "Art", "Economics", "Music", "Sports"],
    "Number of Articles Written": [18, 15, 10, 20, 8, 22, 12, 7, 25, 9, 5, 14, 11, 13, 19, 17, 21, 16],
    "Hours Spent Researching": [120, 100, 80, 110, 70, 130, 90, 60, 140, 75, 50, 95, 85, 105, 115, 110, 125, 100],
    "Expenditure on Writing Materials (in $)": [250, 200, 180, 240, 160, 260, 190, 140, 270, 170, 130, 210, 175, 220, 230, 225, 245, 215],
    "Interest in Writing (%)": [92, 88, 85, 90, 80, 94, 86, 75, 95, 82, 72, 87, 84, 89, 91, 87, 93, 86]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 12))

bar_height = 0.2

indices = df.index
r1 = range(len(indices))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]

ax.barh(r1, df['Number of Articles Written'], color='#FF6F61', edgecolor='white', height=bar_height, label='Number of Articles Written')
ax.barh(r2, df['Hours Spent Researching'], color='#6B5B95', edgecolor='white', height=bar_height, label='Hours Spent Researching')
ax.barh(r3, df['Expenditure on Writing Materials (in $)'], color='#88B04B', edgecolor='white', height=bar_height, label='Expenditure on Writing Materials (in $)')
ax.barh(r4, df['Interest in Writing (%)'], color='#F7CAC9', edgecolor='white', height=bar_height, label='Interest in Writing (%)')

ax.set_xlabel('Values', fontsize=15)
ax.set_ylabel('Categories', fontsize=15)
ax.set_title('Writing Habits and Expenditures by Category', fontsize=18, pad=20)

ax.set_yticks([r + bar_height for r in range(len(r1))])
ax.set_yticklabels(df['Category'])

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.tight_layout()
plt.show()