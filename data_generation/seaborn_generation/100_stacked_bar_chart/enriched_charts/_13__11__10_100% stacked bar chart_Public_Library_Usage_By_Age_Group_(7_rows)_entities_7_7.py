
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Blogging', 'Social Media': '20%', 'Advertising': '15%', 'Email Marketing': '25%', 'Content Marketing': '20%', 'SEO': '10%', 'PPC': '10%'},
    {'Category': 'Podcasting', 'Social Media': '10%', 'Advertising': '20%', 'Email Marketing': '20%', 'Content Marketing': '25%', 'SEO': '15%', 'PPC': '10%'},
    {'Category': 'Video Production', 'Social Media': '15%', 'Advertising': '10%', 'Email Marketing': '25%', 'Content Marketing': '20%', 'SEO': '20%', 'PPC': '10%'},
    {'Category': 'Graphic Design', 'Social Media': '25%', 'Advertising': '20%', 'Email Marketing': '15%', 'Content Marketing': '10%', 'SEO': '20%', 'PPC': '10%'},
    {'Category': 'Web Development', 'Social Media': '30%', 'Advertising': '10%', 'Email Marketing': '20%', 'Content Marketing': '10%', 'SEO': '20%', 'PPC': '10%'},
    {'Category': 'App Development', 'Social Media': '25%', 'Advertising': '15%', 'Email Marketing': '15%', 'Content Marketing': '10%', 'SEO': '25%', 'PPC': '10%'},
    {'Category': 'Copywriting', 'Social Media': '20%', 'Advertising': '20%', 'Email Marketing': '25%', 'Content Marketing': '15%', 'SEO': '10%', 'PPC': '10%'},
    {'Category': 'Influencer Marketing', 'Social Media': '15%', 'Advertising': '25%', 'Email Marketing': '20%', 'Content Marketing': '10%', 'SEO': '20%', 'PPC': '10%'},
    {'Category': 'Analytics', 'Social Media': '20%', 'Advertising': '15%', 'Email Marketing': '20%', 'Content Marketing': '15%', 'SEO': '20%', 'PPC': '10%'},
    {'Category': 'E-commerce', 'Social Media': '25%', 'Advertising': '10%', 'Email Marketing': '20%', 'Content Marketing': '15%', 'SEO': '20%', 'PPC': '10%'},
    {'Category': 'Digital Strategy', 'Social Media': '20%', 'Advertising': '10%', 'Email Marketing': '20%', 'Content Marketing': '20%', 'SEO': '20%', 'PPC': '10%'}
]

df = pd.DataFrame(data)
df = df.set_index('Category')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666', '#66FF66']

fig, ax = plt.subplots(figsize=(10, 14))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.5)
    bottom = cumulative_sum[column]

ax.legend(title='Marketing Channels', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Marketing Categories')
ax.set_title('Marketing Channel Distribution Across Various Categories', pad=20)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()