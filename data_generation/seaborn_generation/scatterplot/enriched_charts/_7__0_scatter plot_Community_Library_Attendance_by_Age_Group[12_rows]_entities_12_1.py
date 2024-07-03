
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    'Daily Exercise Time': [1.5, 0.5, 2.0, 3.5, 4.0, 1.2, 2.5, 3.8, 0.8, 4.5, 2.8, 3.0, 3.3, 1.8, 0.3, 1.0, 3.2, 4.8, 2.3, 0.7, 2.7, 3.4, 4.2, 1.4, 2.1, 3.6, 4.7, 1.9, 0.6, 2.4, 3.1, 0.9, 4.3, 2.6, 1.3, 3.7, 4.6, 1.1, 2.2, 3.9],
    'Mental Wellness Score': [65, 45, 75, 90, 92, 58, 80, 88, 50, 95, 82, 85, 87, 70, 40, 60, 86, 98, 78, 48, 83, 89, 93, 67, 77, 91, 97, 72, 47, 79, 84, 52, 94, 81, 66, 87, 96, 62, 76, 88]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))

scatter = sns.scatterplot(
    x='Daily Exercise Time',
    y='Mental Wellness Score',
    data=df,
    color='#3498db',
    s=100
)

scatter.set_title('Relationship Between Daily Exercise Time and Mental Wellness Score', fontsize=18)
scatter.set_xlabel('Daily Exercise Time (hours)', fontsize=14)
scatter.set_ylabel('Mental Wellness Score', fontsize=14)

plt.show()