
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Category': [
        'Fitness Training', 'Yoga & Meditation', 'Cardio Workouts', 'Strength Training', 'Flexibility Exercises',
        'Sports Activities', 'Wellness Programs', 'Outdoor Adventures', 'Nutrition Plans', 'Mental Health Activities',
        'Recreational Sports', 'Recovery Techniques'
    ],
    'Value': [
        500, 450, 400, 350, 300,
        550, 320, 370, 280, 340,
        360, 290
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1',
    '#955251', '#B565A7', '#009B77', '#DD4124', '#D65076',
    '#45B8AC', '#EFC050'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=df['Value'], label=df['Category'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Popularity of Sports & Fitness Activities', fontsize=22, y=1.05)

# Show the plot
plt.show()