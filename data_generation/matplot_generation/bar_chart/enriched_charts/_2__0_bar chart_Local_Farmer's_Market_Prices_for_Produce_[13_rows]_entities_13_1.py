
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Category": ["Fiction", "Non-Fiction", "Science", "History", "Biography", "Fantasy", "Mystery", "Self-Help", "Comics", "Travel", "Poetry", "Drama"],
    "Number of Books Read in a Year": [15, 10, 8, 12, 7, 14, 9, 5, 13, 6, 4, 11],
    "Frequency of Visits to Library": [10, 8, 6, 9, 5, 11, 7, 4, 12, 5, 3, 9],
    "Expenditure on Books (in $)": [200, 150, 120, 180, 100, 210, 130, 90, 220, 110, 70, 160],
    "Interest in Reading (%)": [90, 85, 80, 88, 75, 92, 78, 70, 95, 77, 65, 83]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.18

indices = df.index
r1 = range(len(indices))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

ax.bar(r1, df['Number of Books Read in a Year'], color='#FF5733', edgecolor='white', width=bar_width, label='Number of Books Read in a Year')
ax.bar(r2, df['Frequency of Visits to Library'], color='#33FF57', edgecolor='white', width=bar_width, label='Frequency of Visits to Library')
ax.bar(r3, df['Expenditure on Books (in $)'], color='#3357FF', edgecolor='white', width=bar_width, label='Expenditure on Books (in $)')
ax.bar(r4, df['Interest in Reading (%)'], color='#F333FF', edgecolor='white', width=bar_width, label='Interest in Reading (%)')

ax.set_ylabel('Categories', fontsize=15)
ax.set_xlabel('Values', fontsize=15)
ax.set_title('Reading Habits and Expenditures by Category', fontsize=18, pad=20)

ax.set_xticks([r + bar_width for r in range(len(r1))])
ax.set_xticklabels(df['Category'])

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()