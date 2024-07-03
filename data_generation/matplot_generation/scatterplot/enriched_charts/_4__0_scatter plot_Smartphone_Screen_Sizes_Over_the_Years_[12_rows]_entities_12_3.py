
import matplotlib.pyplot as plt

# Data
time_spent_on_exercise = [5, 6, 4, 10, 9, 3, 15, 8, 11, 14, 2, 7, 12, 13, 1, 16, 17, 18]
overall_fitness_score = [65, 70, 60, 85, 82, 55, 95, 80, 88, 92, 50, 75, 90, 93, 45, 97, 98, 99]

# Create the scatter plot
plt.figure(figsize=(14, 10))
plt.scatter(time_spent_on_exercise, overall_fitness_score, color=['#1f77b4' if x < 10 else '#d62728' for x in time_spent_on_exercise])

# Title and labels
plt.title('Correlation between Time Spent on Exercise and Overall Fitness Score', pad=20)
plt.xlabel('Time Spent on Exercise (hours per week)')
plt.ylabel('Overall Fitness Score')

# Show the plot
plt.show()