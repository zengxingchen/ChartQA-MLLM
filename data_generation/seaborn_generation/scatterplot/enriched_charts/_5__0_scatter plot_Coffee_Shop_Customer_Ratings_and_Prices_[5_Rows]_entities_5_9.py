
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age': [10, 10, 10, 10, 12, 12, 12, 12, 14, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 20, 20, 20, 20, 22, 22, 22, 22, 24, 24, 24, 24, 26, 26, 26, 26],
    'Internet_Usage': [5, 6, 4, 7, 10, 8, 9, 11, 14, 12, 13, 15, 18, 16, 19, 17, 20, 21, 22, 23, 25, 24, 26, 27, 28, 30, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    'Test_Score': [85, 87, 82, 90, 78, 80, 73, 75, 65, 70, 68, 62, 55, 60, 53, 58, 50, 48, 45, 43, 40, 42, 38, 35, 33, 30, 32, 28, 25, 27, 22, 20, 18, 15, 17, 12]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
scatter_plot = sns.scatterplot(x='Internet_Usage', y='Test_Score', hue='Age', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFD2'], data=df)

scatter_plot.set_title('Impact of Internet Usage on Test Scores by Age', fontsize=16, pad=20)
scatter_plot.set_xlabel('Average Weekly Internet Usage (hours)', fontsize=14)
scatter_plot.set_ylabel('Average Test Score (out of 100)', fontsize=14)

plt.legend(title='Age Group', loc='upper right', bbox_to_anchor=(1.15, 1))
plt.show()