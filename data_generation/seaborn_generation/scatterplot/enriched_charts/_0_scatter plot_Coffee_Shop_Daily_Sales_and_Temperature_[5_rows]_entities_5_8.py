
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided table data
data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    'DailyHoursStudied': [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 4, 5, 6, 7, 8, 9],
    'ExamScore': [65, 70, 72, 74, 76, 78, 80, 82, 85, 87, 89, 90, 91, 93, 94, 95, 97, 99, 100, 77, 84, 88, 92, 96, 98]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(12, 6))
scatter_plot = sns.scatterplot(x='DailyHoursStudied', y='ExamScore',
                               data=df, color='#1f77b4', s=50)

# Set the chart title and labels
scatter_plot.set_title('Relationship Between Daily Study Hours and Exam Scores', fontsize=16)
scatter_plot.set_xlabel('Daily Hours Studied', fontsize=14)
scatter_plot.set_ylabel('Exam Score', fontsize=14)

# Show the plot
plt.show()