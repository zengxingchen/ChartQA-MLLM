
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'ScienceResearch': [1200, 1250, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200],
    'TechnologicalAdvancements': [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450],
    'InnovativeProjects': [700, 720, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

plt.figure(figsize=(20, 14))

plt.fill_between(df.index, 0, df_cum['ScienceResearch'], color=colors[0], alpha=0.7, label='Science Research')
plt.fill_between(df.index, df_cum['ScienceResearch'], df_cum['ScienceResearch'] + df_cum['TechnologicalAdvancements'], color=colors[1], alpha=0.7, label='Technological Advancements')
plt.fill_between(df.index, df_cum['ScienceResearch'] + df_cum['TechnologicalAdvancements'], df_cum['ScienceResearch'] + df_cum['TechnologicalAdvancements'] + df_cum['InnovativeProjects'], color=colors[2], alpha=0.7, label='Innovative Projects')

for category in ['ScienceResearch', 'TechnologicalAdvancements', 'InnovativeProjects']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, 
             category.replace("ScienceResearch", "Science Research").replace("TechnologicalAdvancements", "Technological Advancements"), 
             verticalalignment='center')

plt.title('Monthly Science and Technology Contributions', pad=30, fontsize=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Hours Dedicated', fontsize=16)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.tight_layout()

plt.show()