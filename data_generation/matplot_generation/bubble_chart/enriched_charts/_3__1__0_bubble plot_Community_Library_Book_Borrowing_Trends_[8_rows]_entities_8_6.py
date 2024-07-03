
import matplotlib.pyplot as plt

# Defining the data
categories = ['Fruits', 'Vegetables', 'Whole Grains', 'Lean Proteins', 'Dairy Products',
              'Nuts and Seeds', 'Seafood', 'Legumes', 'Herbs and Spices', 'Fermented Foods',
              'Beverages', 'Sweets and Desserts']
popularity = [90, 88, 85, 82, 78, 75, 72, 70, 68, 65, 60, 55]
nutritional_value = [95, 90, 88, 85, 80, 78, 82, 75, 70, 77, 65, 50]
respondents = [600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50]

# Rescaling respondents for bubble size
size = [respondent / 2 for respondent in respondents]

# Create a bubble chart
fig, ax = plt.subplots(figsize=(14, 10))

# Using specific color codes for better clarity
colors = ['#FF6347', '#3CB371', '#FFD700', '#4682B4', '#8A2BE2',
          '#FF69B4', '#1E90FF', '#32CD32', '#FF4500', '#DA70D6',
          '#6495ED', '#FF1493']

for i in range(len(categories)):
    ax.scatter(popularity[i], nutritional_value[i], s=size[i],
               alpha=0.6, color=colors[i])

# Loop to annotate each bubble
for i, txt in enumerate(categories):
    ax.annotate(txt, (popularity[i], nutritional_value[i]), ha='center', va='center')

# Set the chart's title and labels
ax.set_title('Popularity and Nutritional Value of Different Food Categories', fontsize=18, pad=20)
ax.set_xlabel('Popularity among consumers', fontsize=14)
ax.set_ylabel('Nutritional Value', fontsize=14)

# Change the axes limits
ax.set_xlim(50, 100)
ax.set_ylim(45, 100)

# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()