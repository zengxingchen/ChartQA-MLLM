
import matplotlib.pyplot as plt

# Data from your provided table
data = [
    {'Class Type': 'Yoga', 'Gym Name': 'FlexFit', 'Season': 'Summer', 'Participants': 15, 'Calories Burned Per Session': 180, 'Session Length (Minutes)': 60},
    {'Class Type': 'Pilates', 'Gym Name': 'Wellness Works', 'Season': 'Summer', 'Participants': 10, 'Calories Burned Per Session': 220, 'Session Length (Minutes)': 60},
    # ... (include all other data points) ...
]

# Prepare the data for plotting
season_shapes = {'Summer': 'o', 'Winter': '^'} # Circle for Summer, triangle for Winter
colors = plt.cm.viridis  # Colormap for the calories burned data

# Determine the range for the colors normalization
calories_burned = [d['Calories Burned Per Session'] for d in data]
norm = plt.Normalize(min(calories_burned), max(calories_burned))

# Create the plot
fig, ax = plt.subplots()

# Plot each data point
for item in data:
    scatter = ax.scatter(
        item['Session Length (Minutes)'],  # x-axis: session length
        item['Class Type'],  # y-axis: class type
        s=item['Participants'] * 10,  # Bubble size based on participants, with a scaling factor
        c=[colors(norm(item['Calories Burned Per Session']))],  # Bubble color based on calories
        marker=season_shapes[item['Season']],  # Marker shape based on the season
        label='_nolegend_' if any(item['Class Type'] in s.get_text() for s in ax.get_yticklabels()) else item['Class Type'],  # Unique class type labels
        alpha=0.6,  # Bubble transparency
        edgecolors='w',  # Bubble edge color
        linewidths=0.5,  # Width of the edge
    )

# Create colorbar based on calories burned
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=colors), ax=ax)
cbar.set_label('Calories Burned Per Session')

# Customize the plot
ax.set_xlabel('Session Length (Minutes)')
ax.set_title('Fitness Class Participation')
ax.grid(True)

# Create a legend for seasons
season_patches = [plt.Line2D([0], [0], marker=shape, color='gray', markersize=10, label=season, linestyle='None') for season, shape in season_shapes.items()]
ax.legend(handles=season_patches, title='Season')

# Show the plot
plt.show()