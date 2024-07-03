
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Location': 'School A', 'Students Enrolled': 300, 'Classes Conducted': 50, 'Average Score': 85, 'Books Issued': 120, 'Lab Sessions': 15},
    {'Location': 'School B', 'Students Enrolled': 250, 'Classes Conducted': 45, 'Average Score': 88, 'Books Issued': 110, 'Lab Sessions': 12},
    {'Location': 'School C', 'Students Enrolled': 280, 'Classes Conducted': 47, 'Average Score': 90, 'Books Issued': 130, 'Lab Sessions': 14},
    {'Location': 'School D', 'Students Enrolled': 320, 'Classes Conducted': 52, 'Average Score': 87, 'Books Issued': 140, 'Lab Sessions': 16},
    {'Location': 'School E', 'Students Enrolled': 310, 'Classes Conducted': 48, 'Average Score': 89, 'Books Issued': 125, 'Lab Sessions': 13}
]

df = pd.DataFrame(data)
df.set_index('Location', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(12, 10))

bottom = np.zeros(len(df))

colors = ['#FF5733', '#33FFBD', '#337BFF', '#FF33A1', '#A133FF']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.6)
    bottom += df_percentage[col]

plt.xlabel('Locations')
plt.ylabel('Percentage')
plt.title('Education Statistics Breakdown (100% Stacked)', pad=20)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()