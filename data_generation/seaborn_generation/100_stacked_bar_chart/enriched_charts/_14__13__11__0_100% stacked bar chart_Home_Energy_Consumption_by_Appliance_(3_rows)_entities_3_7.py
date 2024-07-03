
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {
    'Age Group': ['Teenagers', 'Young Adults', 'Adults', 'Middle-aged', 'Seniors'],
    'Exercise': [0.4, 0.35, 0.3, 0.25, 0.2],
    'Reading': [0.35, 0.4, 0.45, 0.4, 0.35],
    'Socializing': [0.25, 0.25, 0.25, 0.35, 0.45],
}

df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0)

sns.set(style="whitegrid")

plt.figure(figsize=(10, 8))

df_percentage.plot(kind='bar', stacked=True, color=["#FF6347", "#4682B4", "#32CD32"], width=0.5)

formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Activity Distribution Across Age Groups', fontsize=18)
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

plt.legend(title='Activities', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()