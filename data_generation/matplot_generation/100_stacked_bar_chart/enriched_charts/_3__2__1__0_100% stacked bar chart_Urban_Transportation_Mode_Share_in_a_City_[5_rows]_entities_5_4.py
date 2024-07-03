
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
exercise = np.array([25, 20, 15, 10, 5, 5])
healthy_eating = np.array([30, 35, 25, 20, 15, 10])
regular_checkups = np.array([20, 25, 30, 35, 40, 45])
stress_management = np.array([15, 10, 20, 25, 30, 30])
others = np.array([10, 10, 10, 10, 10, 10])

# Calculate percentages
totals = exercise + healthy_eating + regular_checkups + stress_management + others
exercise_percentage = exercise / totals * 100
healthy_eating_percentage = healthy_eating / totals * 100
regular_checkups_percentage = regular_checkups / totals * 100
stress_management_percentage = stress_management / totals * 100
others_percentage = others / totals * 100

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

# Horizontal bar plot
age_indices = np.arange(len(age_groups))

p1 = plt.barh(age_indices, exercise_percentage, color='#FF5733', edgecolor='white', height=bar_width)
p2 = plt.barh(age_indices, healthy_eating_percentage, left=exercise_percentage, color='#33FF57', edgecolor='white', height=bar_width)
p3 = plt.barh(age_indices, regular_checkups_percentage, left=exercise_percentage+healthy_eating_percentage, color='#3357FF', edgecolor='white', height=bar_width)
p4 = plt.barh(age_indices, stress_management_percentage, left=exercise_percentage+healthy_eating_percentage+regular_checkups_percentage, color='#FF33A6', edgecolor='white', height=bar_width)
p5 = plt.barh(age_indices, others_percentage, left=exercise_percentage+healthy_eating_percentage+regular_checkups_percentage+stress_management_percentage, color='#33FFF5', edgecolor='white', height=bar_width)

plt.xlabel('Percentage')
plt.title('Distribution of Health Habits Among Age Groups')
plt.yticks(age_indices, age_groups)
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Exercise', 'Healthy Eating', 'Regular Checkups', 'Stress Management', 'Others'), loc='lower right')
plt.show()