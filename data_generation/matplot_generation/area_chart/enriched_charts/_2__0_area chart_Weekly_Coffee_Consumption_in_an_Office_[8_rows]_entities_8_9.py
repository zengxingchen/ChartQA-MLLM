
import matplotlib.pyplot as plt

# Generate data points
days = list(range(1, 31))
number_of_books_read = [
    2, 3, 4, 5, 3, 7, 6, 5, 6, 8, 9, 7, 8, 9, 10, 12, 13, 12, 14, 15,
    13, 16, 17, 18, 19, 20, 22, 21, 23, 24
]

# Create an area chart
plt.figure(figsize=(14, 8))
plt.fill_between(days, number_of_books_read, color="#FF5733")

# Customize axes and labels
plt.title("Monthly Reading Progress in June")
plt.xlabel("Day of the Month")
plt.ylabel("Number of Books Read")
plt.xticks(range(1, 31, 2))
plt.yticks(range(0, 26, 2))

# Add annotation
plt.text(15, 20, "Peak reading period", fontsize=12, color='blue')

# Display the plot
plt.show()