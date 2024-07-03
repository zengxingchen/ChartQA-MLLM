
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India', 
             'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada', 
             'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico']
investment_in_sports = [110, 90, 70, 50, 20, 60, 40, 30, 35, 45, 
                        55, 25, 28, 50, 15]  # in billions
olympic_medals = [2800, 2000, 1500, 1300, 700, 1700, 1600, 1300, 
                  1500, 1800, 2200, 1200, 1100, 1900, 800]  # total medals
avg_hours_physical_activity = [5.5, 4.8, 4.1, 5.2, 2.9, 4.6, 4.9, 3.8, 
                               4.4, 6.1, 5.0, 3.7, 4.3, 6.5, 3.1]  # hours per week

# Color for each country
colors = ['#ff6f61', '#6a0dad', '#ffdd57', '#ff7f50', '#4682b4', 
          '#d2691e', '#6495ed', '#dda0dd', '#9acd32', '#ee82ee', 
          '#40e0d0', '#ff4500', '#32cd32', '#ff69b4', '#8a2be2']

# Using Investment in Sports as the size of the bubble
sizes = [inv / max(investment_in_sports) * 2000 for inv in investment_in_sports]

# Set up the figure size
plt.figure(figsize=(16, 12))

# Scatter plot
plt.scatter(olympic_medals, avg_hours_physical_activity, s=sizes, c=colors, alpha=0.7)

# Labels and Title
plt.title('Investment in Sports vs Olympic Medals and Physical Activity', fontsize=18, pad=20)
plt.xlabel('Total Olympic Medals', fontsize=14)
plt.ylabel('Average Hours of Physical Activity per Week', fontsize=14)

# Add country names to the bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (olympic_medals[i], avg_hours_physical_activity[i]), fontsize=10, ha='center')

# Show grid
plt.grid(True)

# Show the plot
plt.show()