
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Steps Walked': [5000, 7000, 6500, 8500, 8000, 9000, 10000]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

palette = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974', '#64b5cd', '#ffcc00']

f, ax = plt.subplots(figsize=(10, 12))

sns.barplot(x="Day", y="Steps Walked", data=df, palette=palette, ci=None)

ax.set_xlabel('Day')
ax.set_ylabel('Steps Walked')
ax.set_title('Weekly Steps Walked Data Visualization', fontsize=18, pad=20)

for p in ax.patches:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2., height, '{:1.0f}'.format(height), ha='center', va='bottom')

plt.subplots_adjust(left=0.1, right=0.95, top=0.85, bottom=0.2)

plt.show()