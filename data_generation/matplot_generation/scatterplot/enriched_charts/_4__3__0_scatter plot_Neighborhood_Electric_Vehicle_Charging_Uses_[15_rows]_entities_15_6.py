
import matplotlib.pyplot as plt

# Data points for movie ratings vs box office revenue
movies = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ"]
ratings = [3.5, 4.2, 3.0, 4.8, 2.9, 4.1, 3.7, 4.5, 3.2, 4.0, 3.4, 4.7, 2.8, 4.3, 3.9, 4.6, 3.1, 4.4, 3.6, 4.9, 2.7, 4.0, 3.8, 4.2, 2.6, 4.5, 3.3, 4.6, 2.5, 4.3, 3.9, 4.7, 3.0, 4.8, 2.9, 4.4]
box_office_revenue = [50, 150, 70, 300, 45, 200, 120, 250, 60, 180, 80, 275, 40, 210, 160, 260, 55, 230, 110, 320, 35, 175, 140, 190, 30, 240, 75, 280, 25, 220, 150, 290, 65, 310, 50, 235]

# Creating the scatter plot
plt.figure(figsize=(16, 8))  # Modify width and height of the chart
plt.scatter(ratings, box_office_revenue, color='#FF5733')  # Change to an RGB color code

# Adding chart labels and title
plt.title('Movie Ratings vs. Box Office Revenue', pad=20)
plt.xlabel('Movie Ratings')
plt.ylabel('Box Office Revenue (Millions)')

# Show the figure
plt.show()