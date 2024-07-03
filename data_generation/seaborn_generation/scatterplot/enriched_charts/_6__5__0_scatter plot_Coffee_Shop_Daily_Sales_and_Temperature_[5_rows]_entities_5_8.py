
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided table data
data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'AverageDailyStudyHours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'ExamScores': [60, 62, 63, 65, 67, 69, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 85, 87, 89, 91, 92, 94, 95, 97, 98, 99, 100, 101, 102]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(16, 9))
scatter_plot = sns.scatterplot(x='AverageDailyStudyHours', y='ExamScores', data=df, color='#ff7f0e', s=100)

# Set the chart title and labels
scatter_plot.set_title('Relationship Between Daily Study Hours and Exam Scores', fontsize=18)
scatter_plot.set_xlabel('Average Daily Study Hours', fontsize=14)
scatter_plot.set_ylabel('Exam Scores', fontsize=14)

# Show the plot
plt.show()