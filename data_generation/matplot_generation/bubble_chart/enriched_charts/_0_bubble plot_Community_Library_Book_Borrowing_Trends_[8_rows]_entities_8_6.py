
import matplotlib.pyplot as plt

# Defining the data
languages = ['Python', 'JavaScript', 'Java', 'C#', 'PHP', 'Ruby',
             'C++', 'Swift', 'Go', 'Kotlin', 'Rust', 'Dart']
popularity  = [90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35]
satisfaction = [85, 70, 65, 75, 60, 80, 70, 85, 90, 75, 95, 80]
respondents = [600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50]

# Rescaling respondents for bubble size
size = [respondent / 2 for respondent in respondents]

# Create a bubble chart
fig, ax = plt.subplots(figsize=(10, 8))  # Changed width and height

for i in range(len(languages)):
    ax.scatter(popularity[i], satisfaction[i], s=size[i],
               alpha=0.5, color=f"C{i}")

# Loop to annotate each bubble
for i, txt in enumerate(languages):
    ax.annotate(txt, (popularity[i], satisfaction[i]), ha='center', va='center')

# Set the chart's title and labels
ax.set_title('Developer Satisfaction and Popularity of Languages', fontsize=15)
ax.set_xlabel('Popularity among developers', fontsize=12)
ax.set_ylabel('Satisfaction', fontsize=12)

# Change the axes limits
ax.set_xlim(30, 100)
ax.set_ylim(50, 100)

# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()