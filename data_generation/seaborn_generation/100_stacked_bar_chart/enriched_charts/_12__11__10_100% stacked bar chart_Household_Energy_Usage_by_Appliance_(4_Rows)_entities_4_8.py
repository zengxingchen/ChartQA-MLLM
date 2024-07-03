
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Subject': 'Math', 'Assignments Completed': 20, 'Hours Studied': 40, 'Projects Done': 5, 'Exams Passed': 3, 'Attendance': 95},
    {'Subject': 'Science', 'Assignments Completed': 18, 'Hours Studied': 35, 'Projects Done': 6, 'Exams Passed': 4, 'Attendance': 92},
    {'Subject': 'History', 'Assignments Completed': 15, 'Hours Studied': 30, 'Projects Done': 4, 'Exams Passed': 4, 'Attendance': 90},
    {'Subject': 'Literature', 'Assignments Completed': 17, 'Hours Studied': 32, 'Projects Done': 3, 'Exams Passed': 5, 'Attendance': 88},
    {'Subject': 'Art', 'Assignments Completed': 22, 'Hours Studied': 28, 'Projects Done': 7, 'Exams Passed': 2, 'Attendance': 85}
]

df = pd.DataFrame(data)
df.set_index('Subject', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(12, 10))

bottom = np.zeros(len(df))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.6)
    bottom += df_percentage[col]

plt.xlabel('Subjects')
plt.ylabel('Percentage')
plt.title('Student Performance Breakdown (100% Stacked)', pad=20)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()