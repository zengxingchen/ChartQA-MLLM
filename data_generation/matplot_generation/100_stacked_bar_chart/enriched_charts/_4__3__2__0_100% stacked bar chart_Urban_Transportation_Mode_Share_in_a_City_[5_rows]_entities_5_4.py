
import matplotlib.pyplot as plt
import numpy as np

categories = ['Mathematics', 'Science', 'Languages', 'Arts', 'Physical Education', 'Social Studies']
primary_education = [20, 15, 25, 30, 10, 15]
secondary_education = [25, 30, 20, 25, 20, 30]
higher_education = [30, 35, 25, 15, 25, 25]
vocational_training = [25, 20, 30, 30, 25, 30]

barWidth = 0.6

r = np.arange(len(categories))

plt.figure(figsize=(10, 12))

plt.bar(r, primary_education, color='#1f77b4', edgecolor='grey', width=barWidth, label='Primary Education')
plt.bar(r, secondary_education, color='#ff7f0e', edgecolor='grey', width=barWidth, label='Secondary Education', bottom=primary_education)
plt.bar(r, higher_education, color='#2ca02c', edgecolor='grey', width=barWidth, label='Higher Education', bottom=np.array(primary_education) + np.array(secondary_education))
plt.bar(r, vocational_training, color='#d62728', edgecolor='grey', width=barWidth, label='Vocational Training', bottom=np.array(primary_education) + np.array(secondary_education) + np.array(higher_education))

plt.ylabel('Percentage')
plt.title('Distribution of Education Levels across Subjects', pad=20)
plt.xticks(r, categories, rotation=45, ha='right')
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()