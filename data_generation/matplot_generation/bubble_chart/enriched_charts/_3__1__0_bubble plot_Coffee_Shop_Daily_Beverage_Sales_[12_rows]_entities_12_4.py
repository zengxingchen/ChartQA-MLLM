
import matplotlib.pyplot as plt

# Data
ages = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
weekly_study_hours = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
study_participants = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
weekly_exercise_hours = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
exercise_participants = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
weekly_sleep_hours = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
sleep_participants = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Create a bubble chart
plt.figure(figsize=(14, 10))  # Adjust the width and height

plt.scatter(ages, weekly_study_hours, s=[i * 2 for i in study_participants], c='#1f77b4', alpha=0.6, label='Study')
plt.scatter(ages, weekly_exercise_hours, s=[i * 2 for i in exercise_participants], c='#ff7f0e', alpha=0.6, label='Exercise')
plt.scatter(ages, weekly_sleep_hours, s=[i * 2 for i in sleep_participants], c='#2ca02c', alpha=0.6, label='Sleep')

# Customize the plot
plt.title('Weekly Hours Spent on Activities by Age Group', fontsize=16, pad=20)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Average Hours per Week', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()