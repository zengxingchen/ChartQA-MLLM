
import matplotlib.pyplot as plt

# Data
ages = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
outdoor_hours = [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]
outdoor_participants = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
reading_hours = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5]
reading_participants = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
movies_hours = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]
movies_participants = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Create a bubble chart
plt.figure(figsize=(14, 9))  # Adjust the width and height

plt.scatter(ages, outdoor_hours, s=[i * 2 for i in outdoor_participants], c='#FF5733', alpha=0.6, label='Outdoor Activities')
plt.scatter(ages, reading_hours, s=[i * 2 for i in reading_participants], c='#33FFBD', alpha=0.6, label='Reading')
plt.scatter(ages, movies_hours, s=[i * 2 for i in movies_participants], c='#335BFF', alpha=0.6, label='Movies')

# Customize the plot
plt.title('Average Time Spent on Leisure Activities by Age Group', fontsize=18, pad=20)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Average Hours per Week', fontsize=14)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()