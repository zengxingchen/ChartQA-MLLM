
import matplotlib.pyplot as plt

# Sample data
data = [
    {'Week': 'Week 1', 'Reading (hours)': 3, 'Video Gaming (hours)': 5, 'Gardening (hours)': 1.0, 'Exercising (hours)': 2.0, 'Cooking (hours)': 4.0},
    {'Week': 'Week 2', 'Reading (hours)': 4, 'Video Gaming (hours)': 6, 'Gardening (hours)': 1.5, 'Exercising (hours)': 2.5, 'Cooking (hours)': 3.0},
    {'Week': 'Week 3', 'Reading (hours)': 5, 'Video Gaming (hours)': 4, 'Gardening (hours)': 2.0, 'Exercising (hours)': 3.0, 'Cooking (hours)': 3.5},
    {'Week': 'Week 4', 'Reading (hours)': 3, 'Video Gaming (hours)': 5, 'Gardening (hours)': 2.5, 'Exercising (hours)': 4.0, 'Cooking (hours)': 4.0},
    {'Week': 'Week 5', 'Reading (hours)': 4, 'Video Gaming (hours)': 4, 'Gardening (hours)': 3.0, 'Exercising (hours)': 3.5, 'Cooking (hours)': 4.5},
    {'Week': 'Week 6', 'Reading (hours)': 3, 'Video Gaming (hours)': 6, 'Gardening (hours)': 2.5, 'Exercising (hours)': 4.0, 'Cooking (hours)': 3.0},
    {'Week': 'Week 7', 'Reading (hours)': 4, 'Video Gaming (hours)': 5, 'Gardening (hours)': 3.0, 'Exercising (hours)': 4.5, 'Cooking (hours)': 4.0}
]

# Extracting weeks and activity hours from the dataset
weeks = [d['Week'] for d in data]
reading_hours = [d['Reading (hours)'] for d in data]
video_gaming_hours = [d['Video Gaming (hours)'] for d in data]
gardening_hours = [d['Gardening (hours)'] for d in data]
exercising_hours = [d['Exercising (hours)'] for d in data]
cooking_hours = [d['Cooking (hours)'] for d in data]

# Stacked area chart
plt.stackplot(weeks, reading_hours, video_gaming_hours, gardening_hours, exercising_hours, cooking_hours,
              labels=['Reading', 'Video Gaming', 'Gardening', 'Exercising', 'Cooking'],
              colors=['steelblue', 'orange', 'lightgreen', 'red', 'purple'],
              alpha=0.5)

# Adding labels and title
plt.xlabel('Week')
plt.ylabel('Total Hours Spent')
plt.title('Weekly Activity Distribution')

# Adding a legend
plt.legend(loc='upper left')

# Optional: add grid
plt.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.tight_layout()  # Adjust the padding between and around subplots
plt.show()