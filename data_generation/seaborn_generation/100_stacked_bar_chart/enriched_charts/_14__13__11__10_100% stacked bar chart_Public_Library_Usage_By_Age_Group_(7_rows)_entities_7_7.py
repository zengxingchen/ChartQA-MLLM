
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Plants', 'Photosynthesis': '25%', 'Respiration': '15%', 'Transpiration': '20%', 'Reproduction': '10%', 'Adaptation': '20%', 'Defense': '10%'},
    {'Category': 'Algae', 'Photosynthesis': '20%', 'Respiration': '10%', 'Transpiration': '15%', 'Reproduction': '10%', 'Adaptation': '25%', 'Defense': '20%'},
    {'Category': 'Fungi', 'Photosynthesis': '10%', 'Respiration': '25%', 'Transpiration': '10%', 'Reproduction': '20%', 'Adaptation': '15%', 'Defense': '20%'},
    {'Category': 'Mosses', 'Photosynthesis': '15%', 'Respiration': '20%', 'Transpiration': '25%', 'Reproduction': '10%', 'Adaptation': '15%', 'Defense': '15%'},
    {'Category': 'Ferns', 'Photosynthesis': '20%', 'Respiration': '10%', 'Transpiration': '20%', 'Reproduction': '25%', 'Adaptation': '15%', 'Defense': '10%'},
    {'Category': 'Flowering Plants', 'Photosynthesis': '30%', 'Respiration': '20%', 'Transpiration': '10%', 'Reproduction': '15%', 'Adaptation': '10%', 'Defense': '15%'},
    {'Category': 'Conifers', 'Photosynthesis': '15%', 'Respiration': '25%', 'Transpiration': '20%', 'Reproduction': '10%', 'Adaptation': '20%', 'Defense': '10%'},
    {'Category': 'Cycads', 'Photosynthesis': '20%', 'Respiration': '10%', 'Transpiration': '25%', 'Reproduction': '15%', 'Adaptation': '10%', 'Defense': '20%'},
    {'Category': 'Ginkgo', 'Photosynthesis': '10%', 'Respiration': '20%', 'Transpiration': '10%', 'Reproduction': '25%', 'Adaptation': '20%', 'Defense': '15%'},
    {'Category': 'Bryophytes', 'Photosynthesis': '15%', 'Respiration': '10%', 'Transpiration': '30%', 'Reproduction': '20%', 'Adaptation': '10%', 'Defense': '15%'},
    {'Category': 'Liverworts', 'Photosynthesis': '25%', 'Respiration': '15%', 'Transpiration': '10%', 'Reproduction': '20%', 'Adaptation': '20%', 'Defense': '10%'}
]

df = pd.DataFrame(data)
df = df.set_index('Category')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF5733', '#33FFBD', '#FF33EC', '#335CFF', '#FF8333', '#33FF57']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.4)
    bottom = cumulative_sum[column]

ax.legend(title='Biological Processes', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Plant Categories')
ax.set_title('Distribution of Biological Processes Across Various Plant Categories', pad=20)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()