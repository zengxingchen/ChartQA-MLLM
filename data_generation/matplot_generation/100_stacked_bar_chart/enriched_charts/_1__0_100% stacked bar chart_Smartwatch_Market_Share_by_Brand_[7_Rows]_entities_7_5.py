
import matplotlib.pyplot as plt
import numpy as np

# Data
subjects = ['Math', 'Science', 'English', 'History', 'Art']
grades_a = [20, 25, 30, 15, 10]
grades_b = [30, 35, 25, 20, 25]
grades_c = [25, 20, 25, 35, 30]
grades_d = [15, 10, 10, 20, 25]
grades_f = [10, 10, 10, 10, 10]

# Convert to percentage
total = np.array(grades_a) + np.array(grades_b) + np.array(grades_c) + np.array(grades_d) + np.array(grades_f)
grades_a = np.array(grades_a) / total * 100
grades_b = np.array(grades_b) / total * 100
grades_c = np.array(grades_c) / total * 100
grades_d = np.array(grades_d) / total * 100
grades_f = np.array(grades_f) / total * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 6))

bar_width = 0.5
bar_spacing = 1.5

bar1 = ax.bar(subjects, grades_a, bar_width, color='#FF5733', label='Grade A')
bar2 = ax.bar(subjects, grades_b, bar_width, bottom=grades_a, color='#33FF57', label='Grade B')
bar3 = ax.bar(subjects, grades_c, bar_width, bottom=grades_a+grades_b, color='#3357FF', label='Grade C')
bar4 = ax.bar(subjects, grades_d, bar_width, bottom=grades_a+grades_b+grades_c, color='#FF33A8', label='Grade D')
bar5 = ax.bar(subjects, grades_f, bar_width, bottom=grades_a+grades_b+grades_c+grades_d, color='#FFC133', label='Grade F')

# Add title and labels
ax.set_title('Distribution of Grades in Different Subjects', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Subjects')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()