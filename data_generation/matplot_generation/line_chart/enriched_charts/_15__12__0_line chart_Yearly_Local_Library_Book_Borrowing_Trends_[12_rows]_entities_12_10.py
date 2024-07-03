
import matplotlib.pyplot as plt

# Data points
dates = ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01",
         "2024-06-01", "2024-07-01", "2024-08-01", "2024-09-01", "2024-10-01",
         "2024-11-01", "2024-12-01"]
books_borrowed = [950, 850, 700, 750, 600, 450, 400, 350, 500, 650, 700, 800]

# Creating the line chart
plt.figure(figsize=(10, 5))

plt.plot(dates, books_borrowed, color="#8A2BE2", marker='o')

# Annotating the highest and lowest points
plt.annotate('Highest\n950 Books', xy=("2024-01-01", 950), xytext=("2024-01-01", 1000),
             arrowprops=dict(facecolor='#FF1493', shrink=0.05), ha='center')
plt.annotate('Lowest\n350 Books', xy=("2024-08-01", 350), xytext=("2024-08-01", 300),
             arrowprops=dict(facecolor='#00FA9A', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Library Book Borrowings in 2024", fontsize=16, pad=20)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Books Borrowed", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')

# Inverting the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()