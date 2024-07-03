
import matplotlib.pyplot as plt

# Data
hours_trained = [5, 6, 4, 10, 9, 3, 15, 8, 11, 14, 2, 7, 12, 13, 1, 16, 17, 18, 20, 19, 21]
performance_score = [75, 82, 70, 92, 89, 65, 97, 85, 90, 95, 60, 78, 93, 94, 55, 98, 99, 100, 100, 99, 100]

# Create the scatter plot
plt.figure(figsize=(14, 10))
plt.scatter(hours_trained, performance_score, color=['#1f77b4' if x < 10 else '#d62728' for x in hours_trained])

# Title and labels
plt.title('Correlation between Hours of Training per Week and Performance Score')
plt.xlabel('Hours of Training per Week')
plt.ylabel('Performance Score')

# Show the plot
plt.show()