
import matplotlib.pyplot as plt
import squarify

# Data points for the treemap
categories = ['Cardiovascular Health', 'Mental Wellness', 'Nutrition', 'Sleep Quality', 'Physical Fitness', 
              'Stress Management', 'Hydration', 'Medical Check-ups', 'Immunity Boosting', 'Weight Management', 
              'Exercise Routines', 'Healthy Eating', 'Meditation', 'Vitamins & Supplements', 'Work-life Balance', 
              'Social Connections', 'Workouts', 'Yoga', 'Pilates']
count = [1300, 1150, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150]

# TreeMap customization
color_palette = ['#FF6347', '#FFD700', '#8A2BE2', '#5F9EA0', '#7FFF00', '#FF7F50', '#DC143C', '#00FFFF', '#00008B', 
                 '#B8860B', '#A9A9A9', '#006400', '#8B008B', '#556B2F', '#FF8C00', '#9932CC', '#8B0000', '#E9967A', '#8FBC8F']
plt.figure(figsize=(16, 9))

# Creating the treemap
squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.8)

# Title and labels
plt.title('Health & Psychology Topics by Popularity', fontsize=20, fontweight='bold')
plt.axis('off')

plt.show()