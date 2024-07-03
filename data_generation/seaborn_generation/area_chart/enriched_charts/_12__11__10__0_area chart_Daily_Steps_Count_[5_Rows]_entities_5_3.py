
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'Distance from Sun (Millions of km)': [57.9, 108.2, 149.6, 227.9, 778.3, 1427, 2871, 4495]
}

df = pd.DataFrame(data)

colors = ["#FF5733"]

plt.figure(figsize=(16, 12))
ax = sns.lineplot(x='Planet', y='Distance from Sun (Millions of km)', data=df, color=colors[0])
ax.fill_between(df['Planet'], df['Distance from Sun (Millions of km)'], color=colors[0], alpha=0.3)

for j, point in df.iterrows():
    ax.text(point['Planet'], point['Distance from Sun (Millions of km)'], str(point['Distance from Sun (Millions of km)']), 
            ha='center', va='bottom', rotation=90, fontsize=10)

ax.set_title('Distance of Planets from the Sun (Millions of km)', fontsize=22, pad=20)
ax.set_xlabel('Planet', fontsize=16)
ax.set_ylabel('Distance from Sun (Millions of km)', fontsize=16)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()