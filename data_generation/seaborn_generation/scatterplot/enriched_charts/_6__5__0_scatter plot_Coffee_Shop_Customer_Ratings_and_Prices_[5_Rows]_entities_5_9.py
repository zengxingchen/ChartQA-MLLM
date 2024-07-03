
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age': [10, 10, 10, 10, 12, 12, 12, 12, 14, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 20, 20, 20, 20, 22, 22, 22, 22, 24, 24, 24, 24, 26, 26, 26, 26],
    'Exercise_Hours': [5, 6, 4, 7, 8, 10, 7, 11, 9, 12, 10, 13, 14, 16, 12, 17, 15, 18, 17, 20, 22, 23, 21, 24, 26, 28, 25, 30, 29, 31, 33, 35, 36, 38, 34, 39],
    'Test_Score': [85, 87, 82, 90, 78, 80, 73, 75, 65, 70, 68, 62, 55, 60, 53, 58, 50, 48, 45, 43, 40, 42, 38, 35, 33, 30, 32, 28, 25, 27, 22, 20, 18, 15, 17, 12]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
scatter_plot = sns.scatterplot(x='Exercise_Hours', y='Test_Score', hue='Age', palette=['#FF6347', '#4682B4', '#32CD32', '#FF1493', '#1E90FF'], data=df)

scatter_plot.set_title('Impact of Exercise Hours on Test Scores by Age', fontsize=18, pad=30)
scatter_plot.set_xlabel('Average Weekly Exercise Hours', fontsize=14)
scatter_plot.set_ylabel('Average Test Score (out of 100)', fontsize=14)

plt.legend(title='Age Group', loc='upper right', bbox_to_anchor=(1.25, 1))
plt.show()