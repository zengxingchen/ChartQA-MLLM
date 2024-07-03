
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'English', 'Portfolio A': '15%', 'Portfolio B': '20%', 'Portfolio C': '25%', 'Portfolio D': '30%', 'Portfolio E': '15%', 'Portfolio F': '10%', 'Portfolio G': '15%', 'Portfolio H': '20%'},
    {'Category': 'Math', 'Portfolio A': '25%', 'Portfolio B': '15%', 'Portfolio C': '20%', 'Portfolio D': '10%', 'Portfolio E': '30%', 'Portfolio F': '25%', 'Portfolio G': '20%', 'Portfolio H': '15%'},
    {'Category': 'Science', 'Portfolio A': '20%', 'Portfolio B': '25%', 'Portfolio C': '15%', 'Portfolio D': '20%', 'Portfolio E': '25%', 'Portfolio F': '15%', 'Portfolio G': '20%', 'Portfolio H': '25%'},
    {'Category': 'History', 'Portfolio A': '15%', 'Portfolio B': '20%', 'Portfolio C': '10%', 'Portfolio D': '15%', 'Portfolio E': '10%', 'Portfolio F': '25%', 'Portfolio G': '15%', 'Portfolio H': '20%'},
    {'Category': 'Physical Education', 'Portfolio A': '10%', 'Portfolio B': '5%', 'Portfolio C': '20%', 'Portfolio D': '10%', 'Portfolio E': '5%', 'Portfolio F': '10%', 'Portfolio G': '15%', 'Portfolio H': '10%'},
    {'Category': 'Art', 'Portfolio A': '5%', 'Portfolio B': '10%', 'Portfolio C': '5%', 'Portfolio D': '5%', 'Portfolio E': '10%', 'Portfolio F': '10%', 'Portfolio G': '5%', 'Portfolio H': '5%'},
    {'Category': 'Music', 'Portfolio A': '10%', 'Portfolio B': '5%', 'Portfolio C': '5%', 'Portfolio D': '10%', 'Portfolio E': '5%', 'Portfolio F': '5%', 'Portfolio G': '10%', 'Portfolio H': '5%'}
]

df = pd.DataFrame(data)
df = df.set_index('Category')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4']

fig, ax = plt.subplots(figsize=(14, 8))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.8)
    bottom = cumulative_sum[column]

ax.legend(title='Subjects', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Subjects')
ax.set_title('Percentage of Time Spent on Different Subjects in Various Schools', pad=20)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()