
import matplotlib.pyplot as plt

# Data
ages = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
beach_visits_hours = [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]
beach_participants = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
hiking_hours = [6, 5.5, 5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5]
hiking_participants = [70, 65, 60, 55, 50, 45, 40, 35, 30, 25]
cultural_visits_hours = [3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
cultural_participants = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

# Create a bubble chart
plt.figure(figsize=(12, 8))  # Adjust the width and height

plt.scatter(ages, beach_visits_hours, s=[i * 2 for i in beach_participants], c='#FF5733', alpha=0.6, label='Beach Visits')
plt.scatter(ages, hiking_hours, s=[i * 2 for i in hiking_participants], c='#33FFBD', alpha=0.6, label='Hiking')
plt.scatter(ages, cultural_visits_hours, s=[i * 2 for i in cultural_participants], c='#335BFF', alpha=0.6, label='Cultural Visits')

# Customize the plot
plt.title('Average Time Spent on Travel Activities by Age Group', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Average Hours per Week', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()