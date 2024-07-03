
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the provided data
data = {
    'StudentID': range(1, 31),
    'HoursStudied': [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0,
                     6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5,
                     12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5],
    'ExamScore': [56, 60, 62, 65, 67, 70, 72, 74, 76, 78, 80, 82, 84, 85, 87,
                  89, 91, 93, 95, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108]
}

df = pd.DataFrame(data)

# Setting the figure size for the scatterplot
plt.figure(figsize=(12, 6))

# Plotting the scatterplot with a specific color scheme
sns.scatterplot(x='HoursStudied', y='ExamScore', data=df, color='#FF5733')

# Set the chart title and labels
plt.title('Relationship Between Hours Studied and Exam Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')

# Display the scatterplot
plt.show()