
import matplotlib.pyplot as plt

# Data for plotting
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
average_hours_studied = [2.1, 3.4, 1.8, 4.2, 3.6, 2.9, 4.5, 3.1, 2.7, 3.9, 2.5, 4.1, 2.2, 3.7, 2.8, 4.3, 3.2, 2.6, 4.0, 3.0, 4.4, 2.3, 3.5, 2.0, 3.8, 2.4, 3.6, 4.1, 2.7, 3.9]
average_grade = [75, 80, 65, 85, 82, 78, 90, 79, 74, 88, 73, 87, 70, 83, 76, 89, 81, 72, 86, 77, 90, 71, 84, 69, 85, 72, 82, 88, 74, 87]

# Create a scatterplot
plt.figure(figsize=(16, 10))
plt.scatter(months, average_hours_studied, c="#00aaff", label="Average Hours Studied")
plt.scatter(months, average_grade, c="#ffaa00", label="Average Grade")

# Customize the chart
plt.title("Monthly Study Habits and Grades", pad=40)
plt.xlabel("Month")
plt.ylabel("Hours/Grade")
plt.legend(loc="upper left")
plt.grid(True)

# Show the scatterplot
plt.show()