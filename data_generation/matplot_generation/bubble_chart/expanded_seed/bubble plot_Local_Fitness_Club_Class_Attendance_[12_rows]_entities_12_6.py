
import matplotlib.pyplot as plt

# Example data
data = [
    {'ClassName': 'Yoga Basics', 'Instructor': 'Sarah E.', 'Difficulty Level': 'Beginner', 'Weekly Attendees': 25, 'Average Age of Participants': 35, 'Calories Burned Per Session': 180},
    {'ClassName': 'Cycling Rush', 'Instructor': 'Mike B.', 'Difficulty Level': 'Intermediate', 'Weekly Attendees': 30, 'Average Age of Participants': 29, 'Calories Burned Per Session': 500},
    {'ClassName': 'HIIT Explosive', 'Instructor': 'Ali T.', 'Difficulty Level': 'Advanced', 'Weekly Attendees': 20, 'Average Age of Participants': 27, 'Calories Burned Per Session': 600},
    {'ClassName': 'Zumba Dance Party', 'Instructor': 'Lucy G.', 'Difficulty Level': 'All Levels', 'Weekly Attendees': 40, 'Average Age of Participants': 33, 'Calories Burned Per Session': 350},
    # ... (Other data points)
    {'ClassName': 'Morning Meditation', 'Instructor': 'Gary D.', 'Difficulty Level': 'All Levels', 'Weekly Attendees': 30, 'Average Age of Participants': 38, 'Calories Burned Per Session': 50}
]

# Prepare data for plotting
x = [d['Average Age of Participants'] for d in data]
y = [d['Weekly Attendees'] for d in data]
sizes = [d['Calories Burned Per Session'] for d in data]  # Bubble sizes
difficulty_levels = [d['Difficulty Level'] for d in data]
colors = {'Beginner': 'green', 'Intermediate': 'blue', 'Advanced': 'red', 'All Levels': 'purple'}

# Create a scatter plot
fig, ax = plt.subplots()
for xi, yi, si, di in zip(x, y, sizes, difficulty_levels):
    ax.scatter(xi, yi, s=si*5, c=colors[di], label=di, alpha=0.6, edgecolors='w')

# Annotate data point names
for i, class_name in enumerate(data):
    ax.text(x[i], y[i], class_name['ClassName'], fontsize=9, ha='center')

# Setting the legend to show unique difficulty levels only
handles, labels = ax.get_legend_handles_labels()
unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
ax.legend(*zip(*unique), loc='upper right')

# Title and labels
plt.title('Fitness Class Attendance and Calories Burned')
plt.xlabel('Average Age of Participants')
plt.ylabel('Weekly Attendees')

# Show the plot
plt.show()