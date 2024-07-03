
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'India', 'Japan', 'United Kingdom', 
             'France', 'Germany', 'South Korea', 'Italy', 'Spain', 
             'Canada', 'Australia', 'Russia', 'Brazil', 'Mexico']
box_office_revenue = [42, 30, 15, 8, 12, 7, 6, 5, 3, 4, 2.5, 3, 2, 1.5, 1]  # in billions
total_films_released = [900, 700, 2000, 500, 450, 350, 300, 250, 200, 180, 
                        150, 140, 130, 120, 110]  # total films
avg_ratings = [7.8, 7.2, 6.5, 7.0, 7.6, 7.1, 7.3, 7.4, 6.9, 7.0, 7.5, 7.4, 6.8, 6.7, 6.5]  # average ratings

# Color for each country
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5']

# Using Box Office Revenue as the size of the bubble
sizes = [rev / max(box_office_revenue) * 2000 for rev in box_office_revenue]

# Set up the figure size
plt.figure(figsize=(18, 14))

# Scatter plot
plt.scatter(total_films_released, avg_ratings, s=sizes, c=colors, alpha=0.7)

# Labels and Title
plt.title('Film Industry Overview: Box Office Revenue, Films Released, and Ratings', fontsize=20, pad=30)
plt.xlabel('Total Films Released', fontsize=14)
plt.ylabel('Average Ratings', fontsize=14)

# Add country names to the bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (total_films_released[i], avg_ratings[i]), fontsize=10, ha='center')

# Show grid
plt.grid(True)

# Show the plot
plt.show()