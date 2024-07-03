
import matplotlib.pyplot as plt

# Define the data for the scatterplot
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
books_read = [3, 5, 2, 6, 4, 5, 7, 4, 8, 6, 7, 9, 5, 10, 8, 7, 9, 6, 11, 8, 9, 10, 
              12, 11, 13, 10, 12, 14, 11, 13, 15]
study_hours = [2, 3, 2, 4, 3, 4, 5, 3, 6, 4, 5, 6, 4, 7, 5, 4, 6, 4, 8, 5, 6, 7, 
               8, 7, 9, 6, 8, 10, 7, 9, 10]

# Create the scatterplot
plt.figure(figsize=(12, 8))  # Change width and height of the chart reasonably
plt.scatter(books_read, study_hours, color='#FF6347')  # Modify the color scheme using a specific color code

# Apply labels and a title to the scatterplot
plt.xlabel('Books Read')
plt.ylabel('Study Hours')
plt.title('Study Hours vs Books Read')

# Display the scatterplot
plt.show()