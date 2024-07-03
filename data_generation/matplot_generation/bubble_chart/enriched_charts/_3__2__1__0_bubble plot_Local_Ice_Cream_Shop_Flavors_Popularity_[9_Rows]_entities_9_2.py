
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'India', 'Japan', 'United Kingdom', 
             'France', 'South Korea', 'Germany', 'Australia', 'Canada', 
             'Brazil', 'Italy', 'Russia', 'Mexico', 'Spain', 
             'Netherlands', 'Switzerland', 'Sweden', 'Singapore']
box_office_revenue = [11.1, 8.6, 3.2, 2.4, 1.9, 1.6, 1.4, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]  # Billions USD
movie_production = [700, 600, 2000, 300, 250, 220, 150, 160, 100, 110, 120, 130, 140, 180, 170, 90, 80, 70, 60]  # Movies produced per year
audience_ratings = [85.0, 75.5, 60.1, 78.6, 82.9, 79.0, 83.4, 80.2, 80.7, 81.3, 60.5, 70.0, 65.8, 58.9, 71.2, 84.0, 87.6, 86.2, 89.4]  # Audience rating scores

# Color for each country
colors = ['#FF5733', '#C70039', '#FFC300', '#DAF7A6', '#581845', 
          '#900C3F', '#1ABC9C', '#2E86C1', '#5DADE2', '#AF7AC5', 
          '#D35400', '#E74C3C', '#2ECC71', '#1F618D', '#A569BD',
          '#C0392B', '#F39C12', '#27AE60', '#2980B9']

# Using Box Office Revenue as the size of the bubble
sizes = [bo / max(box_office_revenue) * 2000 for bo in box_office_revenue]

# Set up the figure size
plt.figure(figsize=(20, 12))

# Scatter plot
plt.scatter(audience_ratings, movie_production, s=sizes, c=colors, alpha=0.7)

# Labels and Title
plt.title('Box Office Revenue vs Movie Production and Audience Ratings', fontsize=20, pad=20)
plt.xlabel('Audience Rating Scores', fontsize=14)
plt.ylabel('Movies Produced per Year', fontsize=14)

# Add country names to the bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (audience_ratings[i], movie_production[i]), fontsize=10, ha='center')

# Show grid
plt.grid(True)

# Show the plot
plt.show()