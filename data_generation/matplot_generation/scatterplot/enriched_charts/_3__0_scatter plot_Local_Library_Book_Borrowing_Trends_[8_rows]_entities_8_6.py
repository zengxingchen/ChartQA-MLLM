
import matplotlib.pyplot as plt

# Data for scatterplot
categories = ["Children", "Teens", "Adults", "Seniors", "Professionals"]
percentage = [20, 25, 30, 15, 10]
number_of_people = [40, 60, 100, 30, 20]

# Size of each point will be proportional to the number of people
sizes = [people * 10 for people in number_of_people]

# Different colors for different categories
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF']

# Create scatterplot
plt.figure(figsize=(14, 10))  # increase the width and height of the chart
plt.scatter(categories, percentage, s=sizes, c=colors, alpha=0.7)

# Chart details
plt.title('Distribution of Age Groups and Their Representation in a Community')
plt.xlabel('Category')
plt.ylabel('Percentage (%)')
plt.grid(True)

# Show the chart
plt.show()