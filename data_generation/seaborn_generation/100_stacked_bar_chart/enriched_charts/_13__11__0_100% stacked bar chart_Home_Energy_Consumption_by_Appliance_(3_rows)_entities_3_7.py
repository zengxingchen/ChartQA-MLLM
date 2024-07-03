
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {
    'Category': ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10'],
    'Math': [0.3, 0.25, 0.35, 0.4, 0.3, 0.45, 0.5, 0.4, 0.35, 0.3],
    'Science': [0.4, 0.5, 0.35, 0.3, 0.4, 0.25, 0.3, 0.35, 0.3, 0.4],
    'History': [0.3, 0.25, 0.3, 0.3, 0.3, 0.3, 0.2, 0.25, 0.35, 0.3],
}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0)

sns.set(style="whitegrid")

plt.figure(figsize=(8, 10))

df_percentage.plot(kind='bar', stacked=True, color=["#FFA07A", "#20B2AA", "#778899"], width=0.6)

formatter = FuncFormatter(lambda y, pos: "%d%%" % (y * 100))
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Subject Distribution Across Grades', fontsize=18)
plt.xlabel('Grade', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

plt.legend(title='Subjects', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()