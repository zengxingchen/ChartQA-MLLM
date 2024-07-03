
import matplotlib.pyplot as plt

# Data
ages = [20, 30, 40, 50, 60]
reading_hours = [3.5, 4, 4.5, 5, 5.5]
reading_participants = [50, 65, 60, 70, 75]
gaming_hours = [6, 5, 3.5, 2.5, 2]
gaming_participants = [100, 150, 90, 60, 40]
exercising_hours = [5.5, 6, 5, 4.5, 4]
exercising_participants = [80, 75, 60, 55, 50]

# Create a bubble chart
plt.figure(figsize=(10, 6))  # Adjust the width and height

plt.scatter(ages, reading_hours, s=[i * 2 for i in reading_participants], c='#ff9999', alpha=0.6, label='Reading')
plt.scatter(ages, gaming_hours, s=[i * 2 for i in gaming_participants], c='#9999ff', alpha=0.6, label='Gaming')
plt.scatter(ages, exercising_hours, s=[i * 2 for i in exercising_participants], c='#99ff99', alpha=0.6, label='Exercising')

# Customize the plot
plt.title('Average Time Spent on Hobbies by Age Group', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Average Hours per Week', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()