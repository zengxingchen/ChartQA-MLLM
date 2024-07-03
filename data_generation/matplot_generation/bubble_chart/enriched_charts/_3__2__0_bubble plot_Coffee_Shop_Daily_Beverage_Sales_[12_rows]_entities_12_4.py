
import matplotlib.pyplot as plt

# Data
age = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
exercise_hours = [1.5, 2.0, 2.2, 2.5, 2.8, 3.0, 2.5, 2.3, 2.0, 1.8, 1.5, 1.3, 1.0, 0.8]
exercise_participants = [65, 70, 60, 75, 80, 90, 85, 70, 65, 60, 55, 50, 45, 40]
sleep_hours = [7, 6.8, 6.5, 6.3, 6.0, 5.8, 5.5, 5.2, 5.0, 4.8, 4.5, 4.2, 4.0, 3.8]
sleep_participants = [80, 75, 70, 85, 90, 95, 80, 70, 60, 55, 50, 45, 40, 35]
work_hours = [4, 4.5, 5, 5.5, 6, 6.5, 6, 5.8, 5.5, 5.2, 5, 4.8, 4.5, 4.2]
work_participants = [90, 85, 80, 75, 70, 65, 75, 60, 55, 50, 45, 40, 35, 30]

# Create a bubble chart
plt.figure(figsize=(14, 10))  # Adjust the width and height

plt.scatter(age, exercise_hours, s=[i * 2 for i in exercise_participants], c='#FF7F50', alpha=0.6, label='Exercise')
plt.scatter(age, sleep_hours, s=[i * 2 for i in sleep_participants], c='#6495ED', alpha=0.6, label='Sleep')
plt.scatter(age, work_hours, s=[i * 2 for i in work_participants], c='#8A2BE2', alpha=0.6, label='Work')

# Customize the plot
plt.title('Average Daily Activities by Age Group', fontsize=18, y=1.05)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Average Hours per Day', fontsize=14)
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()