
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2022))
action_movies = [120, 140, 160, 190, 220, 260, 300, 350, 410, 480, 560]
comedy_movies = [150, 170, 190, 220, 260, 300, 350, 410, 470, 540, 620]
drama_movies = [180, 200, 230, 270, 310, 360, 420, 490, 570, 660, 760]

# Start plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked area chart
ax.stackplot(years, action_movies, comedy_movies, drama_movies, colors=['#FF5733', '#33FF57', '#3357FF'])

# Annotate specific points
ax.annotate('Significant rise in Drama Movies', xy=(2020, 660), xytext=(2015, 500),
            arrowprops=dict(facecolor='#3357FF', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Movies Released')
plt.title('Movie Releases by Genre (2011-2021)', pad=20)

# Add legend
plt.legend(['Action Movies', 'Comedy Movies', 'Drama Movies'], loc='upper left')

# Show the plot
plt.show()