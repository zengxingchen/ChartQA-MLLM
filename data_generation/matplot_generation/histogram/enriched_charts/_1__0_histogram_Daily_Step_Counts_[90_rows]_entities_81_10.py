
import matplotlib.pyplot as plt

# Data points
book_ranges = ["0-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40"]
frequency = [4, 8, 15, 20, 10, 5, 3, 1]

# Modify the plot size
plt.figure(figsize=(10, 6))

# Create a vertical histogram
plt.bar(book_ranges, frequency, color="#FF5733", edgecolor="#C70039", width=0.6)  # Adjusted band width and color

# Customize the display
plt.xlabel('Number of Books', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Books Read by Students in a Year', fontsize=14)

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the histogram
plt.show()