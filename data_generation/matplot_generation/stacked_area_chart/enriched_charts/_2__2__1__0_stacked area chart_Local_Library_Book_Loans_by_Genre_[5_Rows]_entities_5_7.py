
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2023))
science = [7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500]
technology = [8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500]
engineering = [9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500]

# Start plotting
fig, ax = plt.subplots(figsize=(16, 12))

# Plot stacked area chart
ax.stackplot(years, science, technology, engineering, colors=['#FF5733', '#33FF57', '#3357FF'])

# Annotate specific points
ax.annotate('Rise in Technology', xy=(2021, 13000), xytext=(2015, 14000),
            arrowprops=dict(facecolor='#33FF57', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.title('Engagement in STEM Fields (2011-2022)', pad=40)

# Show the plot
plt.show()