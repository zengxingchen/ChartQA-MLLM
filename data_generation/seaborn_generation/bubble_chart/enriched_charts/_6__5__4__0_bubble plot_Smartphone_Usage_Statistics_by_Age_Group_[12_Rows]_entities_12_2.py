
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Age': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    'Daily_Study_Hours': [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14],
    'Test_Score': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165],
    'Interest_Level': [10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55, 57, 60, 62, 65, 68, 70]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df, x='Age', y='Daily_Study_Hours', hue='Test_Score', size='Interest_Level', sizes=(50, 1500),
                               palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#FFA133'])

bubble_chart.set_title('Daily Study Hours and Test Scores by Age', fontsize=20, pad=20)
bubble_chart.set_xlabel('Age (Years)', fontsize=16)
bubble_chart.set_ylabel('Daily Study Hours', fontsize=16)

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.show()