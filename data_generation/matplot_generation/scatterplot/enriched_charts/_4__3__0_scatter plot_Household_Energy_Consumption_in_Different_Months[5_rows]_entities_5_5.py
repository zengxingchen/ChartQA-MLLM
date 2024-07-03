
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
books_read = [1, 2, 1, 3, 2, 2, 3, 4, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 
              10, 9, 10, 11, 10, 11, 12]
writing_hours = [2, 2.5, 3, 3.5, 4, 3, 2.5, 3.5, 4, 4.5, 5, 5.5, 6, 5.5, 6.5, 6, 
                 5.5, 6, 6.5, 7, 7.5, 7, 6.5, 7, 7.5, 8, 8.5, 8, 8.5, 9]

# Create a scatterplot
plt.figure(figsize=(16, 12))
plt.scatter(days, books_read, c="#3498db", label="Books Read")
plt.scatter(days, writing_hours, c="#e74c3c", label="Writing Hours (Hours)")

# Customize the chart
plt.title("Monthly Literary Activities", fontsize=16)
plt.xlabel("Day of the Month", fontsize=14)
plt.ylabel("Books Read / Writing Hours", fontsize=14)
plt.legend(loc="upper right")
plt.grid(True)

# Show the scatterplot
plt.show()