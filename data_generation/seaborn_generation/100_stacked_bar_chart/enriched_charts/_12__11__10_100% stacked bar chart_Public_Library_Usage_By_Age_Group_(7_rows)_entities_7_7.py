
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Environment', 'Online Articles': '30%', 'Podcasts': '20%', 'Documentaries': '15%', 'Books': '10%', 'Webinars': '15%', 'Research Papers': '10%'},
    {'Category': 'Climate Change', 'Online Articles': '25%', 'Podcasts': '15%', 'Documentaries': '20%', 'Books': '15%', 'Webinars': '10%', 'Research Papers': '15%'},
    {'Category': 'Sustainable Energy', 'Online Articles': '20%', 'Podcasts': '15%', 'Documentaries': '25%', 'Books': '15%', 'Webinars': '10%', 'Research Papers': '15%'},
    {'Category': 'Wildlife Conservation', 'Online Articles': '30%', 'Podcasts': '20%', 'Documentaries': '15%', 'Books': '10%', 'Webinars': '10%', 'Research Papers': '15%'},
    {'Category': 'Pollution Control', 'Online Articles': '25%', 'Podcasts': '20%', 'Documentaries': '15%', 'Books': '15%', 'Webinars': '15%', 'Research Papers': '10%'},
    {'Category': 'Recycling', 'Online Articles': '20%', 'Podcasts': '25%', 'Documentaries': '15%', 'Books': '10%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Category': 'Forestry', 'Online Articles': '25%', 'Podcasts': '15%', 'Documentaries': '15%', 'Books': '15%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Category': 'Climate Policy', 'Online Articles': '15%', 'Podcasts': '20%', 'Documentaries': '25%', 'Books': '15%', 'Webinars': '10%', 'Research Papers': '15%'},
    {'Category': 'Marine Biology', 'Online Articles': '20%', 'Podcasts': '20%', 'Documentaries': '20%', 'Books': '10%', 'Webinars': '15%', 'Research Papers': '15%'},
    {'Category': 'Sustainable Agriculture', 'Online Articles': '25%', 'Podcasts': '15%', 'Documentaries': '20%', 'Books': '15%', 'Webinars': '15%', 'Research Papers': '10%'}
]

df = pd.DataFrame(data)
df = df.set_index('Category')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(16, 12))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.75)
    bottom = cumulative_sum[column]

ax.legend(title='Resources', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Topics')
ax.set_title('Resource Distribution Across Various Environmental Topics', pad=40)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()