
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points in pandas DataFrame
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jane',
                'Kevin', 'Laura', 'Mike', 'Nina', 'Oscar', 'Paul', 'Quincy', 'Rachel', 'Sam', 'Tina',
                'Ursula', 'Victor', 'Wendy', 'Xander', 'Yara', 'Zane'],
    'StudyHours': [5, 3, 7, 2, 8, 6, 4, 9, 5.5, 3.5, 7.5, 6.5, 4.5, 8.5, 2.5, 1.5, 7, 6, 5, 4, 9, 3, 2, 8, 5.5, 4.5],
    'ExamScore': [78, 52, 91, 43, 95, 84, 65, 97, 79, 58, 92, 88, 67, 96, 50, 38, 89, 82, 77, 64, 98, 54, 46, 93, 80, 69]
}

df = pd.DataFrame(data)

# Setting sns theme and figure size
sns.set_theme()
plt.figure(figsize=(16, 10))

# Creating scatterplot with customized color scheme
scatterplot = sns.scatterplot(x='StudyHours', y='ExamScore', data=df, s=100,
                              palette=['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2'])

# Customize further details of the plot
scatterplot.axes.set_title('Student Performance: Study Hours vs Exam Scores', fontsize=18, weight='bold', y=1.05)
scatterplot.set_xlabel('Study Hours', fontsize=14)
scatterplot.set_ylabel('Exam Score', fontsize=14)
scatterplot.figure.set_size_inches(16, 10)  # Change width and height of the chart
plt.show()