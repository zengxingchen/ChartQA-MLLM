
import matplotlib.pyplot as plt

# Define data
names = [
    "Usain Bolt", "Michael Phelps", "Serena Williams", "Lionel Messi",
    "LeBron James", "Roger Federer", "Cristiano Ronaldo", "Simone Biles",
    "Novak Djokovic", "Tiger Woods", "Katie Ledecky", "Tom Brady",
    "Rafael Nadal", "Stephen Curry", "Venus Williams"
]

performance_score = [
    98, 96, 92, 94, 90, 88, 93, 95, 91, 85, 89, 87, 90, 86, 84
]

endurance_level = [
    85, 88, 82, 80, 78, 84, 79, 90, 83, 70, 86, 75, 81, 74, 77
]

hours_training_per_week = [
    25, 30, 20, 22, 25, 18, 23, 27, 21, 15, 28, 20, 22, 24, 19
]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(16, 9))

# Bubble sizes as a fraction of hours_training_per_week (adjust the scaling as needed)
sizes = [hours_training_per_week[i] * 10 for i in range(len(hours_training_per_week))]

# Scatter plot (using performance_score as weight for bubble size)
scatter = ax.scatter(
    performance_score, endurance_level, s=sizes, alpha=0.6,
    color=['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2',
           '#FF69B4', '#1E90FF', '#FF4500', '#7B68EE', '#48D1CC',
           '#DAA520', '#ADFF2F', '#D2691E', '#FF7F50', '#6495ED']
)

# Customize the appearance
ax.set_title('Top Athletes\' Performance Metrics', fontsize=18)
ax.set_xlabel('Performance Score', fontsize=14)
ax.set_ylabel('Endurance Level', fontsize=14)
ax.grid(True)

# Adding the names of the athletes to the bubbles
for i, txt in enumerate(names):
    ax.annotate(txt, (performance_score[i], endurance_level[i]))

plt.show()