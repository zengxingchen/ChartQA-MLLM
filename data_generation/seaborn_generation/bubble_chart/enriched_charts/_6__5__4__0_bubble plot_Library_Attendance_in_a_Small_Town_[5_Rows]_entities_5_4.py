
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Activity': ['Running', 'Yoga', 'Cycling', 'Swimming', 'Hiking', 'Weightlifting', 
                 'Dancing', 'Boxing', 'Pilates', 'Meditation', 'Walking', 'Tennis', 
                 'Basketball', 'Soccer', 'Reading', 'Gaming', 'Cooking', 'Gardening'],
    'Sleep Duration (hrs)': [7.5, 6.5, 7, 6, 8, 5, 6.5, 5.5, 6, 8, 7, 6.5, 7, 7.5, 8, 5, 7, 7.5],
    'Happiness Score': [85, 90, 88, 75, 80, 65, 78, 68, 82, 95, 87, 70, 72, 75, 93, 55, 83, 85],
    'Popularity': [90, 80, 70, 60, 85, 50, 75, 55, 65, 40, 60, 45, 50, 60, 55, 35, 65, 70],
    'Color': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
              '#e7969c', '#aec7e8', '#ffbb78', '#98df8a', '#ff6699', 
              '#3399ff', '#cc33ff', '#66cc33']
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))

bubble_chart = sns.scatterplot(data=df, x='Sleep Duration (hrs)', y='Happiness Score', 
                               size='Popularity', hue='Color', 
                               sizes=(100, 2000), edgecolor='w', alpha=0.7, palette=df['Color'].tolist())

plt.xlabel('Sleep Duration (hrs)')
plt.ylabel('Happiness Score')
plt.title('Health & Psychology: Sleep Duration vs. Happiness Score', pad=40)
plt.legend(title='Activity Color', bbox_to_anchor=(1.05, 1), loc=2)

plt.show()