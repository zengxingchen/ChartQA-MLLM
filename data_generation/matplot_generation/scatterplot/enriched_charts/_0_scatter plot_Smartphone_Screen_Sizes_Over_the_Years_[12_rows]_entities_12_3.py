
import matplotlib.pyplot as plt

# Data
hours_studied = [5, 6, 4, 10, 9, 3, 15, 8, 11, 14, 2, 7, 12, 13, 1]
exam_score = [75, 82, 70, 92, 89, 65, 97, 85, 90, 95, 60, 78, 93, 94, 55]

# Create the scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(hours_studied, exam_score, color=['#2ca02c' if x < 10 else '#ff7f0e' for x in hours_studied])

# Title and labels
plt.title('Correlation between Hours Studied and Exam Scores')
plt.xlabel('Hours Studied per Week')
plt.ylabel('Final Exam Score')

# Show the plot
plt.show()