
import matplotlib.pyplot as plt

# Defining the data
categories = ['Machine Learning', 'Web Development', 'Mobile Apps', 'Data Science', 
              'Cloud Computing', 'Cybersecurity', 'AI', 'Blockchain', 'DevOps', 
              'IoT', 'AR/VR', 'Game Development']
popularity = [92, 85, 78, 88, 70, 65, 90, 55, 72, 68, 50, 60]
satisfaction = [88, 80, 75, 85, 68, 70, 89, 60, 74, 65, 55, 67]
respondents = [600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50]

# Rescaling respondents for bubble size
size = [respondent / 2 for respondent in respondents]

# Create a bubble chart
fig, ax = plt.subplots(figsize=(12, 9))

# Using specific color codes for better clarity
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8333', 
          '#33FFA1', '#A133FF', '#33FFF2', '#FF5733', '#337FFF',
          '#8D33FF', '#FFC433']

for i in range(len(categories)):
    ax.scatter(popularity[i], satisfaction[i], s=size[i],
               alpha=0.6, color=colors[i])

# Loop to annotate each bubble
for i, txt in enumerate(categories):
    ax.annotate(txt, (popularity[i], satisfaction[i]), ha='center', va='center')

# Set the chart's title and labels
ax.set_title('Popularity and Satisfaction in Emerging Tech Fields', fontsize=18)
ax.set_xlabel('Popularity among professionals', fontsize=14)
ax.set_ylabel('Satisfaction', fontsize=14)

# Change the axes limits
ax.set_xlim(45, 100)
ax.set_ylim(50, 100)

# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()