import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Reading': [1.2, 2.3, 3.1, 2.7, 3.8, 4.5, 3.0]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 9))

ax.fill_between(df['Day'], df['Reading'], color='#ff5733', alpha=0.7, label='Reading')

for i, txt in enumerate(df['Reading']):
    ax.annotate(txt, (df['Day'][i], df['Reading'][i]), textcoords="offset points", xytext=(0, 5), ha='center')

ax.set_title('Weekly Hours Spent on Reading Activities', fontsize=18)
ax.set_xlabel('Day', fontsize=15)
ax.set_ylabel('Hours', fontsize=15)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()