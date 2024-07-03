
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Age': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Average_Sleep': [14, 14, 13.5, 13, 12.8, 12.5, 12, 11.8, 11.5, 11, 10.8, 10.5, 10.2, 10, 9.8, 9.5, 9.2, 9, 8.8, 8.5, 8.2, 8, 7.8, 7.5, 7.2, 7, 6.8, 6.5, 6.2, 6],
    'Screen_Time': [1, 1.5, 1.7, 2, 2.3, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5],
    'Count': [5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 18, 22, 25, 28, 30, 32, 35, 37, 40, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, x='Age', y='Average_Sleep', hue='Screen_Time', size='Count', sizes=(100, 2000),
                               palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])

bubble_chart.set_title('Average Sleep and Screen Time by Age', fontsize=20, pad=30)
bubble_chart.set_xlabel('Age (Years)', fontsize=14)
bubble_chart.set_ylabel('Average Sleep (Hours per Night)', fontsize=14)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()