
import matplotlib.pyplot as plt

# Data for cities, number of dance studios, music venues, and student population
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston',
          'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 
          'Dallas', 'San Jose', 'Austin', 'Jacksonville', 
          'Fort Worth', 'Columbus', 'Charlotte']

dance_studios = [150, 100, 80, 60, 50, 70, 40, 60, 55, 45, 65, 30, 35, 25, 40]
music_venues = [200, 150, 120, 100, 90, 110, 80, 90, 85, 70, 95, 50, 60, 40, 75]
student_population = [1000000, 700000, 500000, 400000, 300000, 350000, 250000, 320000, 280000, 260000, 330000, 150000, 170000, 120000, 180000]

# Normalizing the student population size to be suitable for the bubble size
bubble_size = [p / 10000 for p in student_population]

# Creating the bubble chart
plt.figure(figsize=(14, 10))
for i in range(len(cities)):
    plt.scatter(dance_studios[i],
                music_venues[i],
                s=bubble_size[i],  # Bubble sizes
                alpha=0.5,
                label=f'{cities[i]}',  # Label for hover
                c=f'#{hex(100 + i * 10 % 155)[2:].zfill(2)}{hex(50 + i * 15 % 155)[2:].zfill(2)}ff')  # Unique color for each city

# Chart title and labels
plt.title('Dance Studios, Music Venues, and Student Population in U.S. Cities', pad=20)
plt.xlabel('Number of Dance Studios')
plt.ylabel('Number of Music Venues')

# Adding legend with just the city names
plt.legend(loc='upper left', title='Cities')

# Show the plot
plt.show()