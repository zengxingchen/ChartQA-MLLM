
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Profession': ['Doctor', 'Engineer', 'Teacher', 'Artist', 'Lawyer', 'Nurse', 'Scientist', 'Musician', 'Writer', 'Chef', 'Athlete'],
    'HoursOfSleep': [6.5, 7.1, 7.4, 8.0, 6.2, 6.8, 7.5, 8.2, 7.9, 7.0, 8.5],
    'StressLevel': [8.2, 7.3, 6.5, 5.9, 8.5, 7.8, 6.0, 5.5, 6.2, 7.1, 5.0],
    'Productivity': [70.1, 75.4, 80.2, 85.6, 65.3, 72.0, 78.5, 82.3, 80.7, 74.3, 88.9]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble = sns.scatterplot(data=df, x='HoursOfSleep', y='StressLevel', size='Productivity', hue='Profession', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#57FFC1', '#FFD133', '#8333FF', '#33FFF7', '#FF335B', '#FF9733', '#737373'], sizes=(100, 2000), alpha=0.7, edgecolor='black')

plt.title('Hours of Sleep vs. Stress Level in Different Professions', fontsize=18, pad=20)
plt.xlabel('Hours of Sleep', fontsize=14)
plt.ylabel('Stress Level', fontsize=14)

hand, labl = bubble.get_legend_handles_labels()
bubble.legend(hand[1:], labl[1:], title='Profession', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()