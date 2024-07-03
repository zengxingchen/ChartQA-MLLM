
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'],
    'Science': [25, 27, 26, 28, 29, 30, 31, 32, 33, 34, 35],
    'Math': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'History': [30, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19],
    'Art': [25, 24, 25, 23, 22, 21, 20, 19, 18, 17, 16]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(8, 10))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']

bottoms = [0] * len(df_percentage)
for i, col in enumerate(df_percentage.columns):
    ax.bar(df_percentage.index, df_percentage[col], bottom=bottoms, color=colors[i], edgecolor='white', width=0.6)
    bottoms = bottoms + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_title('Student Enrollment by Subject Over Years')
ax.legend(df_percentage.columns, loc='upper left', bbox_to_anchor=(1, 1))

ax.set_axisbelow(True)
ax.yaxis.grid(True, color='gray', linestyle='dashed', alpha=0.7)

plt.tight_layout()
plt.show()