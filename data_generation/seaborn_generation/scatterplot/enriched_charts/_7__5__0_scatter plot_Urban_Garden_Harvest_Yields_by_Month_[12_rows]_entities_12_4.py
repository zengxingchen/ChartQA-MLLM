import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'PlayerID': range(1, 60),
    'HoursStudied': [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0],
    'ExamScore': [55, 60, 58, 62, 64, 67, 70, 73, 75, 78, 80, 82, 85, 87, 89, 91, 93, 95, 97, 99, 100, 102, 103, 105, 106, 108, 109, 111, 112, 114, 115, 117, 118, 120, 121, 123, 124, 126, 127, 128, 130, 131, 132, 134, 135, 136, 138, 139, 140, 141, 143, 144, 145, 147, 148, 149, 150, 152, 153]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))

sns.scatterplot(x='HoursStudied', y='ExamScore', data=df, color='#e74c3c')

plt.title('Correlation Between Study Hours and Exam Scores', pad=20)
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')

plt.show()