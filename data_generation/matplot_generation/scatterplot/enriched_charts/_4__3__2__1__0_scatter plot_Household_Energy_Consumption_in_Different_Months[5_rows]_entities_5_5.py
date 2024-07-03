
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
hours_of_study = [1, 2, 1.5, 3, 2.5, 3.5, 2, 4, 3, 2.5, 4.5, 5, 3.5, 4, 4.5, 5.5, 3, 2.5, 3.5, 4.5, 2, 1.5, 3, 4, 5, 5.5, 6, 4, 3, 2.5]
test_scores = [50, 55, 53, 65, 60, 67, 58, 70, 66, 62, 73, 75, 68, 72, 74, 77, 64, 61, 69, 76, 57, 54, 63, 71, 78, 79, 80, 73, 65, 59]

# Create a scatterplot
plt.figure(figsize=(16, 10))
plt.scatter(days, hours_of_study, c="#8A2BE2", label="Hours of Study")
plt.scatter(days, test_scores, c="#228B22", label="Test Scores")

# Customize the chart
plt.title("Daily Study Hours and Test Scores in June", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Hours/Score")
plt.legend(loc='upper right')
plt.grid(True)

# Show the scatterplot
plt.show()