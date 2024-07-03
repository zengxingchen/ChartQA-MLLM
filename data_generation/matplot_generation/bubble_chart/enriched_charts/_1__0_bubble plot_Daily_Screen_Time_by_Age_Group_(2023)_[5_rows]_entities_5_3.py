
import matplotlib.pyplot as plt

# Data for popular tourist attractions in the U.S.
cities = ['Broadway', 'Hollywood', 'Disneyland', 'Grand Canyon',
          'Yellowstone', 'Times Square', 'Central Park', 'Las Vegas Strip', 
          'Golden Gate Bridge', 'Statue of Liberty', 'Universal Studios', 
          'Mall of America', 'Niagara Falls', 'Smithsonian Museums', 
          'Metropolitan Museum of Art']

rating = [8.5, 7.8, 9.0, 8.9, 8.7,
          8.4, 8.6, 8.2, 8.1, 8.3,
          8.8, 8.0, 8.9, 8.7, 8.4]

reviews = [4000, 3500, 5000, 4500, 4200,
           3800, 3900, 3700, 3600, 3750,
           4100, 3400, 4600, 4300, 3950]

visitors = [15000000, 10000000, 18000000, 6000000, 4000000,
            50000000, 42000000, 43000000, 10000000, 4200000,
            9500000, 40000000, 8000000, 30000000, 6000000]

# Normalizing the visitors size to be suitable for the bubble size
bubble_size = [v / 100000 for v in visitors]

# Creating the bubble chart
plt.figure(figsize=(14, 10))
for i in range(len(cities)):
    plt.scatter(rating[i],
                reviews[i],
                s=bubble_size[i],  # Bubble sizes
                alpha=0.5,
                label=f'{cities[i]}', # Label for hover
                c=f'#{(255 - i * 15 % 255):02x}{(i * 15 % 255):02x}cc')  # Unique color for each city

# Chart title and labels
plt.title('Ratings, Reviews, and Visitors of Popular Tourist Attractions in the U.S.', pad=20)
plt.xlabel('Average Rating')
plt.ylabel('Number of Reviews')

# Adding legend with just the city names
plt.legend(loc='lower right', title='Attractions')

# Show the plot
plt.show()