
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Subject': ['Health', 'Fitness', 'Nutrition', 'Mental Health', 'Wellness', 'Exercise', 'Yoga', 
               'Diet', 'Meditation', 'Sleep', 'Hydration', 'Weight Loss', 'Cardio', 'Strength Training', 
               'Flexibility', 'Stress Management', 'Recovery'],
    'Participants': [800, 600, 400, 350, 300, 250, 200, 150, 120, 100, 90, 80, 70, 60, 50, 40, 30],
    'Percentage': [0.20, 0.15, 0.10, 0.09, 0.075, 0.0625, 0.05, 0.0375, 0.03, 0.025, 0.0225, 0.02, 0.0175, 0.015, 0.0125, 0.01, 0.0075]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#ADFF2F', '#FF69B4', 
          '#CD5C5C', '#FFA07A', '#20B2AA', '#9370DB', '#8FBC8F', '#4682B4', '#BDB76B', 
          '#FF4500', '#DAA520', '#B0E0E6']

# Plot the Treemap
plt.figure(figsize=(18, 14))
squarify.plot(sizes=df['Percentage'], label=df['Subject'], color=colors, alpha=0.8)
plt.title('Popularity of Health & Fitness Topics among Participants', fontsize=22, y=1.05)
plt.axis('off')
plt.show()