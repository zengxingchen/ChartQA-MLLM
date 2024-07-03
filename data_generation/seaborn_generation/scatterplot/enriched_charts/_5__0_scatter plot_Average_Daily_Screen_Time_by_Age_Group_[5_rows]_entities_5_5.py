
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'RunningDistance': [5.2, 6.5, 7.0, 4.8, 8.1, 5.7, 9.0, 6.3, 4.5, 7.2, 6.8, 5.0, 8.3, 5.5, 7.5, 6.0, 9.2, 4.9, 8.5, 5.3],
    'CaloriesBurned': [300, 350, 400, 280, 420, 310, 450, 340, 260, 380, 370, 290, 430, 320, 390, 330, 460, 285, 440, 305]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
scatterplot = sns.scatterplot(x='RunningDistance', y='CaloriesBurned', data=df, color='#2E8B57')

scatterplot.set_title('Running Distance vs Calories Burned', fontsize=18)
scatterplot.set_xlabel('Running Distance (km)', fontsize=14)
scatterplot.set_ylabel('Calories Burned (kcal)', fontsize=14)

plt.show()