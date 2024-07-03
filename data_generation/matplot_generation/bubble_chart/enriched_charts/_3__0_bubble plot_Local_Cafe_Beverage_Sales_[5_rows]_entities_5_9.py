
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['5-12', '13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
primary_education = [30, 50, 20, 10, 5, 3, 2, 1]
secondary_education = [10, 40, 80, 70, 50, 30, 15, 5]
higher_education = [5, 10, 50, 90, 70, 50, 30, 10]
online_learning = [5, 15, 60, 80, 50, 30, 20, 10]
adult_education = [2, 8, 20, 40, 30, 20, 15, 10]

# Bubble sizes
bubble_scale = 200
primary_sizes = np.array(primary_education) * bubble_scale
secondary_sizes = np.array(secondary_education) * bubble_scale
higher_sizes = np.array(higher_education) * bubble_scale
online_sizes = np.array(online_learning) * bubble_scale
adult_sizes = np.array(adult_education) * bubble_scale

fig, ax = plt.subplots(figsize=(16, 10))  # Set the width and height of the chart

# Create scatter points for each educational category
ax.scatter(age_groups, primary_education, s=primary_sizes, color='#ff7f0e', alpha=0.6, label='Primary Education')
ax.scatter(age_groups, secondary_education, s=secondary_sizes, color='#1f77b4', alpha=0.6, label='Secondary Education')
ax.scatter(age_groups, higher_education, s=higher_sizes, color='#2ca02c', alpha=0.6, label='Higher Education')
ax.scatter(age_groups, online_learning, s=online_sizes, color='#d62728', alpha=0.6, label='Online Learning')
ax.scatter(age_groups, adult_education, s=adult_sizes, color='#9467bd', alpha=0.6, label='Adult Education')

# Chart title and labels
ax.set_title('Educational Engagement by Age Group and Category', fontsize=18, pad=20)
ax.set_xlabel('Age Group', fontsize=14)
ax.set_ylabel('Number of Participants (in thousands)', fontsize=14)

# Legend
ax.legend(loc='upper left', title='Education Categories')

plt.tight_layout()
plt.show()