
import matplotlib.pyplot as plt

# Table data provided
data = [
    {'Day': 'Monday', 'Healthy Recipes': 200, 'Workout Plans': 150, 'Mental Health Articles': 180, 'Self-Care Tips': 140, 'Healthy Snacks': 220},
    {'Day': 'Tuesday', 'Healthy Recipes': 210, 'Workout Plans': 160, 'Mental Health Articles': 190, 'Self-Care Tips': 150, 'Healthy Snacks': 230},
    {'Day': 'Wednesday', 'Healthy Recipes': 220, 'Workout Plans': 170, 'Mental Health Articles': 200, 'Self-Care Tips': 160, 'Healthy Snacks': 240},
    {'Day': 'Thursday', 'Healthy Recipes': 230, 'Workout Plans': 180, 'Mental Health Articles': 210, 'Self-Care Tips': 170, 'Healthy Snacks': 250},
    {'Day': 'Friday', 'Healthy Recipes': 240, 'Workout Plans': 190, 'Mental Health Articles': 220, 'Self-Care Tips': 180, 'Healthy Snacks': 260},
    {'Day': 'Saturday', 'Healthy Recipes': 250, 'Workout Plans': 200, 'Mental Health Articles': 230, 'Self-Care Tips': 190, 'Healthy Snacks': 270},
    {'Day': 'Sunday', 'Healthy Recipes': 260, 'Workout Plans': 210, 'Mental Health Articles': 240, 'Self-Care Tips': 200, 'Healthy Snacks': 280}
]

# Extracting data for plotting
days = [item['Day'] for item in data]
healthy_recipes = [item['Healthy Recipes'] for item in data]
workout_plans = [item['Workout Plans'] for item in data]
mental_health_articles = [item['Mental Health Articles'] for item in data]
self_care_tips = [item['Self-Care Tips'] for item in data]
healthy_snacks = [item['Healthy Snacks'] for item in data]

# Creating a line chart with a different line style and marker for each type
plt.figure(figsize=(16, 12))
plt.plot(days, healthy_recipes, label='Healthy Recipes', linestyle='-', marker='o', color='#1f77b4')
plt.plot(days, workout_plans, label='Workout Plans', linestyle='--', marker='s', color='#ff7f0e')
plt.plot(days, mental_health_articles, label='Mental Health Articles', linestyle='-.', marker='^', color='#2ca02c')
plt.plot(days, self_care_tips, label='Self-Care Tips', linestyle=':', marker='D', color='#d62728')
plt.plot(days, healthy_snacks, label='Healthy Snacks', linestyle='-', marker='*', color='#9467bd')

# Adding relevant titles and labels
plt.title('Weekly Health & Wellness Content Engagement', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Views')
plt.legend(loc='upper right')

# Customizing the grid
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Adding annotations for Healthy Snacks
for i, txt in enumerate(healthy_snacks):
    plt.annotate(txt, (days[i], healthy_snacks[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Invert y-axis
plt.gca().invert_yaxis()

# Displaying the chart
plt.tight_layout()
plt.show()