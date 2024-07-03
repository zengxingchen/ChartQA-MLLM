
import matplotlib.pyplot as plt

# Data
ages = [18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
math_hours = [4.5, 5, 4.8, 5.2, 4.9, 5.1, 5.4, 4.7, 5.3, 5, 4.6, 5.2]
math_participants = [70, 85, 60, 75, 65, 80, 90, 55, 85, 70, 60, 80]
science_hours = [3.5, 4, 4.2, 4.5, 4.7, 4.3, 4.6, 4.8, 4.4, 4.2, 4.1, 4.5]
science_participants = [90, 75, 65, 80, 85, 70, 95, 60, 80, 75, 65, 85]
arts_hours = [2.5, 3, 3.2, 3.5, 3.8, 3.6, 3.9, 4.1, 4, 3.7, 3.4, 3.8]
arts_participants = [60, 50, 55, 60, 70, 65, 75, 50, 65, 55, 50, 70]

# Create a bubble chart
plt.figure(figsize=(12, 8))  # Adjust the width and height

plt.scatter(ages, math_hours, s=[i * 2 for i in math_participants], c='#FF6347', alpha=0.6, label='Mathematics')
plt.scatter(ages, science_hours, s=[i * 2 for i in science_participants], c='#4682B4', alpha=0.6, label='Science')
plt.scatter(ages, arts_hours, s=[i * 2 for i in arts_participants], c='#32CD32', alpha=0.6, label='Arts')

# Customize the plot
plt.title('Average Study Hours by Age Group in Different Subjects', fontsize=18)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Average Hours per Week', fontsize=14)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()