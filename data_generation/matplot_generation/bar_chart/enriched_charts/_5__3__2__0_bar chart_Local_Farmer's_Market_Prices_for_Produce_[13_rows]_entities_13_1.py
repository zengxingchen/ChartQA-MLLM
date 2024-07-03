import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Category": ["Philosophy", "Ethics", "Logic", "Metaphysics", "Epistemology", "Aesthetics", "Existentialism", "Utilitarianism", "Deontology", "Phenomenology", "Nihilism", "Pragmatism", "Stoicism", "Hedonism", "Absurdism", "Objectivism", "Transcendentalism", "Determinism"],
    "Number of Articles Written": [21, 17, 15, 19, 13, 18, 16, 14, 20, 22, 12, 11, 10, 23, 9, 8, 24, 25],
    "Hours Spent Researching": [130, 115, 100, 120, 85, 105, 110, 95, 125, 140, 80, 75, 70, 145, 65, 60, 150, 155],
    "Expenditure on Writing Materials (in $)": [260, 245, 220, 230, 200, 240, 225, 210, 250, 270, 190, 180, 170, 275, 160, 150, 280, 285],
    "Interest in Writing (%)": [94, 90, 88, 92, 87, 89, 91, 86, 93, 95, 84, 83, 82, 96, 81, 80, 97, 98]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(18, 14))

bar_height = 0.25

indices = df.index
r1 = range(len(indices))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]

ax.bar(r1, df['Number of Articles Written'], color='#1f77b4', edgecolor='white', width=bar_height, label='Number of Articles Written')
ax.bar(r2, df['Hours Spent Researching'], color='#ff7f0e', edgecolor='white', width=bar_height, label='Hours Spent Researching')
ax.bar(r3, df['Expenditure on Writing Materials (in $)'], color='#2ca02c', edgecolor='white', width=bar_height, label='Expenditure on Writing Materials (in $)')
ax.bar(r4, df['Interest in Writing (%)'], color='#d62728', edgecolor='white', width=bar_height, label='Interest in Writing (%)')

ax.set_ylabel('Values', fontsize=15)
ax.set_xlabel('Categories', fontsize=15)
ax.set_title('Philosophical Studies: Articles, Research, and Resources', fontsize=18, pad=20)

ax.set_xticks([r + bar_height for r in range(len(r1))])
ax.set_xticklabels(df['Category'], rotation=90)

ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15))

plt.tight_layout()
plt.ylim([5, 30])
plt.show()