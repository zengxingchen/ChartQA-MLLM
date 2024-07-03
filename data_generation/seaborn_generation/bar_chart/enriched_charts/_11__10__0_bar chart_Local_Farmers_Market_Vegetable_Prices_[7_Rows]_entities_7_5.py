
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte'],
    'average_study_hours': [3.5, 3.7, 3.2, 3.6, 3.4, 3.3, 3.8, 3.9, 3.6, 3.7, 3.5, 3.4, 3.3, 3.5, 3.6]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
barplot = sns.barplot(
    x='average_study_hours',
    y='city',
    data=df,
    palette=['#4B0082', '#FF1493', '#1E90FF', '#32CD32', '#FFD700', '#FF4500', '#DA70D6', '#8A2BE2', '#5F9EA0',
             '#FF69B4', '#20B2AA', '#B22222', '#FF6347', '#4682B4', '#008080'],
    orient='h'
)

for bar in barplot.patches:
    bar.set_height(0.5)

plt.title('Average Daily Study Hours in Different Cities', fontsize=16, pad=20)
plt.xlabel('Average Study Hours', fontsize=14)
plt.ylabel('City', fontsize=14)

plt.show()