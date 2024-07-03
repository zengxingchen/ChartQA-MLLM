
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
books_read = [23, 30, 27, 35, 40, 45, 50, 60, 55, 65, 70, 75]

# Creating the figure and specifying figure size
plt.figure(figsize=(10, 12))

# Creating the bar chart as a horizontal chart
plt.barh(months, books_read, height=0.5, color=['#FF5733', '#FF6F33', '#FF8733', '#FF9F33', '#FFB733', '#FFCF33', '#FFE733', '#FFFF33', '#E7FF33', '#CFFF33', '#B7FF33', '#9FFF33'])

# Adding labels and title
plt.xlabel('Number of Books Read')
plt.ylabel('Month')
plt.title('Books Read Per Month - 2023', pad=20)

# Setting y-axis limit
plt.xlim(20, 80)

# Show the plot
plt.show()