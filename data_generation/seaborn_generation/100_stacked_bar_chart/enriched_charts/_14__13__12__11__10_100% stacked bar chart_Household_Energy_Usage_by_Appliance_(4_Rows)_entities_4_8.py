
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Category': 'Region A', 'Physical Health': 70, 'Emotional Wellbeing': 80, 'Mental Health': 75, 'Social Health': 65, 'Lifestyle Health': 85},
    {'Category': 'Region B', 'Physical Health': 75, 'Emotional Wellbeing': 82, 'Mental Health': 78, 'Social Health': 70, 'Lifestyle Health': 88},
    {'Category': 'Region C', 'Physical Health': 60, 'Emotional Wellbeing': 75, 'Mental Health': 70, 'Social Health': 60, 'Lifestyle Health': 80},
    {'Category': 'Region D', 'Physical Health': 65, 'Emotional Wellbeing': 78, 'Mental Health': 72, 'Social Health': 68, 'Lifestyle Health': 82},
    {'Category': 'Region E', 'Physical Health': 68, 'Emotional Wellbeing': 79, 'Mental Health': 74, 'Social Health': 67, 'Lifestyle Health': 84},
    {'Category': 'Region F', 'Physical Health': 72, 'Emotional Wellbeing': 81, 'Mental Health': 76, 'Social Health': 69, 'Lifestyle Health': 87}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(12, 10))

bottom = np.zeros(len(df))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD133']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.6)
    bottom += df_percentage[col]

plt.xlabel('Regions')
plt.ylabel('Percentage')
plt.title('Health Metrics Breakdown by Region (100% Stacked)', pad=20)
plt.legend(title='Health Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()