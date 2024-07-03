
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Activity': ['Running', 'Yoga', 'Cycling', 'Swimming', 'Hiking', 'Weightlifting', 
                 'Dancing', 'Boxing', 'Pilates', 'Meditation', 'Walking', 'Tennis', 
                 'Basketball', 'Soccer'],
    'Exercise Time (hrs)': [5, 3, 4, 2, 6, 1, 2.5, 1.5, 2, 1, 3.5, 2.5, 3, 4],
    'Mental Wellness Score': [85, 90, 88, 75, 80, 65, 78, 68, 82, 95, 87, 70, 72, 75],
    'Popularity': [90, 80, 70, 60, 85, 50, 75, 55, 65, 40, 60, 45, 50, 60],
    'Color': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
              '#e7969c', '#aec7e8', '#ffbb78', '#98df8a']
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))

bubble_chart = sns.scatterplot(data=df, x='Exercise Time (hrs)', y='Mental Wellness Score', 
                               size='Popularity', hue='Color', 
                               sizes=(100, 2000), edgecolor='w', alpha=0.7, palette=df['Color'].tolist())

plt.xlabel('Exercise Time (hrs)')
plt.ylabel('Mental Wellness Score')
plt.title('Mental Wellness: Exercise Time vs. Mental Wellness Score', pad=20)
plt.legend(title='Activity Color', bbox_to_anchor=(1.05, 1), loc=2)

plt.show()