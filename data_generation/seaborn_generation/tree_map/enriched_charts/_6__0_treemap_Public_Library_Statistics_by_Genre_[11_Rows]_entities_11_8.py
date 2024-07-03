
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with the updated data
df = pd.DataFrame({
    'topic': ['Sports & Fitness'] * 11 + ['Health & Psychology'] * 10,
    'sub_topic': ['Running', 'Gym Equipment', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting', 'Cardio Machines', 'Pilates', 'Boxing', 'Martial Arts', 'Rowing', 'Mental Health', 'Nutrition', 'Physical Health', 'Wellness', 'Self-care', 'Fitness', 'Stress Management', 'Sleep Health', 'Work-life Balance', 'Addiction Recovery'],
    'value': [1500, 1200, 900, 1100, 800, 700, 600, 500, 400, 300, 200, 1000, 850, 750, 650, 550, 450, 350, 250, 150, 100]
})

# Create a color list with specific color codes for better clarity
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666', '#c2f0c2', '#e0e0d1', '#ffccff', '#f1c232', '#8e7cc3', '#76a5af', '#d9d2e9', '#b6d7a8', '#f4cccc', '#c9daf8', '#d5a6bd', '#ffd966', '#a2c4c9']

# Plot
plt.figure(figsize=(22, 12))
squarify.plot(sizes=df['value'], label=df['sub_topic'], color=colors, alpha=.8)
plt.title('Market Segmentation in Sports & Health', fontsize=25, pad=15)
plt.axis('off')
plt.show()