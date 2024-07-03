
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Destination': 'Europe', 'Vegetables': '25%', 'Fruits': '20%', 'Proteins': '15%', 'Grains': '20%', 'Dairy': '10%', 'Sweets': '10%'},
    {'Destination': 'Asia', 'Vegetables': '20%', 'Fruits': '25%', 'Proteins': '20%', 'Grains': '15%', 'Dairy': '10%', 'Sweets': '10%'},
    {'Destination': 'Africa', 'Vegetables': '15%', 'Fruits': '20%', 'Proteins': '25%', 'Grains': '15%', 'Dairy': '10%', 'Sweets': '15%'},
    {'Destination': 'North America', 'Vegetables': '20%', 'Fruits': '15%', 'Proteins': '20%', 'Grains': '25%', 'Dairy': '10%', 'Sweets': '10%'},
    {'Destination': 'South America', 'Vegetables': '25%', 'Fruits': '15%', 'Proteins': '15%', 'Grains': '25%', 'Dairy': '10%', 'Sweets': '10%'},
    {'Destination': 'Australia', 'Vegetables': '20%', 'Fruits': '20%', 'Proteins': '20%', 'Grains': '20%', 'Dairy': '10%', 'Sweets': '10%'},
    {'Destination': 'Antarctica', 'Vegetables': '10%', 'Fruits': '10%', 'Proteins': '10%', 'Grains': '10%', 'Dairy': '40%', 'Sweets': '20%'}
]

df = pd.DataFrame(data)
df = df.set_index('Destination')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF4500']

fig, ax = plt.subplots(figsize=(14, 10))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.7)
    bottom = cumulative_sum[column]

ax.legend(title='Food Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Destination')
ax.set_title('Nutritional Preferences by Region')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()