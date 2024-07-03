
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Reading_Hours_per_Week': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Average_Exam_Score': [55, 60, 62, 65, 67, 70, 72, 75, 77, 80, 82, 85, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 97, 98, 99, 100, 100, 100, 100, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(18, 12))
scatter_plot = sns.scatterplot(data=df, x='Reading_Hours_per_Week', y='Average_Exam_Score', color="#1F77B4")

# Customize the plot
scatter_plot.set_title('Impact of Weekly Reading Hours on Exam Scores', fontsize=20, pad=25)
scatter_plot.set(xlabel='Reading Hours per Week', ylabel='Average Exam Score (out of 100)')

plt.show()