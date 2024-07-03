
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'StudyHours': [2, 3, 1.5, 2.5, 4, 5, 3.5, 2.5, 4.5, 3, 5, 1, 6, 5.5,
                   3, 4, 2, 5.5, 4.5, 6.5, 5, 3.5, 4.2, 2.8, 5.1, 3.9, 6.3, 5.6],
    'ExamScore': [45, 50, 35, 55, 60, 70, 65, 48, 72, 58, 78, 40, 85, 80,
                  52, 68, 46, 77, 70, 90, 75, 60, 65, 50, 74, 64, 88, 82]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create the scatterplot
plt.figure(figsize=(12, 8))
scatter_plot = sns.scatterplot(x='StudyHours', y='ExamScore',
                               data=df, color="#1F77B4", s=60)

# Customize the axes and title
scatter_plot.set_title('Study Hours vs. Exam Scores', fontsize=18, pad=20)
scatter_plot.set_xlabel('Study Hours', fontsize=14)
scatter_plot.set_ylabel('Exam Score', fontsize=14)

# Show the plot
plt.show()