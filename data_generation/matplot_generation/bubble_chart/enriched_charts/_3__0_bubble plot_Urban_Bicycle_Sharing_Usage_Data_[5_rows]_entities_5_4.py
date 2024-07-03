
import matplotlib.pyplot as plt

# Define data points
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City', 'Beijing', 'Cairo', 'New York', 'Bangkok', 'Los Angeles', 'Moscow', 'Dubai', 'Sydney', 'Cape Town', 'Berlin', 'Paris', 'London', 'Rome', 'Madrid', 'Toronto', 'San Francisco', 'Chicago', 'Vancouver', 'Buenos Aires']
books_read = [12, 18, 10, 8, 16, 11, 14, 13, 17, 9, 7, 5, 6, 20, 15, 22, 21, 19, 25, 23, 24, 26, 27, 28, 29]
study_hours = [15, 20, 13, 14, 22, 12, 16, 19, 18, 10, 11, 9, 8, 25, 21, 24, 23, 26, 28, 27, 30, 29, 31, 32, 33]
average_grades = [90, 88, 85, 83, 87, 82, 89, 84, 91, 80, 79, 78, 77, 92, 86, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]

# Normalize grades for bubble sizes
size_factor = 10
sizes = [g * size_factor for g in average_grades]

# Define colors
colors = ['#4B8BBE', '#306998', '#FFE873', '#FFD43B', '#646464', '#00568B', '#FF5733', '#33FFBD', '#33D4FF', '#FF33E2', '#A833FF', '#3385FF', '#5B5D8B', '#8B1A1A', '#8B8B00', '#5D5D5D', '#336B5D', '#3F005D', '#8B0056', '#5D8B75', '#5D8B5D', '#5D5D8B', '#8B0033', '#8B3300', '#8B3300']

# Create the plot
plt.figure(figsize=(16,12))
plt.scatter(books_read, study_hours, s=sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=0.5)

# Create labels and title
plt.title('Books Read vs. Study Hours with Average Grades Bubble Sizes')
plt.xlabel('Books Read')
plt.ylabel('Study Hours')

# Add city labels to the bubbles
for i, city in enumerate(cities):
    plt.text(books_read[i], study_hours[i], city, ha='center', va='center', fontsize=8)

# Show the plot
plt.tight_layout()
plt.show()